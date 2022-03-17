import json

def read_json(filename):
    with open(filename) as file:
        return json.load(file)

def write_json(dictionary, filename):
    with open(filename, 'w') as outfile:
        json.dump(dictionary, outfile)

def main():
    print(read_json('naszbog.json'))

if __name__ == '__main__':
    main()