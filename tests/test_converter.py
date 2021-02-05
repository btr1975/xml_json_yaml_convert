import pytest
import sys
import os
base_path = os.path.join(os.path.abspath(os.path.dirname(__name__)))
sys.path.append(os.path.join(base_path))
from xml_json_yaml_convert import Converter


def test_to_json(json_data_from_file_as_dict, json_data_from_file_as_string):
    test_obj = Converter(data=json_data_from_file_as_dict)

    assert test_obj.to_json() == json_data_from_file_as_string


def test_to_json_bad_data():
    test_obj = Converter(data='string')
    with pytest.raises(TypeError):
        test_obj.to_json()


def test_from_json_string(json_data_from_file_as_string, json_data_from_file_as_dict):
    test_obj = Converter(data=json_data_from_file_as_string)

    assert test_obj.from_json() == json_data_from_file_as_dict


def test_from_json_fp(json_data_from_file_as_dict):
    with open('tests/data/json_data.json', 'r') as file:
        test_obj = Converter(data=file)

        assert test_obj.from_json() == json_data_from_file_as_dict


def test_from_json_bad_data():
    test_obj = Converter(data=['list'])
    with pytest.raises(TypeError):
        test_obj.from_json()


def test_to_yaml(json_data_from_file_as_dict, yaml_data_from_file_as_string):
    test_obj = Converter(data=json_data_from_file_as_dict)

    assert test_obj.to_yaml() == yaml_data_from_file_as_string


def test_to_yaml_bad_data():
    test_obj = Converter(data='string')
    with pytest.raises(TypeError):
        test_obj.to_yaml()


def test_from_yaml_string(json_data_from_file_as_dict, yaml_data_from_file_as_string):
    test_obj = Converter(data=yaml_data_from_file_as_string)

    assert test_obj.from_yaml() == json_data_from_file_as_dict


def test_from_yaml_fp(json_data_from_file_as_dict):
    with open('tests/data/yaml_data.yml', 'r') as file:
        test_obj = Converter(data=file)

        assert test_obj.from_yaml() == json_data_from_file_as_dict


def test_from_yaml_bad_data():
    test_obj = Converter(data=['list'])
    with pytest.raises(TypeError):
        test_obj.from_yaml()


def test_to_xml(json_data_from_file_as_dict, xml_data_from_file_as_string):
    test_obj = Converter(data=json_data_from_file_as_dict)

    assert test_obj.to_xml() == xml_data_from_file_as_string


def test_to_xml_bad_data():
    test_obj = Converter(data='string')
    with pytest.raises(TypeError):
        test_obj.to_xml()


def test_form_yaml_bad_data():
    test_obj = Converter(data=['list'])
    with pytest.raises(TypeError):
        test_obj.from_yaml()


def test_from_xml_string(json_data_from_file_as_dict_ordered, xml_data_from_file_as_string):
    test_obj = Converter(data=xml_data_from_file_as_string)

    assert type(test_obj.from_xml()) == type(json_data_from_file_as_dict_ordered)


def test_from_xml_fp(json_data_from_file_as_dict_ordered):
    with open('tests/data/xml_data.xml', 'r') as file:
        test_obj = Converter(data=file)

        assert type(test_obj.from_xml()) == type(json_data_from_file_as_dict_ordered)


def test_from_xml_bad_data():
    test_obj = Converter(data=['list'])
    with pytest.raises(TypeError):
        test_obj.from_xml()
