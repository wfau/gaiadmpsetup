from pyspark.sql.types import *
from pyspark.sql.session import SparkSession

from gaiaedr3-pyspark-schema-structures import *
from gaiadr3-pyspark-schema-structures import *
from gaiadmpstore import *

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
            expected_tables = gaiaedr3_tables # + gaiadr3_tables TODO add in DR3 tables expected once loaded
            check =  all(item in actual_tables for item in expected_tables)
            return check

        if not tablesExist():
        
            # database name to create
            database = "gaiaedr3"

            # create the database and switch the current SQL database context to it (from default)
            spark.sql("create database " + database)
            spark.sql("use " + database)

            # create the tables against their corresponding file sets and schema
            reattachParquetFileResourceToSparkContext("gaia_source", data_store + "GEDR3/GEDR3_GAIASOURCE", gaia_source_schema)
            reattachParquetFileResourceToSparkContext("gaia_source_tmasspsc_best_neighbours",
                                                  data_store + "GEDR3/GEDR3_2MASSPSC_BEST_NEIGHBOURS",
                                                  tmasspscxsc_best_neighbour_schema, twomass_psc_schema)
            reattachParquetFileResourceToSparkContext("gaia_source_allwise_best_neighbours",
                                                  data_store + "GEDR3/GEDR3_ALLWISE_BEST_NEIGHBOURS",
                                                  allwise_best_neighbour_schema, twomass_psc_schema)
            reattachParquetFileResourceToSparkContext("gaia_source_ps1_best_neighbours",
                                                  data_store + "GEDR3/GEDR3_PS1_BEST_NEIGHBOURS",
                                                  panstarrs1_best_neighbour_schema, panstarrs_dr1_otmo_schema)
                                                  
            # ... similarly for Gaia DR3
            database = "gaiadr3"
            spark.sql("create database " + database)
            spark.sql("use " + database)
            
            # TODO create the tables against their corresponding file sets and schema            



GaiaDMPSetup.setup()
