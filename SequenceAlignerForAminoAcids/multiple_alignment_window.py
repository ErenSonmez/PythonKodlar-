# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'multiple_alignment_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

import sys
from PyQt5 import QtCore, QtGui, QtWidgets
import multiple_alignment as ma

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900,500)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
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
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.seq2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.seq2_input.setObjectName("seq2_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.seq2_input)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.kval_input = QtWidgets.QSpinBox(self.centralwidget)
        self.kval_input.setMinimum(1)
        self.kval_input.setObjectName("kval_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.kval_input)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setObjectName("pushButton")
        self.pushButton.clicked.connect(self.run_aligner)
        self.horizontalLayout.addWidget(self.pushButton)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.score_matrix_table = QtWidgets.QTableView(self.centralwidget)
        self.score_matrix_table.setObjectName("score_matrix_table")
        self.gridLayout.addWidget(self.score_matrix_table, 1, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.seq1_input.setText('EQLLKALEFKL')
        self.seq2_input.setText('KVLEFGY')

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Multiple Alignment - Greedy Approach"))
        self.label.setText(_translate("MainWindow", "Sequence 1"))
        self.label_2.setText(_translate("MainWindow", "Sequence 2"))
        self.label_3.setText(_translate("MainWindow", "k value"))
        self.pushButton.setText(_translate("MainWindow", "    Find Multiple Alignment    "))

    def run_aligner(self):
        aligner=ma.multiple_aligner(str(self.seq1_input.text()),str(self.seq2_input.text()),int(self.kval_input.text()))
        score_matrix,matches,hm_score,hm_cells=aligner.run()
        
        model=ma.table_model(score_matrix,matches,hm_cells)
        self.score_matrix_table.setModel(model)
        #Tablo cell'lerinin boyutunu küçültmek için
        header=self.score_matrix_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)        
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

