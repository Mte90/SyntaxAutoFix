# SyntaxAlert
This script will track and automatically fix every word that you will type to the right words!  
An easy solution to fix typos!

Check the `words` folder for the languages available.

## Required Installation
```
pip3 install keyboard
```
For the UI is required PyQt5.

## How to use with Target Language(s)
- For English only
```
syntaxalert.py -words ./words/en.json
```

- For Italian/English/Spanish (or without parameters is the same):  
```
syntaxalert.py -words ./words/en.json -words2 ./words/it.json
```
<br>
  
## Adding New Terms
```
manageterms.py -wrong="wdiget" -right="widget" -lang=en
```

You can use also an ui for that: `manageterms-gui.py`

## Adding New Terms using CSV File
Directly upload new terms using a CSV file with row format:
```
<correct-term>, <wrong-term>
```

For example:
Let `new_words.csv` be
```
Africa,Afica
America,Ameria
```

Then use the command:
```
csvtoterms.py -file new_words.csv -lang en
```
