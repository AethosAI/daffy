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

from click.testing import CliRunner
from daffy.__main__ import main
import pytest


@pytest.mark.skip(reason="Local CLI testing.")
def test_cli():
    """Currently Testing is Only Manual, tests will be added in the future to be run locally!"""
    host_path = "http://localhost:8080"
    token = "2a0f458a6c21efcf892c0047f68b6bf41e09f275"
    runner = CliRunner()
    result = runner.invoke(main, ["details", "-h", host_path, "-t", token])
    assert result.exit_code == 0
    result = runner.invoke(
        main, ["details", "-h", host_path, "-t", token, "-r"]
    )
    assert result.exit_code == 0
    pass
