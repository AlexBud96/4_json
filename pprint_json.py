import json
import sys


def load_data(filepath):
    with open(filepath, 'r') as f:
        data = json.load(f)
    return data

def pretty_print_json(data):
    parsed = data
    print (json.dumps(parsed, indent=4, sort_keys=True))


if __name__ == '__main__':
    data = load_data(sys.argv[1])
    pretty_print_json(data)
