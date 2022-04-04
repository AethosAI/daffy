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

from setuptools import setup, find_packages
from io import open
from os import path
import pathlib

# The directory containing this file
HERE = pathlib.Path(__file__).parent
# The text of the README file
README = (HERE / "README.md").read_text()
# automatically captured required modules for install_requires in requirements.txt and as well as configure dependency links
with open(path.join(HERE, "requirements.txt"), encoding="utf-8") as f:
    all_reqs = f.read().split("\n")
install_requires = [
    x.strip()
    for x in all_reqs
    if ("git+" not in x) and (not x.startswith("#")) and (not x.startswith("-"))
]
dependency_links = [x.strip().replace("git+", "") for x in all_reqs if "git+" not in x]

setup(
    name="daffy",
    description="Tool to allow container based training and prediction of Machine Learning Models.",
    include_package_data=True,
    package_data={
        "": ["*.txt"],
    },
    version="0.0.2",
    packages=find_packages(),  # list of all packages
    install_requires=install_requires,
    python_requires=">=3.10",  # any python greater than 2.7
    entry_points="""
        [console_scripts]
        daffy=daffy.__main__:main
    """,
    author="Austin Ruth",
    keywords="integration, pachyderm, label studio, AI alliance",
    long_description=README,
    long_description_content_type="text/markdown",
    license="Apache 2.0",
    url="https://github.com/gtri/daffy",
    download_url="",
    dependency_links=dependency_links,
    author_email="aruth3@gatech.edu",
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
    ],
)
