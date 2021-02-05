import sys
import os
import json
from collections import OrderedDict
import pytest
base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path, 'xml_json_yaml_convert'))


@pytest.fixture
def json_data_from_file_as_dict():
    with open('tests/data/json_data.json', 'r') as file:
        string_data = json.load(file)

    return string_data


@pytest.fixture
def json_data_from_file_as_dict_ordered():
    with open('tests/data/json_data.json', 'r') as file:
        string_data = json.load(file, object_pairs_hook=OrderedDict)

    return string_data


@pytest.fixture
def json_data_from_file_as_string():
    with open('tests/data/json_data.json', 'r') as file:
        string_data = file.read()

    return string_data


@pytest.fixture
def xml_data_from_file_as_string():
    with open('tests/data/xml_data.xml', 'r') as file:
        string_data = file.read()

    return string_data


@pytest.fixture
def yaml_data_from_file_as_string():
    with open('tests/data/yaml_data.yml', 'r') as file:
        string_data = file.read()

    return string_data
