# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'global_alignment_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import global_alignment as ga

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(533, 223)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.score_output = QtWidgets.QLineEdit(self.centralwidget)
        self.score_output.setObjectName("score_output")
        self.score_output.setReadOnly(True)
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.score_output)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.gridLayout.addLayout(self.formLayout_2, 5, 0, 1, 1)
        self.seq1_output = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.seq1_output.setFont(font)
        self.seq1_output.setReadOnly(True)
        self.seq1_output.setObjectName("seq1_output")
        self.gridLayout.addWidget(self.seq1_output, 3, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.gridLayout.addItem(spacerItem, 1, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.gridLayout.addWidget(self.label_3, 2, 0, 1, 1)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.formLayout = QtWidgets.QFormLayout()
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.seq1_input = QtWidgets.QLineEdit(self.centralwidget)
        self.seq1_input.setObjectName("seq1_input")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.seq1_input)
        self.seq2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.seq2_input.setObjectName("seq2_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.seq2_input)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.run_aligner)
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.seq2_output = QtWidgets.QLineEdit(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        font.setBold(True)
        font.setWeight(75)
        self.seq2_output.setFont(font)
        self.seq2_output.setReadOnly(True)
        self.seq2_output.setObjectName("seq2_output")
        self.gridLayout.addWidget(self.seq2_output, 4, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.seq1_input.setText('EQLLKALEFKL')
        self.seq2_input.setText('KVLEFGY')

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Global Alignment"))
        self.label_4.setText(_translate("MainWindow", "Score : "))
        self.seq1_output.setText(_translate("MainWindow", "Sequence 1 output"))
        self.label_3.setText(_translate("MainWindow", "Results:"))
        self.label.setText(_translate("MainWindow", "Sequence 1"))
        self.label_2.setText(_translate("MainWindow", "Sequence 2"))
        self.pushButton.setText(_translate("MainWindow", "    Find Global Alignment    "))
        self.seq2_output.setText(_translate("MainWindow", "Sequence 2 output"))

    def run_aligner(self):
        aligner=ga.global_aligner(str(self.seq1_input.text()), str(self.seq2_input.text()))
        s1,s2,score=aligner.run()
        self.seq1_output.setText(s1)
        self.seq2_output.setText(s2)
        self.score_output.setText(str(score))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

