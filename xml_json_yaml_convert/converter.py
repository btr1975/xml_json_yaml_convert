"""
Module to convert between XML, JSON, and YAML
"""
import json
import _io
import yaml
import xmltodict


class Converter:
    """Class to convert between XML, JSON, and YAML

    :type data: String, Dict, fp(_io.TextIOWrapper)
    :param data: The data to convert to what you want

    """

    def __init__(self, data=None):
        self.data = data

    def to_xml(self):
        """Method to convert a Dict to a String XML

        :rtype: String
        :returns: XML Data

        :raises TypeError: If data is not a Dict

        """
        if not isinstance(self.data, dict):
            raise TypeError(f'to_xml expected a dict but received a {type(self.data)}')
        return xmltodict.unparse(self.data)

    def from_xml(self):
        """Method to convert a String or File Processor of XML to a OrderedDict

        :rtype: OrderedDict
        :returns: YAML Data as a OrderedDict

        :raises TypeError: If data is not a String or fp(_io.TextIOWrapper)

        """
        if isinstance(self.data, str):
            return self.__from_xml_from_string()

        elif isinstance(self.data, _io.TextIOWrapper):
            return self.__from_xml_from_fp()

        raise TypeError(f'from_xml expected a string or _io.TextIOWrapper, but received a {self.data}')

    def __from_xml_from_string(self):
        """Private Method to deal with XML from a String

        :rtype: Dict
        :returns: XML Data as a OrderedDict

        :raises TypeError: If data is not a String

        """
        if not isinstance(self.data, str):  # pragma: no cover
            raise TypeError(f'__from_xml_from_string expected a string but received a {type(self.data)}')

        return xmltodict.parse(self.data)

    def __from_xml_from_fp(self):
        """Private Method to deal with XML from a fp(_io.TextIOWrapper)

        :rtype: Dict
        :returns: XML Data as a OrderedDict

        :raises TypeError: If data is not a fp(_io.TextIOWrapper)

        """
        if not isinstance(self.data, _io.TextIOWrapper):  # pragma: no cover
            raise TypeError(f'__from_xml_from_fp expected a _io.TextIOWrapper but received a {type(self.data)}')

        return xmltodict.parse(self.data.read())

    def to_yaml(self):
        """Method to convert a Dict to a String YAML

        :rtype: String
        :returns: YAML Data

        :raises TypeError: If data is not a Dict

        """
        if not isinstance(self.data, dict):
            raise TypeError(f'to_yaml expected a dict but received a {type(self.data)}')

        return yaml.safe_dump(self.data)

    def from_yaml(self):
        """Method to convert a String or File Processor of YAML to a Dict

        :rtype: Dict
        :returns: YAML Data as a Dict

        :raises TypeError: If data is not a String or fp(_io.TextIOWrapper)

        """
        if isinstance(self.data, str):
            return self.__from_yaml_from_string()

        elif isinstance(self.data, _io.TextIOWrapper):
            return self.__from_yaml_from_fp()

        raise TypeError(f'from_yaml expected a string or _io.TextIOWrapper, but received a {self.data}')

    def __from_yaml_from_string(self):
        """Private Method to deal with YAML from a String

        :rtype: Dict
        :returns: YAML Data as a Dict

        :raises TypeError: If data is not a String

        """
        if not isinstance(self.data, str):  # pragma: no cover
            raise TypeError(f'__from_yaml_from_string expected a string but received a {type(self.data)}')

        return yaml.safe_load(self.data)

    def __from_yaml_from_fp(self):
        """Private Method to deal with YAML from a fp(_io.TextIOWrapper)

        :rtype: Dict
        :returns: YAML Data as a Dict

        :raises TypeError: If data is not a fp(_io.TextIOWrapper)

        """
        if not isinstance(self.data, _io.TextIOWrapper):  # pragma: no cover
            raise TypeError(f'__from_yaml_from_fp expected a _io.TextIOWrapper but received a {type(self.data)}')

        return yaml.safe_load(self.data)

    def to_json(self):
        """Method to convert a Dict to a String JSON

        :rtype: String
        :returns: JSON Data

        :raises TypeError: If data is not a Dict

        """
        if not isinstance(self.data, dict):
            raise TypeError(f'to_json expected a dict but received a {type(self.data)}')

        return json.dumps(self.data)

    def from_json(self):
        """Method to convert a String or File Processor of JSON to a Dict

        :rtype: Dict
        :returns: JSON Data as a Dict

        :raises TypeError: If data is not a String or fp(_io.TextIOWrapper)

        """
        if isinstance(self.data, str):
            return self.__from_json_from_string()

        elif isinstance(self.data, _io.TextIOWrapper):
            return self.__from_json_from_fp()

        raise TypeError(f'from_json expected a string or _io.TextIOWrapper, but received a {self.data}')

    def __from_json_from_string(self):
        """Private Method to deal with JSON from a String

        :rtype: Dict
        :returns: JSON Data as a Dict

        :raises TypeError: If data is not a String

        """
        if not isinstance(self.data, str):  # pragma: no cover
            raise TypeError(f'__from_json_from_string expected a string but received a {type(self.data)}')

        return json.loads(self.data)

    def __from_json_from_fp(self):
        """Private Method to deal with JSON from a fp(_io.TextIOWrapper)

        :rtype: Dict
        :returns: JSON Data as a Dict

        :raises TypeError: If data is not a fp(_io.TextIOWrapper)

        """
        if not isinstance(self.data, _io.TextIOWrapper):  # pragma: no cover
            raise TypeError(f'__from_json_from_fp expected a _io.TextIOWrapper but received a {type(self.data)}')

        return json.load(self.data)
