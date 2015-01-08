#!/usr/bin/env python3
import contextlib, random
import subprocess, json
import argparse, os.path

# Parse argument
parser = argparse.ArgumentParser(description='Scan your digited letter for wrong words and alert you!')
parser.add_argument('-words', action="store", dest='words_file', required=True)
parser.add_argument('-alerts', action="store", dest='alerts_file', required=True)
parser.add_argument('-xinput', action="store", dest='xinput', required=True)
parser.add_argument('-words2', action="store", dest='words_file2')
parser.add_argument('-alerts2', action="store", dest='alerts_file2')
args = parser.parse_args()

# Clean output from the shell
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

# Load the keycode from the keyboard
def keyMap():
    p = subprocess.Popen(["xmodmap","-pke"], stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)
    key = {}
    for line in unbuffered(p):
        line = line.replace('keycode','').strip().split()
        if len(line) > 2 and line[2] != None:
            key[line[0]] = line[2]
    return key

# Check the last key
def getKey(char):
    if char.startswith("key release"):
        char = char.replace('key release','').strip()
        if str(keys[char]) != 'None':
            if str(keys[char]) == 'apostrophe':
                keys[char] = "'"
            elif str(keys[char]) == 'ograve':
                keys[char] = "ò"
            elif str(keys[char]) == 'egrave':
                keys[char] = "è"
            elif str(keys[char]) == 'agrave':
                keys[char] = "à"
            elif str(keys[char]) == 'igrave':
                keys[char] = "ì"
            return keys[char]

# Alert the user about the wrong word
def alert(word):
    if word != '':
        alert = random.choice(alerts)
        alert = alert.rstrip('\n')
        for (wrongs, correct) in words.items():
            for wrong in words[wrongs]:
                if wrong == word:
                    message = alert % ('<font color="red"><b>' + word + '</b></font>', '<font color="blue"><b>' + str(correct[0]) + '</b></font>')
                    subprocess.call(['kdialog','--sorry', message ])

# Load words
def loadWord(filename):
    with open(filename) as json_file:
        words = json.load(json_file)
        return words

keys = keyMap()

# Check the file and load it
if os.path.isfile(args.words_file) == False:
    print('ERR: Words file not exist!')
    exit()

if os.path.isfile(args.alerts_file) == False:
    print('ERR: Alerts file not exist!')
    exit()

if args.alerts_file2 != None:
    if os.path.isfile(args.alerts_file2) != False:
        f = open(args.alerts_file)
        alerts = f.readlines()
        f = open(args.alerts_file2)
        alerts2 = f.readlines()
        alerts = alerts + alerts2
    else:
        print('ERR: Alerts 2 file not exist!')
else:
    f = open(args.alerts_file)
    alerts = f.readlines()

if args.words_file2 != None:
    if os.path.isfile(args.words_file2) != False:
        words = loadWord(args.words_file)
        words2 = loadWord(args.words_file2)
        words.update(words2)
    else:
        print('ERR: Alerts 2 file not exist!')
else:
    words = loadWord(args.words_file)

word = ''
process = subprocess.Popen( ['xinput', 'test', args.xinput], stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)

# Check if space or enter for split the word
for line in unbuffered(process):
    letter = getKey(line)
    if str(letter) != 'None' or letter != None:
        if letter == 'space' or letter == 'KP_Enter' or letter == 'Return':
            alert(word)
            word = ''
        # Ignore the functional key and append the letter
        elif len(letter) == 1:
            word += str(letter)
