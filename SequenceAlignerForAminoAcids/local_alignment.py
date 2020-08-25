import pandas as pd
from PyQt5.QtWidgets import QTableView
from PyQt5.QtCore import QAbstractTableModel,Qt,QVariant
from PyQt5.QtGui import QColor

class table_model(QAbstractTableModel):

    def __init__(self,df,path):
        QAbstractTableModel.__init__(self)
        self.df=df
        self.path=path

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
                if [index.row(),index.column()] in self.path:
                    bgColor=QColor(Qt.green)
                return QVariant(QColor(bgColor))
        return None

    def headerData(self,col,orientation,role):
        if orientation==Qt.Horizontal and role==Qt.DisplayRole:
            return self.df.columns[col]
        return None

class local_aligner():

    def __init__(self,seq1,seq2,match_score,mismatch_score,gap_score):
        self.seq1='--'+seq1.upper()
        self.seq2='-'+seq2.upper()
        
        self.match_score=match_score
        self.mismatch_score=mismatch_score
        self.gap_score=gap_score

        self.paths=[[]]
        
        self.score_matrix=pd.DataFrame(index=list(self.seq2),columns=list(self.seq1))
        for i in range(len(self.seq2)):
            self.score_matrix.iloc[i][0]=self.seq2[i]

    def best_score_mismatch(self,left,upperleft,up,current):
        if left > up:#Gap
            best_score=left+self.gap_score
        else:
            best_score=up+self.gap_score
            
        if best_score<(upperleft+self.mismatch_score):#Mismatch
            best_score=upperleft+self.mismatch_score
            
        if best_score<0:
            best_score=0
            
        return best_score

    def score(self):
        columns=list(self.score_matrix.columns)
        rows=list(self.score_matrix.index)
        
        for i in range(1,len(columns)):
            self.score_matrix.iloc[0][i] = 0

        for i in range(1,len(rows)):
            self.score_matrix.iloc[i][1] = 0

        for i in range(1,len(rows)):
            for j in range(2,len(columns)):
                if rows[i]==columns[j]: #Match
                    self.score_matrix.iloc[i][j]=self.score_matrix.iloc[i-1][j-1]+self.match_score
                else:
                    self.score_matrix.iloc[i][j]=self.best_score_mismatch(self.score_matrix.iloc[i][j-1],
                                                                          self.score_matrix.iloc[i-1][j-1],
                                                                          self.score_matrix.iloc[i-1][j],
                                                                          self.score_matrix.iloc[i][j])

    def find_alignment(self,
                       current_cell_row,
                       current_cell_column,
                       path_index): #path_index işlediğimiz path indexi 

        self.paths[path_index].append([current_cell_row,current_cell_column])
        print(self.paths[path_index], path_index)
        print(self.paths)
        
        current=self.score_matrix.iloc[current_cell_row][current_cell_column]
        up=self.score_matrix.iloc[current_cell_row][current_cell_column-1]
        left=self.score_matrix.iloc[current_cell_row-1][current_cell_column]
        upperleft=self.score_matrix.iloc[current_cell_row-1][current_cell_column-1]

        match_possible=(current==(upperleft+self.match_score) and (upperleft>0))
        mismatch_possible=(current==(upperleft+self.mismatch_score))
        gap_possible_left=(current==(left+self.gap_score))
        gap_possible_up=(current==(up+self.gap_score))

        print(current,up,left,upperleft)

        print(match_possible,mismatch_possible,gap_possible_left,gap_possible_up)

        if (match_possible or mismatch_possible) and not gap_possible_left and not gap_possible_up:#Sadece çapraz gidilebilir
            self.find_alignment(current_cell_row-1,current_cell_column-1,path_index)
            
        elif not match_possible and not mismatch_possible and gap_possible_left and not gap_possible_up:#Sadece yatay gidilebilir
            self.find_alignment(current_cell_row-1,current_cell_column,path_index)
            
        elif not match_possible and not mismatch_possible and not gap_possible_left and gap_possible_up:#Sadece dikey gidilebilir
            self.find_alignment(current_cell_row,current_cell_column-1,path_index)


        elif match_possible or mismatch_possible:#Çapraz gidebilir
            if gap_possible_up:#Dikey gidebilir
                if gap_possible_left:#Yatay gidebilir
                    self.start_new_path(path_index)
                    self.start_new_path(path_index)

                    self.find_alignment(current_cell_row-1,current_cell_column-1,path_index)#Çapraz

                    self.find_alignment(current_cell_row-1,current_cell_column,(len(self.paths)-1))#Üst
                    
                    self.find_alignment(current_cell_row,current_cell_column-1,(len(self.paths)-2))#Sol
                    
                else:#Yatay gidemez    
                    self.start_new_path(path_index)
                    self.find_alignment(current_cell_row-1,current_cell_column,(len(self.paths)-1))#Üst

                    self.find_alignment(current_cell_row-1,current_cell_column-1,path_index)#Çapraz

            else:#Dikey gidemez
                if gap_possible_left:#Yatay gidebilir   
                    self.start_new_path(path_index)
                    self.find_alignment(current_cell_row,current_cell_column-1,(len(self.paths)-1))#Sol

                    self.find_alignment(current_cell_row-1,current_cell_column-1,path_index)#Çapraz

                    
        else:#Çapraz gidemez
            if gap_possible_up:#Dikey gidebilir
                if gap_possible_left:#Yatay gidebilir
                    self.start_new_path(path_index)
                    self.find_alignment(current_cell_row,current_cell_column-1,(len(self.paths)-1))#Sol

                    self.find_alignment(current_cell_row-1,current_cell_column,path_index)#Üst
                    
                    
            else:#Dikey gidemez
                if not gap_possible_left:#Yatay gidemez
                    print('Path index',path_index,'is done')

    def start_new_path(self,path_index):#Mevcut pathten yeni bir tane oluşturur. Farklı yolları bulmak için.
        self.paths.append([])
        for i in range(len(self.paths[path_index])):
            self.paths[len(self.paths)-1].append(self.paths[path_index][i])
        print('New path - '+str(path_index)+' to ' + str(len(self.paths)-1))
        print(self.paths)

