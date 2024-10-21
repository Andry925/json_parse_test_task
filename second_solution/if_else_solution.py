import json

INPUT_DIRECTORY = "../input_json_directory"


def read_json_file(file_name: str) -> dict:
    with open(file_name, encoding='utf-8') as json_file:
        file_data = json.load(json_file)
    return file_data


def extract_animal_voice(dict_data: dict) -> str | None:
    animal_name = dict_data.get("animal")
    if animal_name == "dog":
        return "bark"
    elif animal_name == "cat":
        return "meow"
    elif animal_name == "cow":
        return "moo"
    elif animal_name == "rat":
        return "pipi"
    elif animal_name == "alien":
        return "Kill"
    return None


if __name__ == '__main__':
    converted_dict_data = read_json_file(f"{INPUT_DIRECTORY}/test_unknown_animal.json")
    animal_voice = extract_animal_voice(converted_dict_data)
    print(animal_voice)
