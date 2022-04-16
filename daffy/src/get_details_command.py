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
import logging
import json

logging.basicConfig(
    format="[%(asctime)s] %(levelname)s: %(message)s",
    datefmt="%m/%d/%Y %I:%M:%S %p",
    level=logging.INFO,
)

OUT_FILE_NAME = "details.json"


def format_details(content, raw=False):
    # Decoding and Converting to JSON
    content = json.loads(content.decode("utf-8"))

    # Return JSON with no formatting
    logging.info("Skipping Format...")
    if raw:
        return json.dumps(content)

    logging.info("Formatting Content...")
    results = []
    for i in content["results"]:
        keys = ["id", "title", "description", "created_by"]
        simple_dict = {x: i[x] for x in keys}
        results.append(simple_dict)
    return json.dumps(results, indent=2)


def save_file(output, results):
    """Saves the results to file.

    Args:
        output (String): Path to the file to save results to, should be a JSON.
        results (String): Results of the API call for details. This is formatted for readability.
    """

    full_path = "{}/{}".format(output, OUT_FILE_NAME)

    logging.info("Writing to {}...".format(output))

    with open(full_path, "w+") as file:
        file.write(results)

    pass


def get_details(url, headers):

    logging.info("Connecting and Retrieving Data...")
    response = requests.get(url, headers=headers,)

    return response.content


def run(host_path, token, output=None, raw=False, print_out=True):
    token_string = "Token {}".format(token)
    headers = {"Authorization": token_string}
    logging.info("Building URL...")
    url = "{}/api/projects/".format(host_path)

    # Connect and download the details
    details = get_details(url, headers)

    # Format the details as defined
    results = format_details(details, raw)

    if print_out:
        logging.info(results)
        logging.info("Done!")

    if output is not None:
        save_file(output, results)

    pass