##    def YolOlustur(self,gecis,x,y,dizi01,dizi02):
##        dizi_01=list(self.score_matrix.columns)
##        dizi_02=list(self.score_matrix.index)
##        
##        if x == 0 or y == 0:
##            return dizi01, dizi02
##
##        elif gecis.iloc[x][y] == 1: #Match
##            dizi01.append(dizi_01[x - 1])
##            dizi02.append(dizi_02[y - 1])
##            return self.YolOlustur(dizi_01, dizi_02, gecis, x - 1, y - 1, dizi01, dizi02)
##
##        elif gecis.iloc[x][y] == 2: #Mismatch
##            dizi01.append(dizi_01[x - 1])
##            dizi02.append(dizi_02[y - 1])
##            return self.YolOlustur(dizi_01, dizi_02, gecis, x - 1, y - 1, dizi01, dizi02)
##
##        elif gecis.iloc[x][y] == 3: #Sol
##            dizi01.append("_")
##            dizi02.append(dizi_02[y])
##            dizi01.append(dizi_01[x])
##            dizi02.append("_")
##            return self.YolOlustur(dizi_01, dizi_02, gecis, x - 1, y - 1, dizi01, dizi02)
##
##        elif gecis.iloc[x][y] == 4: #Üst
##            dizi01.append(dizi_01[x])
##            dizi02.append("_")
##            dizi01.append("_")
##            dizi02.append(dizi_02[y])
##            return self.YolOlustur(dizi_01, dizi_02, gecis, x - 1, y - 1, dizi01, dizi02)
##
##        else:
##            return dizi01, dizi02
##
##    def results(self):
##        print_texts=[]
##            
##        gecis=pd.DataFrame(index=list(self.score_matrix.index),columns=list(self.score_matrix.columns))
##        gecis.fillna(value=0,inplace=True)
##        
##        for i in range(len(self.paths)):
##            for j in range(len(self.paths[i])):
##                if self.paths[i][j-1][0]==self.paths[i][j][0]+1:
##                    if self.paths[i][j-1][1]==self.paths[i][j][1]+1:#Match-Mismatch
##                       gecis.iloc[i][j]=1
##                    elif self.paths[i][j-1][1]==self.paths[i][j][1]:#Sol
##                       gecis.iloc[i][j]=3
##                elif self.paths[i][j-1][0]==self.paths[i][j][0]:
##                    if self.paths[i][j-1][1]==self.paths[i][j][1]+1:#Üst
##                       gecis.iloc[i][j]=4
##                               
##            dizi01,dizi02=self.YolOlustur(gecis,self.paths[i][0][0],self.paths[i][0][1],[],[])
##            dizi01=dizi01[::-1]
##            dizi02=dizi02[::-1]
##            print(dizi01,dizi02)
##            print_texts.append([dizi01,dizi02])
##
##        print(print_texts)
##        return self.score_matrix,self.paths,print_texts

