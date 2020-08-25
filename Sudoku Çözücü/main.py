import sys
from PyQt5 import QtWidgets
from sudoku_form import SudokuForm

if __name__=='__main__':
    app=QtWidgets.QApplication(sys.argv)
    ana_ekran=SudokuForm()
    ana_ekran.show()
    
    sys.exit(app.exec_())