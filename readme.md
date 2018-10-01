# SyntaxAlert
This script will track and automatically fix every word that you will digit to right words!  
An easy solution to fix typos!
###### latest readme update : 30 Sept 2018
<br>

## Required Installation
```
pip3 install keyboard
```
<br>

## How to use with Target Language(s)
- For English only
```
syntaxalert.py -words ./words/en.json
```

- For Italian and English (or without parameters is the same):  
```
syntaxalert.py -words ./words/en.json -words2 ./words/it.json
```
<br>
  
## Adding New Terms
```
manageterms.py -wrong="wdiget" -right="widget" -lang=en
```

