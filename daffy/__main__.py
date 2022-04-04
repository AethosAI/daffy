import click
from daffy.src import export_command


@click.group()
def main():
    pass


@click.option(
    "--download_resources",
    "-dr",
    is_flag=True,
    help="Download additional resources",
)
@click.option(
    "--download_all_tasks",
    "-dat",
    is_flag=True,
    help="Download all tasks regardless of status.",
)
@click.option(
    "--unzip",
    "-u",
    type=click.BOOL,
    default=True,
    help="If you would like to unzip the output file [supported for certain export types]",
)
@click.option(
    "--export_type",
    "-e",
    required=True,
    type=click.STRING,
    help="Export type you would like to use. [JSON, VOC, etc...]",
)
@click.option(
    "--project_id",
    "-p",
    required=True,
    type=click.INT,
    help="Project ID with data you would like to export.",
)
@click.option(
    "--token",
    "-t",
    required=True,
    help="Label Studio authorization token",
)
@click.option(
    "--host_path",
    "-h",
    required=True,
    help="Path to the host machine running Label Studio [http(s)://path:port]",
)
@main.command()
def export(
    host_path,
    token,
    project_id,
    export_type,
    unzip,
    download_all_tasks,
    download_resources,
    ids,
):
    export_command.run(
        host_path,
        token,
        project_id,
        export_type,
        unzip=unzip,
        download_all_tasks=download_all_tasks,
        download_resources=download_resources,
        ids=ids,
    )


if __name__ == "__main__":
    main()
