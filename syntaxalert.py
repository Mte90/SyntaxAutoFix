#!/usr/bin/env python3
import contextlib, random
import subprocess, json
import argparse, os.path, re

# Parse argument
parser = argparse.ArgumentParser(description='Scan your digited letter for wrong words and alert you!')
parser.add_argument('-words', action="store", dest='words_file', required=True)
parser.add_argument('-alerts', action="store", dest='alerts_file', required=True)
parser.add_argument('-xinput', action="store", dest='xinput', required=True)
parser.add_argument('-warning', action="store", dest='warnings_file')
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
        line = line.replace('keycode', '').strip().split()
        if len(line) > 2 and line[2] is not None:
            key[line[0]] = line[2]
    return key


# Check the last key
def getKey(char):
    if char.startswith("key release"):
        char = char.replace('key release', '').strip()
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
                    message = alert % ('<font color="red"><b>' + word + '</b></font>', '<font color="blue"><b>' + str(wrongs) + '</b></font>')
                    subprocess.Popen(['kdialog', '--sorry', message ])
                    subprocess.Popen(['play', '/usr/share/sounds/KDE-Sys-File-Open-Foes.ogg'])

# Load words
def loadWord(filename):
    with open(filename) as json_file:
        words = json.load(json_file)
        return words

# Autodetect xinput device
def idAutoDetect():
    return int(re.sub("[^0-9]", "",os.popen("xinput list | grep 'Keyboard' | head -n 1 | cut -d '=' -f 2 | cut -b 1-3").read()))


# Open a notify about a warning
def checkWarning(word):
    for (wrong, alert) in warning.items():
        if word == wrong:
            message = alert % (wrong)
            subprocess.Popen(['notify-send', message ])
            subprocess.Popen(['play', '/usr/share/sounds/KDE-Sys-Warning.ogg'])

keys = keyMap()

# Check the file and load it
if os.path.isfile(args.words_file) is False:
    print('ERR: Words file not exist!')
    exit()

if os.path.isfile(args.alerts_file) is False:
    print('ERR: Alerts file not exist!')
    exit()

if args.xinput == 'auto':
    args.xinput = str(idAutoDetect())

if args.alerts_file2 is not None:
    if os.path.isfile(args.alerts_file2) is not False:
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

if args.words_file2 is not None:
    if os.path.isfile(args.words_file2) is not False:
        words = loadWord(args.words_file)
        words2 = loadWord(args.words_file2)
        words.update(words2)
    else:
        print('ERR: Alerts 2 file not exist!')
else:
    words = loadWord(args.words_file)

# Load warning word
warnings = []
warning = {}
if args.warnings_file is not None:
    if os.path.isfile(args.warnings_file) is not False:
        f = open(args.warnings_file)
        warnings = f.readlines()
        for warningsplit in warnings:
            warningsplit = warningsplit.split('|\|')
            warning[warningsplit[0]] = warningsplit[1]
    else:
        print('ERR: Warning file not exist!')

word = ''
process = subprocess.Popen( ['xinput', 'test', args.xinput], stdout=subprocess.PIPE, stderr=subprocess.PIPE,universal_newlines=True)

# Check if space or enter for split the word
for line in unbuffered(process):
    letter = getKey(line)
    if str(letter) != 'None' or letter is not None:
        if letter == 'space' or letter == 'KP_Enter' or letter == 'Return':
            alert(word)
            word = ''
        # Remove last char
        elif letter == 'BackSpace':
            letter = letter[:-1]
        # This key create problem in the keylogger so reset the word
        elif letter == 'Home' or letter == '~Prior' or letter == '~Next' or letter == 'Left' or letter == 'Right' or letter == 'Up' or letter == 'Down' or letter == 'Delete' or letter == 'End':
            word = ''
        # Ignore the functional key and append the letter
        elif len(letter) == 1:
            word += str(letter)
            checkWarning(word)
