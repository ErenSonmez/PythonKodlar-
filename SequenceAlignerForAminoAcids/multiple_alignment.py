import pandas as pd
from PyQt5.QtWidgets import QApplication,QTableView
from PyQt5.QtCore import QAbstractTableModel,Qt,QVariant
from PyQt5.QtGui import QColor

class table_model(QAbstractTableModel):

    def __init__(self,df,matches,hm_cells):
        QAbstractTableModel.__init__(self)
        self.df=df
        self.matches=matches
        self.hm_cells=hm_cells

    def rowCount(self,parent=None):
        return self.df.shape[0]

    def columnCount(self,parent=None):
        return self.df.shape[1]

    def data(self,index,role):
        if index.isValid():
            if role==Qt.DisplayRole:
                return str(self.df.iloc[index.row(), index.column()])
            if role==Qt.BackgroundColorRole:
                bgColor=QColor(Qt.white)
                if [index.row(),index.column()] in self.hm_cells:
                    bgColor=QColor(Qt.green)
                elif [index.row(),index.column()] in self.matches:
                    bgColor=QColor(Qt.blue)
                return QVariant(QColor(bgColor))
        return None
    
    def headerData(self,col,orientation,role):
        if orientation==Qt.Horizontal and role==Qt.DisplayRole:
            return self.df.columns[col]
        return None
    


class multiple_aligner:

    def __init__(self,seq1,seq2,k):
        self.seq1='-'+seq1.upper()
        self.seq2=seq2.upper()
        self.k=k

        self.matches=[]
        self.diagonals=[]

        self.highest_match_score=-1
        self.highest_match_cells=None

        self.score_matrix=pd.DataFrame(index=list(self.seq2),columns=list(self.seq1))
        for i in range(len(self.seq2)):
            self.score_matrix.iloc[i][0]=self.seq2[i]
        self.score_matrix.fillna('-', inplace=True)

    def find_matches(self):
        
        rows=list(self.score_matrix.index)
        columns=list(self.score_matrix.columns)

        for i in range(len(rows)):
            for j in range(1,len(columns)):
                if rows[i]==columns[j]:
                    self.matches.append([i,j])
                    self.score_matrix.iloc[i][j]='*'

    def find_diagonals(self):        
        for i in self.matches:
            row=i[0]
            column=i[1]
            found_diagonals=0
            
            while 1:
                if row+1==len(self.score_matrix.index) or column+1==len(self.score_matrix.columns):
                    break
                
                row=row+1
                column=column+1
                
                if self.score_matrix.iloc[row][column]=='*':
                    found_diagonals=found_diagonals+1
                else:
                    break
            if found_diagonals>=self.k:
                self.diagonals.append([[i[0],i[1]],[row-1,column-1]])#Başlangıç ve bitiş noktalarını kaydeder
                if self.highest_match_score<found_diagonals:
                    self.highest_match_score=found_diagonals
                    self.highest_match_cells=[[i[0],i[1]],[row-1,column-1]]


    def results(self):
        hmc_start=[]
        hmc_start.append(self.highest_match_cells[0][0])
        hmc_start.append(self.highest_match_cells[0][1])

        hmc_end=[]
        hmc_end.append(self.highest_match_cells[1][0])
        hmc_end.append(self.highest_match_cells[1][1])
        
        hmc=[]#Bu değişken en uzun match köşegeninin tüm noktalarını tutar. Bunu arayüzde göstermeyi kolaylaştırmak için yaptım.
        hmc.append([hmc_start[0],hmc_start[1]])
        while 1:
            hmc_start[0]+=1
            hmc_start[1]+=1
            
            if hmc_start[0]==hmc_end[0]:
                hmc.append([hmc_start[0],hmc_start[1]])
                break

            hmc.append([hmc_start[0],hmc_start[1]])
            
        return self.score_matrix,self.matches,self.highest_match_score,hmc
    

    def run(self):
        self.find_matches()
        self.find_diagonals()
        return self.results()
