from cubix_data_engineer_capstone.utils.datalake import read_file_from_datalake, write_file_to_datalake  # noqa: E501


def bronze_ingest(
        source_path: str,
        bronze_path: str,
        file_name: str,
        container_name: str,
        format: str,
        mode: str,
        partition_by: list[str]
):
    """_summary_

    :param source_path: _description_
    :param bronze_path: _description_
    :param file_name: _description_
    :param container_name: _description_
    :param format: _description_
    :param mode: _description_
    :param partition_by: _description_
    :return: _description_
    """

    df = read_file_from_datalake(container_name, f"{source_path}/{file_name}", format)  # noqa: E501

    return write_file_to_datalake(
        df=df,
        container_name=container_name,
        file_path=f"{bronze_path}/{file_name}",
        format=format,
        mode=mode,
        partition_by=partition_by
    )
