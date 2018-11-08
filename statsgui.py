#!/usr/bin/python3

import sys
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from utils.data_handlers import open_stats_file

class MyTable(QTableWidget):
    def __init__(self, data, *args):
        QTableWidget.__init__(self, *args)
        self.data = data
        self.setmydata()
        self.resizeColumnsToContents()
        self.resizeRowsToContents()

    def setmydata(self):
        horHeaders = []
        for n, key in enumerate(sorted(self.data.keys())):
            horHeaders.append(key)
            for m, item in enumerate(self.data[key]):
                newitem = QTableWidgetItem(item)
                newitem.setFlags(Qt.ItemFlags(~Qt.ItemIsEnabled))
                self.setItem(m, n, newitem)
        self.setHorizontalHeaderLabels(horHeaders)

def main(args):
    app = QApplication(args)
    stats_data = open_stats_file("stats.json")
    items = stats_data.items()
    words,counters = ('','')
    if len(items) > 0:
        items = sorted(items, key=lambda item: item[1], reverse=True)
        words,counters =  [list(item) for item in zip(*items)]
        counters = map(lambda x: str(x), counters)
    result = {'wrong_word' : words, 'counter': counters}
    table = MyTable(result, len(words), 2)
    table.show()
    sys.exit(app.exec_())

if __name__=="__main__":
    main(sys.argv)
