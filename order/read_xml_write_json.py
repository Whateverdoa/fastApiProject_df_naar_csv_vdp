# lees xmlf# vertaal xml naar json, lees xml
import requests
import json
from pathlib import Path
import xmltodict
import pandas as pd
# STEP : Read the xml file here,
# “data_dict” is the variable in which we have loaded our XML data after converting it to dictionary datatype.

# look into named tuples for this

xml_file = Path('..\order\data_xml\Basis_xml_DRUKWERKDEAL.NL_itemnumber_569621071082_202311942_F6HADBE637_MA267C0B9G.xml')



def xml_in_json_out(xml_file_path):
    with open(xml_file_path) as the_xml_file:
        data_dict = xmltodict.parse(the_xml_file.read())
        json_data = json.dumps(data_dict)
    return json_data


def ready_for_mapping_(json_data):
    json_data_as_dict = json.loads(json_data)
    return json_data_as_dict

def main():
    ...

if __name__ == '__main__':
    main()

    vila_json = ready_for_mapping_(xml_in_json_out(xml_file))

    klantnaam = vila_json['CreateJob']['Customer']['CustomerName']

    # if klantnaam == "DRUKWERKDEAL.NL":
    #     #functie voor extracting data from drukwerk deal order uit vila xml.
    #     vilaordernummer= vila_json['CreateJob']['Job']['OrderId']
    #     itemnummer = vila_json['CreateJob']['EskoProducts']['EskoProduct']['ProductNo']
    #
    #     mes=vila_json['CreateJob']
    #     etiket_y=vila_json['CreateJob']
    #
    #     hoogte=vila_json['CreateJob']
    #     breedte=
    #     gutter_across_x=
    #     gutteralong_y=
    #
    #     totaal_aantal_order=vila_json['CreateJob']
    #     aantal_per_rol=
    #     kern_diameter=
    #     afhandeling=
    #     qorder=








