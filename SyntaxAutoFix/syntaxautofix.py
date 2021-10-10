#!/usr/bin/python3
import logging
import keyboard
import argparse
import os.path
from threading import Thread
from time import sleep
from SyntaxAutoFix.utils import open_typo_file
from SyntaxAutoFix.utils import save_stats_file

from configparser import ConfigParser
import json


logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(name)s %(levelname)-8s %(thread)d %(message)s",
    datefmt="%Y-%m-%d %H:%M:%S")
logger = logging.getLogger("SyntaxAutoFix")
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

try:
    config_parser = ConfigParser()
    config_parser.read(args.configini)
    LIST_OF_FILES = json.loads(config_parser.get('DEFAULT', 'words_file'))
    if args.words_file != LIST_OF_FILES[0]:
        args.words_file = LIST_OF_FILES[0]
    if args.words_file2 != LIST_OF_FILES[1]:
        args.words_file2 = LIST_OF_FILES[1]
except:
    logger.error("Config empty")

# it holds the files name passed and the stat os file
files = {}


def get_wrong_word(recorded_words_list):
    if len(recorded_words_list) > 0:
        list_splitted = recorded_words_list[0].split() #Get first element of the list
        if len(list_splitted) > 0:
            wrong_word = list_splitted[-1]
            return wrong_word
    return None


def mispell_callback():
    recorded_words = keyboard.stop_recording()
    recorded_words_list = list(keyboard.get_typed_strings(recorded_words))
    logger.info(f"Captured list of words: {recorded_words_list}")
    wrong_word = get_wrong_word(recorded_words_list)
    if wrong_word:
        logger.info(f"Word '{wrong_word}' detected and tracked")
        save_stats_file(os.path.join(getHomePath(), "stats.json"), wrong_word, 1)
    keyboard.start_recording()


def loadJSON():
    # Check the file and load it
    if not os.path.isfile(args.words_file):
        logger.error(f"Words file {args.words_file} not exist!")
        exit()

    if args.words_file2:
        if os.path.isfile(args.words_file2):
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

    logger.info(f"{str(len(words))} words loaded")
    for (correct_word, misspelled_words) in words.items():
        for misspelled_word in misspelled_words:
            if misspelled_word:
                keyboard.add_abbreviation(misspelled_word, ' ' + correct_word + ' ')
                keyboard.add_word_listener(misspelled_word, mispell_callback)


# Clean the abbreviations from previous JSON and reloads new JSON
def reload_JSON():
    logger.info("Reloading modified JSON!")
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
