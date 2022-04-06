# number of buckets for our platform
NUM_BUCKETS = 2048

spark = SparkSession.builder.getOrCreate()

# root data store path: TODO change this to the official one when established.
data_store = "file:////data/gaia/"  # "file:////user/nch/PARQUET/REPARTITIONED/"

# and to re-establish the resource in a new (or reset) spark context:
def reattachParquetFileResourceToSparkContext(table_name, file_path, *schema_structures):
	"""
	Creates a Spark (in-memory) meta-record for the table resource specified for querying
	through the PySpark SQL API.

	Assumes that the table contains the Gaia source_id attribute and that the files have
	been previously partitioned, bucketed and sorted on this field in parquet format
	- see function saveToBinnedParquet().  If the table name specified already exists in the
	catalogue IT WILL BE REMOVED (but the underlying data, assumed external, will remain).

	Parameters
	----------
	table_name : str
		The table name to be used as the identifier in SQL queries etc.
	file_path : str
		The full disk file system path name to the folder containing the parquet file set.
	schema_structures : StructType
		One or more schema structures expressed as a StructType object containing a list of
		StructField(field_name : str, type : data_type : DataType(), nullable : boolean)
	"""

	# put in the columns and their data types ...
	table_create_statement = "CREATE TABLE `" + table_name + "` ("
	for schema_structure in schema_structures:
		for field in schema_structure:
			table_create_statement += "`" + field.name + "` " + field.dataType.simpleString() + ","
	# ... zapping that extraneous comma at the end
	table_create_statement = table_create_statement[:-1]

	# append the organisational details
	table_create_statement += ") USING parquet OPTIONS (path '" + file_path + "') "
	table_create_statement += "CLUSTERED BY (source_id) SORTED BY (source_id) INTO %d" % (
		NUM_BUCKETS) + " BUCKETS"


	# scrub any existing record - N.B. tables defined in this way are EXTERNAL, so this statement will not scrub
	# the underlying file data set. Also if the table doesn't exist, this will silently do nothing (no exception
	# will be thrown).
	spark.sql("DROP TABLE IF EXISTS " + table_name)

	# create the table resource
	spark.sql(table_create_statement)
