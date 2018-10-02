#!/usr/bin/python3
import keyboard
import json
import argparse
import os.path

script_path = os.path.dirname(os.path.realpath(__file__))
# Load words
def loadWord(filename):
    with open(filename) as json_file:
        words = json.load(json_file)
        return words

# Parse argument
parser = argparse.ArgumentParser(description='Scan your digited letter for wrong words and alert you!')
parser.add_argument('-words', action="store", dest='words_file', nargs='?', default=script_path + '/words/en.json', type=str)
parser.add_argument('-words2', action="store", dest='words_file2', nargs='?', default=script_path + '/words/it.json', type=str)
args = parser.parse_args()

# Check the file and load it
if os.path.isfile(args.words_file) is False:
    print('ERR: Words file not exist!')
    exit()

if args.words_file2 is not None:
    if os.path.isfile(args.words_file2) is not False:
        words = loadWord(args.words_file)
        words2 = loadWord(args.words_file2)
        words.update(words2)
else:
    words = loadWord(args.words_file)

print(str(len(words)) + " words loaded")
for (correct, wrongs) in words.items():
    for wrong in wrongs:
        if wrong != '':
            print('Loaded ' + wrong + ' with as: ' + correct)
            keyboard.add_abbreviation(wrong, ' ' + correct + ' ')

keyboard.wait()
