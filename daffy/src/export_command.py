######################################################
#   Copyright 2022 Georgia Tech Research Institute
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
######################################################

import requests
import zipfile
import logging

logging.basicConfig(
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
)

ZIP_NAME = "requests.zip"
ZIP_EXPORT_TYPES = ["VOC", "COCO", "YOLO"]
JSON_EXPORT_TYPES = ["JSON", "JSON_MIN"]


def unzip_file(path):
    """Unzips the downloaded file.

    Args:
        path (String): Path to the .zip file to be unzipped.
    """
    logging.info("Unzip Path: {}".format(path + "/" + ZIP_NAME))
    logging.info("Unzipping File...")
    with zipfile.ZipFile(path + "/" + ZIP_NAME, "r") as zip_ref:
        zip_ref.extractall(path)
    logging.info("Unzip done!")


def export(
    host_path,
    token,
    project_id,
    export_type,
    out_path,
    filename,
    download_all_tasks=False,
    download_resources=False,
    ids="",
):
    """Export function that utilizes the Label Studio API to download and convert annotations into the selected format.
    See the formats.json file for format details.

    Args:
        host_path (String): Label Studio host path
        token (String): Label Studio instance token (see README)
        project_id (int): ID of the project to download annotations from. Use daffy details command to list out project ids.
        export_type (String): See the formats.json file for available formats.
        out_path (String): Path to save output files.
        filename (string): Name to give output file. Defined in run function.
        download_all_tasks (bool, optional): Download all tasks regardless of status. Defaults to False.
        download_resources (bool, optional): Download additional resources [images, config] Caution: This option is not currently working in our testing. Defaults to False.
        ids (str, optional): Select multiple ids. Defaults to "".

    Returns:
        bool: Returns True if function was successful.
    """

    logging.info("Exporting Files into the {} format...".format(export_type))

    token_string = "Token {}".format(token)

    headers = {"Authorization": token_string}

    # Query options defined for API call.
    query = {
        "export_type": export_type,
        "download_all_tasks": download_all_tasks,
        "download_resources": download_resources,
        "ids": ids,
    }

    url = "{}/api/projects/{}/export".format(host_path, project_id)

    response = requests.get(
        url,
        params=query,
        headers=headers,
    )

    filepath = out_path + "/" + filename

    with open(filepath, "wb+") as file:
        file.write(response.content)

    logging.info("Export Complete!")

    return True


def run(
    host_path,
    token,
    project_id,
    export_type,
    out_path,
    unzip=True,
    download_all_tasks=False,
    download_resources=False,
    ids="",
):

    # Defining the appropriate filename for the expected output.
    if export_type in JSON_EXPORT_TYPES:
        logging.info("Setting output file to JSON...")
        filename = "requests.json"
    elif export_type == "CSV":
        logging.info("Setting output file to CSV...")
        filename = "requests.csv"
    elif export_type == "TSV":
        logging.info("Setting output file to TSV...")
        filename = "requests.tsv"
    elif export_type in ZIP_EXPORT_TYPES:
        filename = ZIP_NAME
        logging.info("Setting output file to ZIP...")

    _ = export(
        host_path,
        token,
        project_id,
        export_type,
        out_path,
        filename=filename,
        download_all_tasks=download_all_tasks,
        download_resources=download_resources,
        ids=ids,
    )

    if export_type in ZIP_EXPORT_TYPES:
        if unzip:
            unzip_file(out_path)
        else:
            logging.info("Skipping Unzip...")

    pass
