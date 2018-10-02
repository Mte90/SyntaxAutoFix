#!/usr/bin/env python3
import argparse
import os.path
import json

import observer

# Parse argument
parser = argparse.ArgumentParser(description='add new terms!')

parser.add_argument('-wrong', dest="wrong", type=str, required=True)
parser.add_argument('-right', dest="right", type=str, required=True)
parser.add_argument('-lang', dest="lang", type=str, required=True)
args = parser.parse_args()

script_path = os.path.dirname(os.path.realpath(__file__)) + '/words/' + args.lang + '.json'

filepath = open(script_path, 'r')
data = json.load(filepath)
if args.right in data:
    if args.wrong not in data[args.right]:
        data[args.right].append(args.wrong)
else:
    data[args.right] = [args.wrong]
filepath = open(script_path, 'w')
filepath.write(json.dumps(data, indent=4, sort_keys=True))
filepath.close()

subject = observer.Subject()
subject.attach(observer.Observer(args.lang))
subject.set_data("%s updated" % args.lang)
