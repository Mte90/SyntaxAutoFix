# SyntaxAlert
Automatically fix every typo that you will type to the right words!  

It uses a database that can be extended.

Check the `words` folder for the languages available.

## Installation
```
pip3 install keyboard
pip3 install syntaxautofix
```
For the UI is required PyQt5.

Doesn't create conflicts with [Espanso](https://espanso.org/).

### Settings and assets files (dictionaries)

Automatically will create a folder inside '~/.config/SyntaxAutoFix` that will include the stats.json files.  
Also will look for the dictionaries and settings also on this folder so this let you customize it without define commandline parameters.

## Usage

### How to use with Target Language(s)

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

### Adding New Terms

This require the git repo or the right path to the pip package folder.

```
manageterms.py -wrong="wdiget" -right="widget" -lang=en
```

You can use also an ui for that: `manageterms-gui.py`

### Adding New Terms using a CSV File

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
