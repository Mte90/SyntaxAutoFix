#SyntaxAlert

Scan **all** your digited letter for wrong words and alert you!  
Is a nice keylogger that not save data!  

!["Screenshot"](screen.png)

#Require

* xinput
* kdialog

#How to use

Check with `xinput list` your keyboard number for use it  

Only En words:  

```syntaxalert.py -words ./words/en.json -alerts ./alerts/en.txt -xinput 10``` 

En and It words:  

```syntaxalert.py -words ./words/en.json -alerts ./alerts/en.txt -words2 ./words/it.json -alerts2 ./alerts/it.txt -xinput 10```