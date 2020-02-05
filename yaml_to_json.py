from os import listdir
from os.path import isfile, join

import yaml
import json

yaml_directory = "./schemas/"
json_directory = "./generated/json/"


def main():
    print("Converting from YAML to JSON")
    yaml_files = [f for f in listdir(yaml_directory) if isfile(join(yaml_directory, f))]
    for file_name in yaml_files:
        json_file_name = file_name.replace(".yaml", ".json")
        with open(join(yaml_directory, file_name), 'r') as yaml_in, \
                open(join(json_directory, json_file_name), 'w') as json_out:
            print("Converting file " + file_name)
            yaml_object = yaml.safe_load(yaml_in)
            json_string = json.dumps(yaml_object).replace(".yaml", ".json")
            json_object = json.loads(json_string)
            json.dump(json_object, json_out, indent=2)
            print(yaml_object)


main()
