# SyntaxAlert
This script will track and automatically fix every word that you will type to the right words!  
An easy solution to fix typos!

Check the `words` folder for the languages available.

## Installation
```
pip3 install keyboard
pip3 install syntaxautofix
```
For the UI is required PyQt5.

## How to use with Target Language(s)
- For English only
```
syntaxautofix -words ./words/en.json
```

- For Italian/English/Spanish (or without parameters is the same):  
```
syntaxautofix -words ./words/en.json -words2 ./words/it.json
```

- Otherwise with the `configini` parameter you can specify a settings file (sample in the package/repo):  
```
syntaxautofix -configini /path/config.ini
```


## Adding New Terms

This require the git repo or the right path to the pip package folder.

```
manageterms.py -wrong="wdiget" -right="widget" -lang=en
```

You can use also an ui for that: `manageterms-gui.py`

## Adding New Terms using CSV File

This require the git repo or the right path to the pip package folder.

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
