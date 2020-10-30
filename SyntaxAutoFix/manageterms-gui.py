#!/usr/bin/env python3
import os, signal, sys, glob
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow, QApplication, QErrorMessage, QShortcut
from PyQt5.QtGui import QKeySequence
from SyntaxAutoFix.utils import open_typo_file, save_typo_data
from SyntaxAutoFix.ui_manageterms import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        # Load the ui
        QMainWindow.__init__(self, parent)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # Connect the function with the signal
        self.ui.save.clicked.connect(self.store_new_argument)
        self.ui.save.clicked.connect(self.save_and_clear)
        self.ui.save_close.clicked.connect(self.save_close)
        # When the software are closed on console the software are closed
        signal.signal(signal.SIGINT, signal.SIG_DFL)
        self.script_path = os.path.dirname(os.path.realpath(__file__)) + '/words/'
        for filepath in sorted(glob.glob(os.path.join(self.script_path, '*.json'))):
            language = os.path.splitext(os.path.basename(filepath))[0]
            self.ui.languages.addItem(language)
        enter = QShortcut(QKeySequence(QtCore.Qt.Key_Return), self)
        enter.activated.connect(self.save_close)
        self.show()

    def store_new_argument(self):
        wrong = self.ui.wrong.text()
        right = self.ui.right.text()
        lang = self.ui.languages.currentText()
        # Check argument is not circular
        if right == wrong:
            msg = QErrorMessage(self)
            msg.setWindowModality(QtCore.Qt.WindowModal)
            msg.showMessage('You can’t replace a word with itself. It will create a loop.')

        lang_path = self.script_path + lang + '.json'
        typo_data = open_typo_file(lang_path)
        if right in typo_data:
            typo_data[right][typo_data.length].append(wrong)
        else:
            typo_data[right] = [wrong]
        save_typo_data(lang_path, typo_data)

    def save_close(self):
        self.store_new_argument()
        self.close()

    # Clear the text fields on save issue #39
    def save_and_clear(self):
        self.ui.wrong.clear()
        self.ui.right.clear()

def main():
    #Start the software
    app = QApplication(sys.argv)
    MainWindow_ = QMainWindow()
    ui = MainWindow()
    ui.setupUi(MainWindow_)
    #Add the close feature at the program with the X
    sys.exit(app.exec_())

#Execute the software
main()
