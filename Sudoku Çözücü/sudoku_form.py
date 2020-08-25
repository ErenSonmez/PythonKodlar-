from PyQt5.QtWidgets import QMainWindow,QFileDialog,QMessageBox
from sudoku_window import Ui_MainWindow as SudokuWindow
from sudokusolver import SudokuSolver
from sudoku_loader import SudokuLoader

class SudokuForm(QMainWindow,SudokuWindow):
    def __init__(self,parent=None):
        QMainWindow.__init__(self,parent)
        self.setupUi(self)
        
        self.solve_btn.clicked.connect(self.run_solver)
        self.sudokuyu_kaydet_action.triggered.connect(self.save_sudoku)
        self.sudoku_yukle_action.triggered.connect(self.load_sudoku)
        self.yeni_sudoku_action.triggered.connect(self.refresh_table)
        
        self.refresh_table()
        self.connect_char_limit_control()
        
    def run_solver(self):
        x=self.get_data()
        solver=SudokuSolver(x)
        result=solver.solve()
        if result==False:
            popup=QMessageBox()
            popup.setWindowTitle('Başarısız')
            popup.setText('Sudoku çözme işlemi başarısız.')
            popup.exec_()
            return
        else:
            popup=QMessageBox()
            popup.setWindowTitle('Başarılı')
            popup.setText('Sudoku çözme işlemi başarılı.')
            popup.exec_()
            
        solver.update_table()
        self.set_data(solver.sudoku_table.values.tolist())
        
    def save_sudoku(self):
        x=self.get_data()
        
        filename,_=QFileDialog.getSaveFileName(self,'Kaydedilecek dosya adını giriniz','','SUDOKU dosyası(*.sudoku)')
        if filename=='':
            popup=QMessageBox()
            popup.setWindowTitle('Hata')
            popup.setText('Dosya adı girilmedi')
            popup.exec_()
            return
        
        loader=SudokuLoader()
        loader.sudoku=x
        loader.save_to(filename)
        
    def load_sudoku(self):
        filename,_=QFileDialog.getOpenFileName(self,'Dosyayı seçiniz','','SUDOKU dosyası(*.sudoku)')
        if filename=='':
            popup=QMessageBox()
            popup.setWindowTitle('Hata')
            popup.setText('Dosya bulunamadı')
            popup.exec_()
            return
        
        loader=SudokuLoader()
        x=loader.get_sudoku(filename)
        print(x)
        self.set_data(x)
        
    def char_limit_control(self,cell):
        if len(cell.toPlainText())>1:
            celltext=self.split(str(cell.toPlainText()))
            celltext=celltext[len(celltext)-1]
            cell.setText(str(celltext))
    
    def split(self,word): 
        return [char for char in word] 
        
    #TODO: değişken adını kullanarak işlemi basitleştir.
    def get_data(self):
        row1=[]
        row1.append(int(self.cell11_11.toPlainText()))
        row1.append(int(self.cell11_12.toPlainText()))
        row1.append(int(self.cell11_13.toPlainText()))
        row1.append(int(self.cell12_11.toPlainText()))
        row1.append(int(self.cell12_12.toPlainText()))
        row1.append(int(self.cell12_13.toPlainText()))
        row1.append(int(self.cell13_11.toPlainText()))
        row1.append(int(self.cell13_12.toPlainText()))
        row1.append(int(self.cell13_13.toPlainText()))
        
        row2=[]
        row2.append(int(self.cell11_21.toPlainText()))
        row2.append(int(self.cell11_22.toPlainText()))
        row2.append(int(self.cell11_23.toPlainText()))
        row2.append(int(self.cell12_21.toPlainText()))
        row2.append(int(self.cell12_22.toPlainText()))
        row2.append(int(self.cell12_23.toPlainText()))
        row2.append(int(self.cell13_21.toPlainText()))
        row2.append(int(self.cell13_22.toPlainText()))
        row2.append(int(self.cell13_23.toPlainText()))
        
        row3=[]
        row3.append(int(self.cell11_31.toPlainText()))
        row3.append(int(self.cell11_32.toPlainText()))
        row3.append(int(self.cell11_33.toPlainText()))
        row3.append(int(self.cell12_31.toPlainText()))
        row3.append(int(self.cell12_32.toPlainText()))
        row3.append(int(self.cell12_33.toPlainText()))
        row3.append(int(self.cell13_31.toPlainText()))
        row3.append(int(self.cell13_32.toPlainText()))
        row3.append(int(self.cell13_33.toPlainText()))
        
        row4=[]
        row4.append(int(self.cell21_11.toPlainText()))
        row4.append(int(self.cell21_12.toPlainText()))
        row4.append(int(self.cell21_13.toPlainText()))
        row4.append(int(self.cell22_11.toPlainText()))
        row4.append(int(self.cell22_12.toPlainText()))
        row4.append(int(self.cell22_13.toPlainText()))
        row4.append(int(self.cell23_11.toPlainText()))
        row4.append(int(self.cell23_12.toPlainText()))
        row4.append(int(self.cell23_13.toPlainText()))
        
        row5=[]
        row5.append(int(self.cell21_21.toPlainText()))
        row5.append(int(self.cell21_22.toPlainText()))
        row5.append(int(self.cell21_23.toPlainText()))
        row5.append(int(self.cell22_21.toPlainText()))
        row5.append(int(self.cell22_22.toPlainText()))
        row5.append(int(self.cell22_23.toPlainText()))
        row5.append(int(self.cell23_21.toPlainText()))
        row5.append(int(self.cell23_22.toPlainText()))
        row5.append(int(self.cell23_23.toPlainText()))
        
        row6=[]
        row6.append(int(self.cell21_31.toPlainText()))
        row6.append(int(self.cell21_32.toPlainText()))
        row6.append(int(self.cell21_33.toPlainText()))
        row6.append(int(self.cell22_31.toPlainText()))
        row6.append(int(self.cell22_32.toPlainText()))
        row6.append(int(self.cell22_33.toPlainText()))
        row6.append(int(self.cell23_31.toPlainText()))
        row6.append(int(self.cell23_32.toPlainText()))
        row6.append(int(self.cell23_33.toPlainText()))
        
        row7=[]
        row7.append(int(self.cell31_11.toPlainText()))
        row7.append(int(self.cell31_12.toPlainText()))
        row7.append(int(self.cell31_13.toPlainText()))
        row7.append(int(self.cell32_11.toPlainText()))
        row7.append(int(self.cell32_12.toPlainText()))
        row7.append(int(self.cell32_13.toPlainText()))
        row7.append(int(self.cell33_11.toPlainText()))
        row7.append(int(self.cell33_12.toPlainText()))
        row7.append(int(self.cell33_13.toPlainText()))
        
        row8=[]
        row8.append(int(self.cell31_21.toPlainText()))
        row8.append(int(self.cell31_22.toPlainText()))
        row8.append(int(self.cell31_23.toPlainText()))
        row8.append(int(self.cell32_21.toPlainText()))
        row8.append(int(self.cell32_22.toPlainText()))
        row8.append(int(self.cell32_23.toPlainText()))
        row8.append(int(self.cell33_21.toPlainText()))
        row8.append(int(self.cell33_22.toPlainText()))
        row8.append(int(self.cell33_23.toPlainText()))
        
        row9=[]
        row9.append(int(self.cell31_31.toPlainText()))
        row9.append(int(self.cell31_32.toPlainText()))
        row9.append(int(self.cell31_33.toPlainText()))
        row9.append(int(self.cell32_31.toPlainText()))
        row9.append(int(self.cell32_32.toPlainText()))
        row9.append(int(self.cell32_33.toPlainText()))
        row9.append(int(self.cell33_31.toPlainText()))
        row9.append(int(self.cell33_32.toPlainText()))
        row9.append(int(self.cell33_33.toPlainText()))
        
        x=[row1,row2,row3,row4,row5,row6,row7,row8,row9]
        
        return x
    
    def set_data(self,data):
        i=0
        j=0
        self.cell11_11.setText(str(data[i][j]))
        j+=1
        self.cell11_12.setText(str(data[i][j]))
        j+=1
        self.cell11_13.setText(str(data[i][j]))
        j+=1
        self.cell12_11.setText(str(data[i][j]))
        j+=1
        self.cell12_12.setText(str(data[i][j]))
        j+=1
        self.cell12_13.setText(str(data[i][j]))
        j+=1
        self.cell13_11.setText(str(data[i][j]))
        j+=1
        self.cell13_12.setText(str(data[i][j]))
        j+=1
        self.cell13_13.setText(str(data[i][j]))
        
        i=1
        j=0
        self.cell11_21.setText(str(data[i][j]))
        j+=1
        self.cell11_22.setText(str(data[i][j]))
        j+=1
        self.cell11_23.setText(str(data[i][j]))
        j+=1
        self.cell12_21.setText(str(data[i][j]))
        j+=1
        self.cell12_22.setText(str(data[i][j]))
        j+=1
        self.cell12_23.setText(str(data[i][j]))
        j+=1
        self.cell13_21.setText(str(data[i][j]))
        j+=1
        self.cell13_22.setText(str(data[i][j]))
        j+=1
        self.cell13_23.setText(str(data[i][j]))
        
        i=2
        j=0
        self.cell11_31.setText(str(data[i][j]))
        j+=1
        self.cell11_32.setText(str(data[i][j]))
        j+=1
        self.cell11_33.setText(str(data[i][j]))
        j+=1
        self.cell12_31.setText(str(data[i][j]))
        j+=1
        self.cell12_32.setText(str(data[i][j]))
        j+=1
        self.cell12_33.setText(str(data[i][j]))
        j+=1
        self.cell13_31.setText(str(data[i][j]))
        j+=1
        self.cell13_32.setText(str(data[i][j]))
        j+=1
        self.cell13_33.setText(str(data[i][j]))
        
        i=3
        j=0
        self.cell21_11.setText(str(data[i][j]))
        j+=1
        self.cell21_12.setText(str(data[i][j]))
        j+=1
        self.cell21_13.setText(str(data[i][j]))
        j+=1
        self.cell22_11.setText(str(data[i][j]))
        j+=1
        self.cell22_12.setText(str(data[i][j]))
        j+=1
        self.cell22_13.setText(str(data[i][j]))
        j+=1
        self.cell23_11.setText(str(data[i][j]))
        j+=1
        self.cell23_12.setText(str(data[i][j]))
        j+=1
        self.cell23_13.setText(str(data[i][j]))
        
        i=4
        j=0
        self.cell21_21.setText(str(data[i][j]))
        j+=1
        self.cell21_22.setText(str(data[i][j]))
        j+=1
        self.cell21_23.setText(str(data[i][j]))
        j+=1
        self.cell22_21.setText(str(data[i][j]))
        j+=1
        self.cell22_22.setText(str(data[i][j]))
        j+=1
        self.cell22_23.setText(str(data[i][j]))
        j+=1
        self.cell23_21.setText(str(data[i][j]))
        j+=1
        self.cell23_22.setText(str(data[i][j]))
        j+=1
        self.cell23_23.setText(str(data[i][j]))
        
        i=5
        j=0
        self.cell21_31.setText(str(data[i][j]))
        j+=1
        self.cell21_32.setText(str(data[i][j]))
        j+=1
        self.cell21_33.setText(str(data[i][j]))
        j+=1
        self.cell22_31.setText(str(data[i][j]))
        j+=1
        self.cell22_32.setText(str(data[i][j]))
        j+=1
        self.cell22_33.setText(str(data[i][j]))
        j+=1
        self.cell23_31.setText(str(data[i][j]))
        j+=1
        self.cell23_32.setText(str(data[i][j]))
        j+=1
        self.cell23_33.setText(str(data[i][j]))
        
        i=6
        j=0
        self.cell31_11.setText(str(data[i][j]))
        j+=1
        self.cell31_12.setText(str(data[i][j]))
        j+=1
        self.cell31_13.setText(str(data[i][j]))
        j+=1
        self.cell32_11.setText(str(data[i][j]))
        j+=1
        self.cell32_12.setText(str(data[i][j]))
        j+=1
        self.cell32_13.setText(str(data[i][j]))
        j+=1
        self.cell33_11.setText(str(data[i][j]))
        j+=1
        self.cell33_12.setText(str(data[i][j]))
        j+=1
        self.cell33_13.setText(str(data[i][j]))
        
        i=7
        j=0
        self.cell31_21.setText(str(data[i][j]))
        j+=1
        self.cell31_22.setText(str(data[i][j]))
        j+=1
        self.cell31_23.setText(str(data[i][j]))
        j+=1
        self.cell32_21.setText(str(data[i][j]))
        j+=1
        self.cell32_22.setText(str(data[i][j]))
        j+=1
        self.cell32_23.setText(str(data[i][j]))
        j+=1
        self.cell33_21.setText(str(data[i][j]))
        j+=1
        self.cell33_22.setText(str(data[i][j]))
        j+=1
        self.cell33_23.setText(str(data[i][j]))
        
        i=8
        j=0
        self.cell31_31.setText(str(data[i][j]))
        j+=1
        self.cell31_32.setText(str(data[i][j]))
        j+=1
        self.cell31_33.setText(str(data[i][j]))
        j+=1
        self.cell32_31.setText(str(data[i][j]))
        j+=1
        self.cell32_32.setText(str(data[i][j]))
        j+=1
        self.cell32_33.setText(str(data[i][j]))
        j+=1
        self.cell33_31.setText(str(data[i][j]))
        j+=1
        self.cell33_32.setText(str(data[i][j]))
        j+=1
        self.cell33_33.setText(str(data[i][j]))
        
    def refresh_table(self):
        self.cell11_11.setText(str(0))
        self.cell11_12.setText(str(0))
        self.cell11_13.setText(str(0))
        self.cell12_11.setText(str(0))
        self.cell12_12.setText(str(0))
        self.cell12_13.setText(str(0))
        self.cell13_11.setText(str(0))
        self.cell13_12.setText(str(0))
        self.cell13_13.setText(str(0))
        
        self.cell11_21.setText(str(0))
        self.cell11_22.setText(str(0))
        self.cell11_23.setText(str(0))
        self.cell12_21.setText(str(0))
        self.cell12_22.setText(str(0))
        self.cell12_23.setText(str(0))
        self.cell13_21.setText(str(0))
        self.cell13_22.setText(str(0))
        self.cell13_23.setText(str(0))
        
        self.cell11_31.setText(str(0))
        self.cell11_32.setText(str(0))
        self.cell11_33.setText(str(0))
        self.cell12_31.setText(str(0))
        self.cell12_32.setText(str(0))
        self.cell12_33.setText(str(0))
        self.cell13_31.setText(str(0))
        self.cell13_32.setText(str(0))
        self.cell13_33.setText(str(0))
        
        self.cell21_11.setText(str(0))
        self.cell21_12.setText(str(0))
        self.cell21_13.setText(str(0))
        self.cell22_11.setText(str(0))
        self.cell22_12.setText(str(0))
        self.cell22_13.setText(str(0))
        self.cell23_11.setText(str(0))
        self.cell23_12.setText(str(0))
        self.cell23_13.setText(str(0))
        
        self.cell21_21.setText(str(0))
        self.cell21_22.setText(str(0))
        self.cell21_23.setText(str(0))
        self.cell22_21.setText(str(0))
        self.cell22_22.setText(str(0))
        self.cell22_23.setText(str(0))
        self.cell23_21.setText(str(0))
        self.cell23_22.setText(str(0))
        self.cell23_23.setText(str(0))
        
        self.cell21_31.setText(str(0))
        self.cell21_32.setText(str(0))
        self.cell21_33.setText(str(0))
        self.cell22_31.setText(str(0))
        self.cell22_32.setText(str(0))
        self.cell22_33.setText(str(0))
        self.cell23_31.setText(str(0))
        self.cell23_32.setText(str(0))
        self.cell23_33.setText(str(0))
        
        self.cell31_11.setText(str(0))
        self.cell31_12.setText(str(0))
        self.cell31_13.setText(str(0))
        self.cell32_11.setText(str(0))
        self.cell32_12.setText(str(0))
        self.cell32_13.setText(str(0))
        self.cell33_11.setText(str(0))
        self.cell33_12.setText(str(0))
        self.cell33_13.setText(str(0))
        
        self.cell31_21.setText(str(0))
        self.cell31_22.setText(str(0))
        self.cell31_23.setText(str(0))
        self.cell32_21.setText(str(0))
        self.cell32_22.setText(str(0))
        self.cell32_23.setText(str(0))
        self.cell33_21.setText(str(0))
        self.cell33_22.setText(str(0))
        self.cell33_23.setText(str(0))
        
        self.cell31_31.setText(str(0))
        self.cell31_32.setText(str(0))
        self.cell31_33.setText(str(0))
        self.cell32_31.setText(str(0))
        self.cell32_32.setText(str(0))
        self.cell32_33.setText(str(0))
        self.cell33_31.setText(str(0))
        self.cell33_32.setText(str(0))
        self.cell33_33.setText(str(0))
        
    def connect_char_limit_control(self):
        self.cell11_11.textChanged.connect(lambda:self.char_limit_control(self.cell11_11))
        self.cell11_12.textChanged.connect(lambda:self.char_limit_control(self.cell11_12))
        self.cell11_13.textChanged.connect(lambda:self.char_limit_control(self.cell11_13))
        self.cell12_11.textChanged.connect(lambda:self.char_limit_control(self.cell12_11))
        self.cell12_12.textChanged.connect(lambda:self.char_limit_control(self.cell12_12))
        self.cell12_13.textChanged.connect(lambda:self.char_limit_control(self.cell12_13))
        self.cell13_11.textChanged.connect(lambda:self.char_limit_control(self.cell13_11))
        self.cell13_12.textChanged.connect(lambda:self.char_limit_control(self.cell13_12))
        self.cell13_13.textChanged.connect(lambda:self.char_limit_control(self.cell13_13))
        
        self.cell11_21.textChanged.connect(lambda:self.char_limit_control(self.cell11_21))
        self.cell11_22.textChanged.connect(lambda:self.char_limit_control(self.cell11_22))
        self.cell11_23.textChanged.connect(lambda:self.char_limit_control(self.cell11_23))
        self.cell12_21.textChanged.connect(lambda:self.char_limit_control(self.cell12_21))
        self.cell12_22.textChanged.connect(lambda:self.char_limit_control(self.cell12_22))
        self.cell12_23.textChanged.connect(lambda:self.char_limit_control(self.cell12_23))
        self.cell13_21.textChanged.connect(lambda:self.char_limit_control(self.cell13_21))
        self.cell13_22.textChanged.connect(lambda:self.char_limit_control(self.cell13_22))
        self.cell13_23.textChanged.connect(lambda:self.char_limit_control(self.cell13_23))
        
        self.cell11_31.textChanged.connect(lambda:self.char_limit_control(self.cell11_31))
        self.cell11_32.textChanged.connect(lambda:self.char_limit_control(self.cell11_32))
        self.cell11_33.textChanged.connect(lambda:self.char_limit_control(self.cell11_33))
        self.cell12_31.textChanged.connect(lambda:self.char_limit_control(self.cell12_31))
        self.cell12_32.textChanged.connect(lambda:self.char_limit_control(self.cell12_32))
        self.cell12_33.textChanged.connect(lambda:self.char_limit_control(self.cell12_33))
        self.cell13_31.textChanged.connect(lambda:self.char_limit_control(self.cell13_31))
        self.cell13_32.textChanged.connect(lambda:self.char_limit_control(self.cell13_32))
        self.cell13_33.textChanged.connect(lambda:self.char_limit_control(self.cell13_33))
        
        self.cell21_11.textChanged.connect(lambda:self.char_limit_control(self.cell21_11))
        self.cell21_12.textChanged.connect(lambda:self.char_limit_control(self.cell21_12))
        self.cell21_13.textChanged.connect(lambda:self.char_limit_control(self.cell21_13))
        self.cell22_11.textChanged.connect(lambda:self.char_limit_control(self.cell22_11))
        self.cell22_12.textChanged.connect(lambda:self.char_limit_control(self.cell22_12))
        self.cell22_13.textChanged.connect(lambda:self.char_limit_control(self.cell22_13))
        self.cell23_11.textChanged.connect(lambda:self.char_limit_control(self.cell23_11))
        self.cell23_12.textChanged.connect(lambda:self.char_limit_control(self.cell23_12))
        self.cell23_13.textChanged.connect(lambda:self.char_limit_control(self.cell23_13))
        
        self.cell21_21.textChanged.connect(lambda:self.char_limit_control(self.cell21_21))
        self.cell21_22.textChanged.connect(lambda:self.char_limit_control(self.cell21_22))
        self.cell21_23.textChanged.connect(lambda:self.char_limit_control(self.cell21_23))
        self.cell22_21.textChanged.connect(lambda:self.char_limit_control(self.cell22_21))
        self.cell22_22.textChanged.connect(lambda:self.char_limit_control(self.cell22_22))
        self.cell22_23.textChanged.connect(lambda:self.char_limit_control(self.cell22_23))
        self.cell23_21.textChanged.connect(lambda:self.char_limit_control(self.cell23_21))
        self.cell23_22.textChanged.connect(lambda:self.char_limit_control(self.cell23_22))
        self.cell23_23.textChanged.connect(lambda:self.char_limit_control(self.cell23_23))
        
        self.cell21_31.textChanged.connect(lambda:self.char_limit_control(self.cell21_31))
        self.cell21_32.textChanged.connect(lambda:self.char_limit_control(self.cell21_32))
        self.cell21_33.textChanged.connect(lambda:self.char_limit_control(self.cell21_33))
        self.cell22_31.textChanged.connect(lambda:self.char_limit_control(self.cell22_31))
        self.cell22_32.textChanged.connect(lambda:self.char_limit_control(self.cell22_32))
        self.cell22_33.textChanged.connect(lambda:self.char_limit_control(self.cell22_33))
        self.cell23_31.textChanged.connect(lambda:self.char_limit_control(self.cell23_31))
        self.cell23_32.textChanged.connect(lambda:self.char_limit_control(self.cell23_32))
        self.cell23_33.textChanged.connect(lambda:self.char_limit_control(self.cell23_33))
        
        self.cell31_11.textChanged.connect(lambda:self.char_limit_control(self.cell31_11))
        self.cell31_12.textChanged.connect(lambda:self.char_limit_control(self.cell31_12))
        self.cell31_13.textChanged.connect(lambda:self.char_limit_control(self.cell31_13))
        self.cell32_11.textChanged.connect(lambda:self.char_limit_control(self.cell32_11))
        self.cell32_12.textChanged.connect(lambda:self.char_limit_control(self.cell32_12))
        self.cell32_13.textChanged.connect(lambda:self.char_limit_control(self.cell32_13))
        self.cell33_11.textChanged.connect(lambda:self.char_limit_control(self.cell33_11))
        self.cell33_12.textChanged.connect(lambda:self.char_limit_control(self.cell33_12))
        self.cell33_13.textChanged.connect(lambda:self.char_limit_control(self.cell33_13))
        
        self.cell31_21.textChanged.connect(lambda:self.char_limit_control(self.cell31_21))
        self.cell31_22.textChanged.connect(lambda:self.char_limit_control(self.cell31_22))
        self.cell31_23.textChanged.connect(lambda:self.char_limit_control(self.cell31_23))
        self.cell32_21.textChanged.connect(lambda:self.char_limit_control(self.cell32_21))
        self.cell32_22.textChanged.connect(lambda:self.char_limit_control(self.cell32_22))
        self.cell32_23.textChanged.connect(lambda:self.char_limit_control(self.cell32_23))
        self.cell33_21.textChanged.connect(lambda:self.char_limit_control(self.cell33_21))
        self.cell33_22.textChanged.connect(lambda:self.char_limit_control(self.cell33_22))
        self.cell33_23.textChanged.connect(lambda:self.char_limit_control(self.cell33_23))
        
        self.cell31_31.textChanged.connect(lambda:self.char_limit_control(self.cell31_31))
        self.cell31_32.textChanged.connect(lambda:self.char_limit_control(self.cell31_32))
        self.cell31_33.textChanged.connect(lambda:self.char_limit_control(self.cell31_33))
        self.cell32_31.textChanged.connect(lambda:self.char_limit_control(self.cell32_31))
        self.cell32_32.textChanged.connect(lambda:self.char_limit_control(self.cell32_32))
        self.cell32_33.textChanged.connect(lambda:self.char_limit_control(self.cell32_33))
        self.cell33_31.textChanged.connect(lambda:self.char_limit_control(self.cell33_31))
        self.cell33_32.textChanged.connect(lambda:self.char_limit_control(self.cell33_32))
        self.cell33_33.textChanged.connect(lambda:self.char_limit_control(self.cell33_33))
        