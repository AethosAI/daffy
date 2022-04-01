import click
from daffy.src import export_command


@click.group()
def main():
    pass


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
