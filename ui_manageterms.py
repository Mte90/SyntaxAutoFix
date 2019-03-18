# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'manageterms.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(220, 158)
        MainWindow.setMinimumSize(QtCore.QSize(200, 0))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayout = QtWidgets.QGridLayout()
        self.gridLayout.setObjectName("gridLayout")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.gridLayout.addWidget(self.label_2, 1, 0, 1, 1)
        self.wrong = QtWidgets.QLineEdit(self.centralwidget)
        self.wrong.setObjectName("wrong")
        self.gridLayout.addWidget(self.wrong, 0, 1, 1, 1)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.right = QtWidgets.QLineEdit(self.centralwidget)
        self.right.setObjectName("right")
        self.gridLayout.addWidget(self.right, 1, 1, 1, 1)
        self.save = QtWidgets.QPushButton(self.centralwidget)
        self.save.setObjectName("save")
        self.gridLayout.addWidget(self.save, 3, 0, 1, 1)
        self.languages = QtWidgets.QComboBox(self.centralwidget)
        self.languages.setObjectName("languages")
        self.gridLayout.addWidget(self.languages, 2, 1, 1, 1)
        self.save_close = QtWidgets.QPushButton(self.centralwidget)
        self.save_close.setObjectName("save_close")
        self.gridLayout.addWidget(self.save_close, 3, 1, 1, 1)
        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Add Terms"))
        self.label_2.setText(_translate("MainWindow", "Right Term"))
        self.label.setText(_translate("MainWindow", "Wrong Term"))
        self.label_3.setText(_translate("MainWindow", "Language"))
        self.save.setText(_translate("MainWindow", "Save"))
        self.save_close.setText(_translate("MainWindow", "Save and Close"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

