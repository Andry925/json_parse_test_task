import json
import os

VOICE_DICT = {"dog": "bark", "cat": "meow", "cow": "moo", "rat": "pipi", "alien": "KILL"}
INPUT_DIRECTORY = "../input_json_directory"


def read_json_file(file_name: str) -> dict:
    with open(file_name, encoding='utf-8') as json_file:
        file_data = json.load(json_file)
    return file_data


def extract_animal_voice(dict_data: dict) -> str | None:
    current_animal_name = dict_data.get('animal')
    if current_animal_name in VOICE_DICT:
        return VOICE_DICT.get(current_animal_name)
    return None


if __name__ == "__main__":

    for file in os.listdir(INPUT_DIRECTORY):
        converted_dict_data = read_json_file(f"{INPUT_DIRECTORY}/{file}")
        expected_voice = VOICE_DICT.get(converted_dict_data.get("animal"))
        assert extract_animal_voice(converted_dict_data) == expected_voice, \
            (f"There is a fail for  {file}: Expected {expected_voice}, "
             f"but got {extract_animal_voice(converted_dict_data)}")
