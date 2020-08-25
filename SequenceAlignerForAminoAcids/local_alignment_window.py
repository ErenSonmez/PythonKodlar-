# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'local_alignment_window.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!
import pandas as pd
import local_alignment as la
from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(900, 700)
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
        self.seq2_input = QtWidgets.QLineEdit(self.centralwidget)
        self.seq2_input.setObjectName("seq2_input")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.seq2_input)
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setObjectName("label_5")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.LabelRole, self.label_5)
        self.match_score_input = QtWidgets.QSpinBox(self.centralwidget)
        self.match_score_input.setMinimum(-99)
        self.match_score_input.setProperty("value", 4)
        self.match_score_input.setObjectName("match_score_input")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.match_score_input)
        self.mismatch_score_input = QtWidgets.QSpinBox(self.centralwidget)
        self.mismatch_score_input.setMinimum(-99)
        self.mismatch_score_input.setProperty("value", -2)
        self.mismatch_score_input.setObjectName("mismatch_score_input")
        self.formLayout.setWidget(3, QtWidgets.QFormLayout.FieldRole, self.mismatch_score_input)
        self.gap_score_input = QtWidgets.QSpinBox(self.centralwidget)
        self.gap_score_input.setMinimum(-99)
        self.gap_score_input.setProperty("value", -1)
        self.gap_score_input.setObjectName("gap_score_input")
        self.formLayout.setWidget(4, QtWidgets.QFormLayout.FieldRole, self.gap_score_input)
        self.horizontalLayout.addLayout(self.formLayout)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.find_alignment_btn = QtWidgets.QPushButton(self.centralwidget)
        self.find_alignment_btn.setObjectName("find_alignment_btn")
        self.find_alignment_btn.clicked.connect(self.run_aligner)
        self.horizontalLayout.addWidget(self.find_alignment_btn)
        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)
        self.score_matrix_table = QtWidgets.QTableView(self.centralwidget)
        self.score_matrix_table.setObjectName("score_matrix_table")
        self.gridLayout.addWidget(self.score_matrix_table, 1, 0, 1, 1)
        self.results_frame = QtWidgets.QFrame(self.centralwidget)
        self.results_frame.setObjectName("results_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.results_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.formLayout_2 = QtWidgets.QFormLayout()
        self.formLayout_2.setObjectName("formLayout_2")
        self.label_6 = QtWidgets.QLabel(self.results_frame)
        self.label_6.setObjectName("label_6")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_6)
        self.possible_alignment_count = QtWidgets.QLineEdit(self.results_frame)
        self.possible_alignment_count.setObjectName("possible_alignment_count")
        self.formLayout_2.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.possible_alignment_count)
        self.label_7 = QtWidgets.QLabel(self.results_frame)
        self.label_7.setObjectName("label_7")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_7)
        self.alignment_no = QtWidgets.QLineEdit(self.results_frame)
        self.alignment_no.setObjectName("alignment_no")
        self.formLayout_2.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.alignment_no)
        self.horizontalLayout_2.addLayout(self.formLayout_2)
        self.formLayout_3 = QtWidgets.QFormLayout()
        self.formLayout_3.setObjectName("formLayout_3")
        self.label_8 = QtWidgets.QLabel(self.results_frame)
        self.label_8.setObjectName("label_8")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label_8)
        self.seq1_output = QtWidgets.QLineEdit(self.results_frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(True)
        font.setWeight(75)
        self.seq1_output.setFont(font)
        self.seq1_output.setObjectName("seq1_output")
        self.formLayout_3.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.seq1_output)
        self.label_9 = QtWidgets.QLabel(self.results_frame)
        self.label_9.setObjectName("label_9")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_9)
        self.seq2_output = QtWidgets.QLineEdit(self.results_frame)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setBold(True)
        font.setWeight(75)
        self.seq2_output.setFont(font)
        self.seq2_output.setObjectName("seq2_output")
        self.formLayout_3.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.seq2_output)
        self.horizontalLayout_2.addLayout(self.formLayout_3)
        self.verticalLayout.addLayout(self.horizontalLayout_2)
        self.next_alignment_btn = QtWidgets.QPushButton(self.results_frame)
        self.next_alignment_btn.setObjectName("next_alignment_btn")
        self.next_alignment_btn.clicked.connect(self.next_path)
        self.verticalLayout.addWidget(self.next_alignment_btn)
        self.gridLayout.addWidget(self.results_frame, 2, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.seq1_input, self.seq2_input)
        MainWindow.setTabOrder(self.seq2_input, self.match_score_input)
        MainWindow.setTabOrder(self.match_score_input, self.mismatch_score_input)
        MainWindow.setTabOrder(self.mismatch_score_input, self.gap_score_input)
        MainWindow.setTabOrder(self.gap_score_input, self.find_alignment_btn)
        #Diğer buton değişkeninde kullanacağım değişkenler. run_aligner'da değer alıyorlar.
        self.paths=None 
        self.print_texts=None
        self.score_matrix=None
        
        self.results_frame.hide()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Local Alignment"))
        self.label.setText(_translate("MainWindow", "Sequence 1"))
        self.seq1_input.setText(_translate("MainWindow", "EQLLKALEFKL"))
        self.seq2_input.setText(_translate("MainWindow", "KVLEFGY"))
        self.label_2.setText(_translate("MainWindow", "Sequence 2"))
        self.label_3.setText(_translate("MainWindow", "Match Score"))
        self.label_4.setText(_translate("MainWindow", "Mismatch Score"))
        self.label_5.setText(_translate("MainWindow", "Gap Score"))
        self.find_alignment_btn.setText(_translate("MainWindow", "    Find Local Alignment    "))
        self.label_6.setText(_translate("MainWindow", "Possible Alignment Count "))
        self.label_7.setText(_translate("MainWindow", "Alignment Number"))
        self.label_8.setText(_translate("MainWindow", "Sequence 1"))
        self.label_9.setText(_translate("MainWindow", "Sequence 2"))
        self.next_alignment_btn.setText(_translate("MainWindow", "Show Next Alignment"))

    def run_aligner(self):
        self.aligner=la.local_aligner(str(self.seq1_input.text()),
                                      str(self.seq2_input.text()),
                                      int(self.match_score_input.text()),
                                      int(self.mismatch_score_input.text()),
                                      int(self.gap_score_input.text()))
        self.score_matrix,self.paths,self.print_texts=self.aligner.run()

        model=la.table_model(self.score_matrix,self.paths[0])
        self.score_matrix_table.setModel(model)
        #Tablo cell'lerinin boyutunu küçültmek için
        header=self.score_matrix_table.horizontalHeader()
        header.setSectionResizeMode(QtWidgets.QHeaderView.ResizeToContents)

        self.results_frame.show()

        self.possible_alignment_count.setText(str(len(self.paths)))
        self.alignment_no.setText('1')
        self.seq1_output.setText(self.print_texts[0][0])
        self.seq2_output.setText(self.print_texts[0][1])
        
    def next_path(self):
        path_index=int(self.alignment_no.text())
        if path_index==int(self.possible_alignment_count.text()):
            path_index=0

        model=la.table_model(self.score_matrix,self.paths[path_index])
        self.score_matrix_table.setModel(model)
        
        self.alignment_no.setText(str(path_index+1))
        self.seq1_output.setText(self.print_texts[path_index][0])
        self.seq2_output.setText(self.print_texts[path_index][1])    
        

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

