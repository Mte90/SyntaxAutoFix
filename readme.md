# SyntaxAlert

This script will track every words that you will digit and fix automatically with the right words!  
An easy way to fix typos!

# Require 

`pip3 install keyboard`

# How to use

Only En words:  

`syntaxalert.py -words ./words/en.json`

En and It words (or without parameters is the same):  

`syntaxalert.py -words ./words/en.json -words2 ./words/it.json`

## Add new terms

`manageterms.py -wrong="wdiget" -right="widget" -lang=en`
