from pyspark.sql.types import *
from pyspark.sql.session import SparkSession
from pyspark.sql.utils import AnalysisException

from . import gaiaedr3_pyspark_schema_structures as edr3
from . import gaiadr3_pyspark_schema_structures as dr3
from .gaiadmpstore import *
from gaiadmpconf import conf

from urllib.parse import urlsplit, unquote_plus
from pathlib import Path

spark = SparkSession.builder.getOrCreate()

class Location(object):

    def __init__(self, url):
        (scheme, net_loc, path, _, _) = urlsplit(url)
        path = Path(unquote_plus(path))
        self.parts = (scheme, net_loc, path)

    def __eq__(self, other):
        return self.parts == other.parts

    def __hash__(self):
        return hash(self.parts)

spark = SparkSession.builder.getOrCreate()

class GaiaDMPSetup:
    """
    Prepare the PySpark env for GaiaDMP
    """

    databases = {
        'gaiaedr3': edr3,
        'gaiadr3': dr3,
    }

    def __init__(self):
        pass

    @staticmethod
    def setup():

        data_store = conf.GAIA_DATA_LOCATION

        def tablesExist(expected_tables, database):
        
            check = False
            
            try:
            
                spark.sql("use " + database)
                actual_tables = [i.name for i in spark.catalog.listTables()]
                check =  all(item in actual_tables for item in expected_tables)
            
            except AnalysisException: pass
                
            return check

        def location_changed(expected_location, schema):
            check = False
            for table_key in schema.table_dict.keys():
                location = spark.sql(f"desc formatted {table_key}").filter("col_name=='Location'").collect()[0].data_type
                folder_path = schema.table_dict[table_key][1]
                if Location(location) != Location(expected_location + folder_path):
                    check = True
                # only compare the first table, assuming they are all the same
                break
            return check

        for database, schema in GaiaDMPSetup.databases.items():
            if not tablesExist(schema.table_dict.keys(), database) or location_changed(data_store, schema):

                # create the database and switch the current SQL database context to it (from default)
                spark.sql("create database if not exists " + database)
                spark.sql("use " + database)

                # create the tables against their corresponding file sets and schema
                for table_key in schema.table_dict.keys():
                    folder_path = schema.table_dict[table_key][1]
                    schemas = schema.table_dict[table_key][0]
                    pk = schema.table_dict[table_key][2]
                    reattachParquetFileResourceToSparkContext(table_key, data_store + folder_path, schemas, cluster_key = pk, sort_key = pk)
        
        # finally always leave the PySpark SQL context in the most recent Gaia DR3 database
        spark.sql("use gaiadr3")

GaiaDMPSetup.setup()

