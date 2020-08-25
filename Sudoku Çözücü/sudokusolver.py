import pandas as pd
import pickle

class SudokuSolver:
    #List olarak tabloyu alır.
    def __init__(self, x):
        for i in range(len(x)):
            for j in range(len(x[i])):
                if x[i][j]==0 or x[i][j]=='':
                    x[i][j]='#'
                    
        self.sudoku_table=pd.DataFrame(x,index=[1,2,3,4,5,6,7,8,9],columns=[1,2,3,4,5,6,7,8,9])
        self.solve_table=self.sudoku_table.values.tolist()
        for row in range(len(self.solve_table)):
            for col in range(len(self.solve_table[row])):
                if self.solve_table[row][col]=='#':
                    self.solve_table[row][col]=[1,2,3,4,5,6,7,8,9]

        self.solve_table=pd.DataFrame(self.solve_table,index=[1,2,3,4,5,6,7,8,9],columns=[1,2,3,4,5,6,7,8,9])
        
    #Bilinmeyen hücrelerin çözümlemesini yapan ana fonksiyon. Diğer fonksiyonları
    #kullanarak bilinmeyen hücreleri bulur.
    def solve(self):
        completed=True
        start_over=False
        
        self.update_table()
        for row in self.sudoku_table.values.tolist():
            for cell in row:
                if cell=='#':
                    completed=False
                    break
                
        if completed:
            self.update_table()
            return True
        
        for row in self.solve_table.index:
            for column in self.solve_table.columns:
                if type(self.solve_table.loc[row][column])==type([]):
                    start_over=self.eliminate_possibilities(row,column)

                    if start_over:
                        print('start over')
                        #self.sudoku_table.loc[row][column]=self.solve_table.loc[row][column]
                        self.update_table()
                        return self.solve()
                    
                    #Bir hücrenin hiçbir olası değeri kalmamımşsa hatalı çözüm
                    elif start_over==None:
                        return False
                    
        print('completed eliminating possibilities, starting to assume.')
        print('searching for cell with least possibilities')
        print()
        
        least_cell_row=0
        least_cell_col=0
        least_cell_len=100
        self.update_table()
        for row in self.solve_table.index:
            for column in self.solve_table.columns:
                if type(self.solve_table.loc[row,column])==type([]):
                    temp=len(self.solve_table.loc[row,column])
                    if temp<least_cell_len:
                        least_cell_len=temp
                        least_cell_row=row
                        least_cell_col=column
                        
                        print('new least cell:')
                        print('length:',least_cell_len)
                        print('row:',least_cell_row,'column:',least_cell_col)
                        print()
                        
        for i in self.solve_table.loc[least_cell_row,least_cell_col]:
            print('assuming cell [',least_cell_row,',',least_cell_col,'] with value',i)
            print()
            result,df=self.assume(least_cell_row,least_cell_col,i)
            if result==True:
                self.solve_table=df.copy()
                return True
        
    #Hücrenin alamayacağı değerleri eler.
    def eliminate_possibilities(self,row,column):
        possibilities=self.solve_table.loc[row][column]
        print('for ', str(row), str(column))
        print('column values:',end='')
        #Sütundaki diğer sayıları possibilities'den çıkarır.
        for cell in self.solve_table.loc[:,column].values.tolist():
            print(cell,end=' ')
            if cell in possibilities and type(cell)!=type([]):
                possibilities.remove(cell)
        print()
        print('row values:',end=', ')
        #Satırdaki diğer sayıları possibilities'den çıkarır.
        for cell in self.solve_table.loc[row,:].values.tolist():
            print(cell,end=', ')
            if cell in possibilities and type(cell)!=type([]):
                possibilities.remove(cell)
        print()
        #3x3 kutunun sınırlarını belirler.
        box_top_row,box_bottom_row,box_top_column,box_bottom_column=self.box_indexes(row,column)
        df=self.solve_table.loc[box_bottom_row:box_top_row,box_bottom_column:box_top_column]

        for r in df.values.tolist():
            for cell in r:
                if cell in possibilities:
                    possibilities.remove(cell)
        print('possibilities:',possibilities)
        print()
        print()
        if len(possibilities)==1:
            self.solve_table.loc[row,column]=possibilities[0]
            return True
        
        if len(possibilities)==0:
            return None
        
        return False
    
    def assume(self,row,column,i):
        x=self.solve_table.values.tolist()
        x[row-1][column-1]=i
        for row in range(len(x)):
            for col in range(len(x[row])):
                if type(x[row][col])==type([]):
                    x[row][col]=0
                    
        solver=SudokuSolver(x)
        result=solver.solve()
        return result,solver.solve_table

    #3x3 kutunun sınırlarını hesaplar.
    def box_indexes(self,row,column):
        row=int(row)
        column=int(column)
        
        btr=(int((row-1)/3)+1)*3
        bbr=btr-2
        btc=(int((column-1)/3)+1)*3
        bbc=btc-2

        return btr,bbr,btc,bbc
    
    #sudoku_table'ı solve_table'a göre günceller.
    def update_table(self):
        for row in self.sudoku_table.index:
            for col in self.sudoku_table.columns:
                if type(self.solve_table.loc[row,col])!=type([]):
                    self.sudoku_table.loc[row,col]=self.solve_table.loc[row,col]
    
    def print_table(self):
        print(self.sudoku_table)

    def print_solve_table(self):
        print(self.solve_table)
if __name__=='__main__':
    sudoku1=[#Zor
            [0,0,0,4,0,0,0,8,9],
            [0,4,0,9,0,0,0,6,1],
            [0,5,8,3,0,0,0,0,0],
            [0,0,0,0,0,0,0,9,8],
            [7,0,0,0,1,4,0,0,0],
            [3,0,0,0,7,0,0,0,0],
            [0,2,5,0,0,0,0,0,0],
            [0,0,0,0,0,6,9,2,0],
            [0,0,0,0,0,8,6,0,3]]
    
    sudoku2=[#Kolay
            [2,0,0,0,9,0,0,0,0],
            [0,0,0,0,0,0,0,7,8],
            [7,3,0,0,2,0,0,6,0],
            [0,0,8,0,0,1,6,2,0],
            [0,0,4,0,0,0,3,0,0],
            [0,0,1,2,0,3,0,0,0],
            [0,0,0,0,0,0,4,3,6],
            [0,0,0,8,0,7,0,0,0],
            [5,9,0,0,0,0,0,0,0]]
    
    solver=SudokuSolver(sudoku2)
    result=solver.solve()
    if result==False:
        print('couldnt solve it')
        
    elif result==True:
        print('solved !')
        solver.update_table()
        solver.print_table()
