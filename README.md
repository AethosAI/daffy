# Daffy

## Summary
Daffy is a CLI tool meant to provide annotation export capabilities for Label Studio outside of the tool. The user can specify their desired export format (see list below) and download annotations or download all available "tasks". Daffy was created primarily to operate inside of Pachyderm as a containerized tool for a pipeline step (see below). 

Read our article for more information on our setup with Pachyderm: _link_

### Installation

#### Container
It is **suggested** to simply use the latest release of the container using Docker or Podman. The entry point of the containter is `daffy` and can be run with standard run commands inside either tool:

```podman run [image] daffy COMMAND [options]```

#### Python
Daffy can also be installed locally as a python CLI tool:

```python setup.py install```

## Usage
Daffy was built using Click for a better CLI user experience. Each "argument" is defined as an option for ease of use, but note that some of the options are required (see Options below).

To see all available commands and options:

```daffy --help```

### Command: Export

```daffy export [options]```

For help:

```daffy export --help```

In the following example a user would connect to their instance of Label Studio using their host path and API token _You can find your user token on the User Account page in Label Studio_. They are then specifying the project id and the VOC export type (VOC being used generally for Tensorflow object detection projects):

```daffy export -h http(s)://path:port -t [api_token] -p [project_id] -e VOC```

#### Options:

`--host_path, -h`: Path to the host machine running Label Studio [http(s)://path:port]

`--token, -t`: Label Studio Authorization Token

`--project_id, -p`: Project ID with annotations you would like to export

`--export_type, -e`: Export type you would like to use [see list]

`--unzip, u`: Boolean to set if you'd like to unzip files exported from supported export types, defaults to True and will be disabled for unsupported export types

`--download_all_tasks, -dat`: Download all tasks regardless of status.

`--download_resources, -dr`: Download additional resources [images, config] **Caution:** This option is not currently working in our testing.

#### Formats:

See [Formats](formats.json) for a list of all available formats, their export name and descriptions.

## Contributing

Thanks for considering, we need your contributions to help this project come to fruition.

Here are some important resources:

- Bugs? [Issues](https://github.com/rutheferd/daffy/issues) is where to report them!
- Please utilize pre-commits or manually invoke black and flake8 to ensure style compliance.

## License

   Copyright 2022 Georgia Tech Research Institute

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.
