# SyntaxAlert
This script will track and automatically fix every word that you will type to right words!  
An easy solution to fix typos!

Check the `words` folder`for the languages available.

## Required Installation
```
pip3 install keyboard
```

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

## Adding New Terms using CSV File
Directly upload new terms using a CSV file with row format:
```
<wrong-term>, <correct-term>
```

For example:
Let `new_words.csv` be
```
aries,Aries
Celsius,Celcius
```

Then use the command:
```
csvtoterms.py -file new_words.csv -lang en
```