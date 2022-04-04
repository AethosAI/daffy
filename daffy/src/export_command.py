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


def unzip_file():
    logging.info("Unzipping File...")
    with zipfile.ZipFile(ZIP_NAME, "r") as zip_ref:
        zip_ref.extractall()
    logging.info("Unzip done!")


def export(
    host_path,
    token,
    project_id,
    export_type,
    filename=ZIP_NAME,
    download_all_tasks=False,
    download_resources=False,
    ids="",
):

    logging.info("Exporting Files into the {} format...".format(export_type))

    token_string = "Token {}".format(token)

    headers = {"Authorization": token_string}

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

    with open(filename, "wb+") as file:
        file.write(response.content)

    logging.info("Export Complete!")

    return True


def run(
    host_path,
    token,
    project_id,
    export_type,
    unzip=True,
    download_all_tasks=False,
    download_resources=False,
    ids="",
):

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
        filename=filename,
        download_all_tasks=download_all_tasks,
        download_resources=download_resources,
        ids=ids,
    )

    if export_type in ZIP_EXPORT_TYPES:
        if unzip:
            unzip_file()
        else:
            logging.info("Skipping Unzip...")

    pass