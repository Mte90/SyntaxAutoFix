#!/usr/bin/python3
import keyboard
import argparse
import os.path
from threading import Thread
from time import sleep
from SyntaxAutoFix.utils import open_typo_file
from SyntaxAutoFix.utils import save_stats_file

from configparser import ConfigParser
import json

script_path = os.path.dirname(os.path.realpath(__file__))
def getHomePath():
    user = os.getenv("SUDO_USER") or os.getenv("USER")
    home = os.path.join(os.path.expanduser('~' + user), '.config/SyntaxAutoFix')
    if not os.path.exists(home):
        os.mkdir(home)
    return home

def getAssetPath(path):
    home = getHomePath()
    complete_path = os.path.join(home, path)
    if not os.path.exists(complete_path):
        complete_path = os.path.join(script_path, path)
    return complete_path

config_parser = ConfigParser()

# Load words
def loadWord(filename):
    with open(filename) as json_file:
        words = open_typo_file(json_file)
        return words


# Parse argument
parser = argparse.ArgumentParser(description='Scan your digited letter for wrong words and alert you!')
parser.add_argument('-config', dest='configini', nargs='?', default=getAssetPath('config.ini'), type=str)
parser.add_argument('-words', dest='words_file', nargs='?', default=getAssetPath('words/en.json'), type=str)
parser.add_argument('-words2', dest='words_file2', nargs='?', default=getAssetPath('words/it.json'), type=str)
args = parser.parse_args()

config_parser.read(args.configini)
LIST_OF_FILES = json.loads(config_parser.get('DEFAULT', 'words_file'))
WORDS_FILE_DEFAULT_LOCATION = [getAssetPath(file_path) for file_path in LIST_OF_FILES]

# it holds the files name passed and the stat os file
files = {}


def mispell_callback():
    recorded_words = keyboard.stop_recording()
    recorded_words_list = list(keyboard.get_typed_strings(recorded_words))
    if len(recorded_words_list) > 0:
        list_splitted = recorded_words_list[0].split()
        if len(list_splitted) > 0:
            wrong_word = list_splitted[-1]
            print("Word '" + wrong_word + "' detected and tracked")
            save_stats_file(os.path.join(getHomePath(), "stats.json"), wrong_word, 1)
    keyboard.start_recording()


def loadJSON():
    # Check the file and load it
    if os.path.isfile(args.words_file) is False:
        print('ERR: Words file not exist!')
        exit()

    if args.words_file2 is not None:
        if os.path.isfile(args.words_file2) is not False:
            words = open_typo_file(args.words_file)
            words2 = open_typo_file(args.words_file2)
            words.update(words2)
            # register the status of file in these moment
            files[args.words_file] = os.stat(args.words_file)
            files[args.words_file2] = os.stat(args.words_file2)
    else:
        words = open_typo_file(args.words_file)
        # register the status of file in these moment
        files[args.words_file] = os.stat(args.words_file)

    print(str(len(words)) + " words loaded")
    for (correct, wrongs) in words.items():
        for wrong in wrongs:
            if wrong != '':
                keyboard.add_abbreviation(wrong, ' ' + correct + ' ')
                keyboard.add_word_listener(wrong, mispell_callback)


# Clean the abbreviations from previous JSON and reloads new JSON
def reload_JSON():
    print("Reloading modified JSON!")
    keyboard.unhook_all()
    loadJSON()


def JSON_modify_watcher():
    while True:
        sleep(3)
        for k in files:
            if files[k] != os.stat(k):
                reload_JSON()
                break


def main():
    keyboard.start_recording()

    loadJSON()
    t_watcher = Thread(target=JSON_modify_watcher)
    t_watcher.start()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        keyboard.stop_recording()
