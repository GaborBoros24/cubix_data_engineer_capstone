from pyspark.sql import DataFrame, SparkSession


from cubix_data_engineer_capstone.utils.config import STORAGE_ACCOUNT_NAME


def read_file_from_datalake(
        container_name: str, file_path: str, format: str) -> DataFrame:
    """Reads a file from Azure Data Lake and returns it as a Spark DataFrame.

    Parameters
    ----------
    container_name : str
        The name of the file system (container) in Azure Data Lake.
    file_path : str
        The path to the file in the data lake.
    format : str
        The format of the file ("csv", "json", "delta", "parquet").
    Returns
    -------
    DataFrame
        DataFrame with a loaded data.
    """
    if format not in ["csv", "json", "delta", "parquet"]:
        raise ValueError(f"Invalid format: {format}. Supported formats are: csv, json, delta, parquet.")  # noqa: E501

    full_path = (f"abfss://{container_name}@{STORAGE_ACCOUNT_NAME}.dfs.core.windows.net/{file_path}")  # noqa: E501

    spark = SparkSession.getActiveSession()
    if not spark:
        raise RuntimeError("No active SparkSession found.")

    if format == "json":
        df = spark.read.json(file_path)
        return df
    else:
        df = (
            spark
            .read
            .format(format)
            .option("header", "true")
            .load(full_path, format=format)
        )

    return df


def write_file_to_datalake(
        df: DataFrame,
        container_name: str,
        file_path: str,
        format: str,
        mode: str = "overwrite",
        partition_by: list[str] = None
) -> None:
    """Writes a DataFrame to Azure Data Lake as a parquet / csv / delta format.

    Parameters
    ----------
    df:             DataFrame to be written.
    container_name: The name of the file system (container) in Azure Data Lake.
    file_path:      The path to the file in the data lake.
    format:         The format of the file ("csv", "json", "delta", "parquet").
    mode:           Default "overwrite" write mode.
    partition_by:   List of columns to partition by, default is None.

    """

    if format not in ["csv", "delta", "parquet"]:
        raise ValueError(f"Invalid format: {format}. Supported formats are: csv, json, delta, parquet.")  # noqa: E501

    full_path = (f"abfss://{container_name}@{STORAGE_ACCOUNT_NAME}.dfs.core.windows.net/{file_path}")  # noqa: E501

    writer = df.write.mode(mode).format(format)

    if format == "csv":
        writer = writer.option("header", True)

    if partition_by:
        writer = writer.partitionBy(*partition_by)

    writer.save(full_path)  

