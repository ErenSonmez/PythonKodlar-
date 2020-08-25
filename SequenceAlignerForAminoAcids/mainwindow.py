# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
import global_alignment_window as gaw
import local_alignment_window as law
import multiple_alignment_window as maw

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(728, 185)
        
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        
        self.verticalLayout.addItem(spacerItem)

        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(20)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)

        spacerItem1 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.MinimumExpanding)
        self.verticalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        self.global_alignment_btn = QtWidgets.QPushButton(self.centralwidget)
        self.global_alignment_btn.setObjectName("global_alignment_btn")
        self.global_alignment_btn.clicked.connect(lambda : self.show_window(gaw.Ui_MainWindow()))
        self.horizontalLayout_2.addWidget(self.global_alignment_btn)

        self.local_alignment_btn = QtWidgets.QPushButton(self.centralwidget)
        self.local_alignment_btn.setObjectName("local_alignment_btn")
        self.local_alignment_btn.clicked.connect(lambda : self.show_window(law.Ui_MainWindow()))
        self.horizontalLayout_2.addWidget(self.local_alignment_btn)

        self.multiple_alignment_btn = QtWidgets.QPushButton(self.centralwidget)
        self.multiple_alignment_btn.setObjectName("multiple_alignment_btn")
        self.multiple_alignment_btn.clicked.connect(lambda : self.show_window(maw.Ui_MainWindow()))
        self.horizontalLayout_2.addWidget(self.multiple_alignment_btn)
        self.verticalLayout.addLayout(self.horizontalLayout_2)

        spacerItem2 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem2)
        MainWindow.setCentralWidget(self.centralwidget)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Sequence Aligner for Amino Acids"))
        self.label.setText(_translate("MainWindow", "Please select an alignment method to use"))
        self.global_alignment_btn.setText(_translate("MainWindow", "Global Alignment"))
        self.local_alignment_btn.setText(_translate("MainWindow", "Local Alignment"))
        self.multiple_alignment_btn.setText(_translate("MainWindow", "Multiple Alignment - Greedy Approach"))

    def show_window(self, new_window):
        self.window=QtWidgets.QMainWindow()
        self.ui=new_window
        self.ui.setupUi(self.window)
        self.window.show()


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
    ui.show_window(ui,Ui_global_alignment_window())

