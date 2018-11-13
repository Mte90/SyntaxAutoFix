#!/usr/bin/env python3
import argparse, os.path
from utils.data_handlers import open_typo_file, save_typo_data


def parse_argument(_parser_):
  _parser_.add_argument('-wrong', dest="wrong", type=str, required=True)
  _parser_.add_argument('-right', dest="right", type=str, required=True)
  _parser_.add_argument('-lang', dest="lang", type=str, required=True)
  args = _parser_.parse_args()
  return args
  
  
def store_new_argument(_args_):
  try:
    lang_path = script_path + '/words/' + _args_.lang + '.json'
    typo_data = open_typo_file(lang_path)
    typo_data[args.right].add(_args_.wrong)
    save_typo_data(lang_path, typo_data)
  except FileNotFoundError:
    raise ValueError('Language ' +  _args_.lang + ' actually not avalaible.')

# Parse argument
parser = argparse.ArgumentParser(description='add new terms!')
args = parse_argument(parser)

# Check argument is not circular
if args.right == args.wrong:
  raise ValueError('You can’t replace a word with itself. It will create a loop.')
else:  
  # Store argument
  script_path = os.path.dirname(os.path.realpath(__file__))
  store_new_argument(args)
  
