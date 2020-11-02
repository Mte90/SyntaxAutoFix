#!/usr/bin/env python3
import argparse
import os.path
import csv
from SyntaxAutoFix.utils import open_typo_file, save_typo_data

# Parse argument
parser = argparse.ArgumentParser(description='add new terms!')

parser.add_argument('-file', dest="file", type=str, required=True)
parser.add_argument('-lang', dest="lang", type=str, required=True)
args = parser.parse_args()

script_path = os.path.dirname(os.path.realpath(__file__))
script_path = os.path.join(script_path, 'SyntaxAutoFix/words/' + args.lang + '.json')

typo_data = open_typo_file(script_path)
with open(args.file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
        typo_data[row[0]].add(row[1])

save_typo_data(script_path, typo_data)
