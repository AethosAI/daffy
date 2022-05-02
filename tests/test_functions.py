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

import json

from requests import get
from daffy.src import get_details_command


def test_format():
    data_input = None
    data_output = None
    data_output_raw = None
    with open("tests/test_assets/detail_json_input.txt", "r") as f:
        data_input = f.read()
        data_input = str.encode(data_input, "utf-8")

    with open("tests/test_assets/detail_json_output.txt", "r") as f:
        data_output = f.read()

    formatted = get_details_command.format_details(data_input)

    assert formatted == data_output

    with open("tests/test_assets/detail_json_input.txt", "r") as f:
        data_input = f.read()
        data_input = str.encode(data_input, "utf-8")

    with open("tests/test_assets/detail_json_output-raw.txt", "r") as f:
        data_output_raw = f.read()

    formatted = get_details_command.format_details(data_input, raw=True)

    assert formatted == data_output_raw
