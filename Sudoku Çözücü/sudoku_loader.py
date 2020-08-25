import pickle

class SudokuLoader():
    def __init__(self):
        self.sudoku=None
        self.file=None
        
    def load_from(self,filename):
        self.file=open(filename,'rb')
        self.sudoku=pickle.load(self.file)
        self.file.close()
        
    def save_to(self,filename):
        self.file=open(filename,'wb')
        pickle.dump(self.sudoku,self.file)
        self.file.close()
        
    def get_sudoku(self,filename):
        self.load_from(filename)
        return self.sudoku
    
if __name__=='__main__':
    loader=SudokuLoader()
    filename='takvim-sudoku1.sudoku'
    loader.sudoku=[[4,0,9,0,6,0,8,2,0],
                   [0,0,7,0,0,8,0,4,0],
                   [5,0,0,9,0,0,1,0,0],
                   [7,0,0,0,2,9,0,8,1],
                   [8,3,5,0,0,0,0,0,9],
                   [0,0,0,0,0,6,0,0,0],
                   [0,0,1,0,0,2,0,0,4],
                   [0,7,0,4,9,0,0,5,0],
                   [0,8,0,0,0,0,3,0,2]
                   ]
    for row in loader.sudoku:
        print(row)
    
    loader.save_to(filename)