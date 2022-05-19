from pyspark.sql.types import *
from pyspark.sql.session import SparkSession

from . import gaiaedr3_pyspark_schema_structures as edr3
from . import gaiadr3_pyspark_schema_structures as dr3
from .gaiadmpstore import *

spark = SparkSession.builder.getOrCreate()

class GaiaDMPSetup:
    """
    Prepare the PySpark env for GaiaDMP
    """

    def __init__(self):
        pass

    @staticmethod
    def setup():

        def tablesExist():
            actual_tables = [i.name for i in spark.catalog.listTables()]
            expected_tables = edr3.table_dict.keys() # | dr3.table_dict.keys() TODO add in DR3 tables expected once loaded
            check =  all(item in actual_tables for item in expected_tables)
            return check

        if not tablesExist():
        
            # database name to create
            database = "gaiaedr3"

            # create the database and switch the current SQL database context to it (from default)
            spark.sql("create database " + database)
            spark.sql("use " + database)

            # create the tables against their corresponding file sets and schema
            for table_key in edr3.table_dict.keys():
                folder_path = edr3.table_dict[table_key][1]
                schema = edr3.table_dict[table_key][0]
                reattachParquetFileResourceToSparkContext(table_key, data_store + folder_path, *schema)
                                                  
            # ... similarly for Gaia DR3
            database = "gaiadr3"
            spark.sql("create database " + database)
            spark.sql("use " + database)
            
            # TODO create the tables against their corresponding file sets and schema            
            #for table_key in dr3.table_dict.keys():
            #    folder_path = dr3.table_dict[table_key][0]
            #    schema = dr3.table_dict[table_key][1]
            #    reattachParquetFileResourceToSparkContext(table_key, data_store + folder_path, *schema)


GaiaDMPSetup.setup()
