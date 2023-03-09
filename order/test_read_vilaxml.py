from pathlib import Path

from .read_xml_write_json import xml_in_json_out

xml_file = Path('..\order\data_xml\Basis_xml_DRUKWERKDEAL.NL_itemnumber_569621071082_202311942_F6HADBE637_MA267C0B9G'
                '.xml')


def test_xml_in_json_out():
    if xml_file.is_file():

        test = type(xml_in_json_out(xml_file))
        result = type("")
        assert test == result
