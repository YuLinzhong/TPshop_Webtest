import json


def read_json(filename):
    with open(filename, 'r', encoding="utf-8") as f:
        return json.load(f)


if __name__ == '__main__':
    print(read_json('../data/login.json'))
    print(type(read_json('../data/login.json')))
