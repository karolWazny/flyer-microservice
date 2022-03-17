from generator import Generator
from song import SongBook
from exsultate import *
import json
import sys
import os

def main():
    dir_path = os.path.dirname(os.path.realpath(__file__))
    log_filename = os.path.dirname(os.path.realpath(__file__)) + '/log.txt'
    # os.system("echo 'beginning' >> " + log_filename)
    json_string = sys.argv[1]
    filename = ''
    if(len(sys.argv) > 2 ):
        filename = sys.argv[2]
    generator = Generator()
    generator.load_configuration()
    dictionary = json.loads(json_string)
    # dictionary = read_json( dir_path + '/' + 'songbook2.json')
    songbook = SongBook.from_dict(dictionary)
    output = generator.generate(songbook, filename)
    print(output)

if __name__ == '__main__':
    main()