##    def results(self):
##        print_texts=[]
##
##        rows=list(self.score_matrix.index)
##        columns=list(self.score_matrix.columns)
##        
##        for i in range(len(self.paths)):
##            seq1_output=str(i)+':'
##            seq2_output=str(i)+':'
##            for j in range(len(self.paths[i])):
##                current_cell=self.paths[i][j]
##                current_cell_row=rows[current_cell[0]]
##                current_cell_col=columns[current_cell[1]]
##                if j==len(self.paths[i])-1:
##                    seq1_output+=current_cell_row
##                    seq2_output+=current_cell_col
##                    break
##                
##                prev_cell=self.paths[i][j+1]
##
##                if current_cell[0]==prev_cell[0]-1:
##                    if current_cell[1]==prev_cell[1]-1:#Çapraz gelmiş
##                        seq1_output+=current_cell_row
##                        seq2_output+=current_cell_col
##                        
##                    elif current_cell[1]==prev_cell[1]:#Soldan gelmiş
##                        seq1_output+='-'
##                        seq2_output+=current_cell_col
##                elif current_cell[0]==prev_cell[0]:
##                    if current_cell[1]==prev_cell[1]-1:#Üstten gelmiş
##                        seq1_output+=current_cell_row
##                        seq2_output+='-'
##            seq1_output=seq1_output[::-1]#Ters çevirir
##            seq2_output=seq2_output[::-1]#Ters çevirir
##            print_texts.append([seq1_output,seq2_output])
##
##        return self.score_matrix,self.paths,print_texts

    def results(self):
        print_texts=[]

        columns=list(self.score_matrix.columns) #Seq1
        rows=list(self.score_matrix.index) #Seq2

        print('Now in results function :')
        
        for i in range(len(self.paths)):
            seq1_output=''
            seq2_output=''
            for j in range(len(self.paths[i])):
                #self.paths[i][j][0]=>Row
                #self.paths[i][j][1]=>Column
                if j==len(self.paths[i])-1:
                    seq1_output+=columns[self.paths[i][j][1]]
                    seq2_output+=rows[self.paths[i][j][0]]
                    
                elif self.paths[i][j][0]==self.paths[i][j+1][0]+1:
                    if self.paths[i][j][1]==self.paths[i][j+1][1]+1:#Çapraz - Hem row hem column yazılır
                        seq1_output+=columns[self.paths[i][j][1]]
                        seq2_output+=rows[self.paths[i][j][0]]
                        
                elif self.paths[i][j][0]==self.paths[i][j+1][0]+1:
                    if self.paths[i][j][1]==self.paths[i][j+1][1]:#Üst - Column yazılır row gap
                        seq1_output+=columns[self.paths[i][j][1]]
                        seq2_output+='-'

                elif self.paths[i][j][0]==self.paths[i][j+1][0]:
                    if self.paths[i][j][1]==self.paths[i][j+1][1]+1:#Sol - Row yazılır column gap
                        seq1_output+='-'
                        seq2_output+=rows[self.paths[i][j][0]]
                        
            seq1_output=seq1_output[::-1]
            seq2_output=seq2_output[::-1]
            
            print_texts.append([seq1_output,seq2_output])
            print(seq1_output,seq2_output,print_texts)
            
        return self.score_matrix,self.paths,print_texts
    
    def run(self):
        self.score()
        
        best_score=-1
        best_score_row=1
        best_score_col=1
        for i in range(len(list(self.score_matrix.index))):
            for j in range(len(list(self.score_matrix.columns))):
                if isinstance(self.score_matrix.iloc[i][j],int):
                    print(self.score_matrix.iloc[i][j],'is int, best score : ',best_score,', best score indexes [',best_score_row,',',best_score_col,']')
                    if (self.score_matrix.iloc[i][j])>best_score:
                        best_score=self.score_matrix.iloc[i][j]
                        best_score_row=i
                        best_score_col=j
                else: print(self.score_matrix.iloc[i][j],'is not int, best score : ',best_score)

        print(self.score_matrix)
        print('Printing alignment with starting point of [',best_score_row,',',best_score_col,']')
        self.find_alignment(best_score_row,best_score_col,(len(self.paths)-1))
        
        return self.results()
            
