#!/usr/bin/env python3
import argparse
import os.path
import json
import csv

# Parse argument
parser = argparse.ArgumentParser(description='add new terms!')

parser.add_argument('-file', dest="file", type=str, required=True)
parser.add_argument('-lang', dest="lang", type=str, required=True)
args = parser.parse_args()

script_path = os.path.dirname(os.path.realpath(__file__)) + '/words/' + args.lang + '.json'

filepath = open(script_path, 'r')
data = json.load(filepath)
with open(args.file) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if row[0] in data:
            data[row[1]].append(row[0])
        else:
            data[row[1]] = [row[0]]

filepath = open(script_path, 'w')
filepath.write(json.dumps(data, indent=4, sort_keys=True))
filepath.close()
