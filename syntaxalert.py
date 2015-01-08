#!/usr/bin/env python3
import contextlib, random
import subprocess, json
import argparse, os.path

parser = argparse.ArgumentParser(description='Scan your gitied letter for wrong word and alert you!')
parser.add_argument('-words', action="store", dest='words_file', required=True)
parser.add_argument('-alerts', action="store", dest='alerts_file', required=True)

args = parser.parse_args()

if os.path.isfile(args.words_file) == False:
    print('ERR: Words file not exist!')
    exit()

if os.path.isfile(args.alerts_file) == False:
    print('ERR: Alerts file not exist!')
    exit()

newlines = ['\n', '\r\n', '\r']
def unbuffered(proc, stream='stdout'):
    stream = getattr(proc, stream)
    with contextlib.closing(stream):
        while True:
            out = []
            last = stream.read(1)
            # Don't loop forever
            if last == '' and proc.poll() is not None:
                break
            while last not in newlines:
                # Don't loop forever
                if last == '' and proc.poll() is not None:
                    break
                out.append(last)
                last = stream.read(1)
            out = ''.join(out)
            yield out

def keyMap():
    p = subprocess.Popen(["xmodmap","-pke"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
    key = {}
    for line in unbuffered(p):
        line = line.replace('keycode','').strip().split()
        if len(line) > 2 and line[2] != None:
            key[line[0]] = line[2]
    return key

def getKey(char):
    if char.startswith("key release"):
        char = char.replace('key release','').strip()
        if str(keys[char]) != 'None':
            return keys[char]

def alert(word):
    if word != '':
        alert = random.choice(alerts)
        alert = alert.rstrip('\n')
        for (wrongs, correct) in words.items():
            for wrong in words[wrongs]:
                if wrong == word:
                    message = alert % ('<font color="red"><b>' + word + '</b></font>', '<font color="blue"><b>' + str(correct[0]) + '</b></font>')
                    subprocess.call(['kdialog','--sorry', message ])

def loadWord(filename):
    with open(filename) as json_file:
        words = json.load(json_file)
        return words

keys = keyMap()
f = open(args.alerts_file)
alerts = f.readlines()

words = loadWord(args.words_file)

word = ''
process = subprocess.Popen( ['xinput', 'test', '10'], stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)

for line in unbuffered(process):
    letter = getKey(line)
    if str(letter) != 'None' or letter != None:
        if letter == 'space' or letter == 'KP_Enter':
            alert(word)
            word = ''
        elif letter != 'F12':
            word += str(letter)
