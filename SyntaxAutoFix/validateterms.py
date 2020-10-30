#!/usr/bin/env python3
import argparse, os.path
from SyntaxAutoFix.utils import open_typo_file


def parse_argument(_parser_):
    _parser_.add_argument('-lang', dest="lang", type=str, required=True)
    args = _parser_.parse_args()
    return args


def load_language(_args_):
    try:
        lang_path = script_path + '/words/' + _args_.lang + '.json'
        words = open_typo_file(lang_path)
        return words
    except FileNotFoundError:
        raise ValueError('Language ' + _args_.lang + ' actually not avalaible.')


def term_is_typo_of_another_word(term, words):
    for (correct, wrongs) in words.items():
        if correct == term:
            print('ERR 1: The term ' + correct + ' is a typo of ' + term + '.')
        for wrong in wrongs:
            if wrong == '':
                print('ERR 3: The term ' + correct + ' has an empty typo.')


# Parse argument
parser = argparse.ArgumentParser(description='validate terms!')
args = parse_argument(parser)

# Store argument
script_path = os.path.dirname(os.path.realpath(__file__))
words = load_language(args)
for (correct, wrongs) in words.items():
    for wrong in wrongs:
        if wrong == correct:
            print('ERR 2: The term ' + correct + ' his a typo of itself.')
            continue
        if wrong != '':
            term_is_typo_of_another_word(wrong, words)
