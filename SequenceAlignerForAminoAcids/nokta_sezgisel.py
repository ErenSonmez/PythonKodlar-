import pandas as pd

k=0

def get_input():
    
    global k
    
    seq1=input("Sequence 1 : ")
    seq2=input("Sequence 2 : ")
    k=int(input("k must be equal or greater than : "))
    
    seq1=list(seq1.upper())
    seq2=list(seq2.upper())
    
    df=pd.DataFrame(index=seq2,columns=seq1)
    df.fillna('-',inplace=True)
    
    return df

def find_matches(score_matrix):
    
    rows=list(score_matrix.index)
    columns=list(score_matrix.columns)

    matches=[]

    for i in range(1,len(rows)):
        for j in range(1,len(columns)):
            if rows[i]==columns[j]:
                matches.append([i,j])
                score_matrix.iloc[i][j]='*'

    return matches

def find_diagonals(score_matrix,matches):
    
    global k

    match_point=None
    diagonals=[]
    for i in matches:
        row=i[0]
        column=i[1]
        found_diagonals=0
        while 1:
            if row+1==len(score_matrix.index) or column+1==len(score_matrix.columns):
                break
            
            row=row+1
            column=column+1
            
            if score_matrix.iloc[row][column]=='*':
                found_diagonals=found_diagonals+1
            else:
                break
        if found_diagonals>=k:
            diagonals.append([[i[0],i[1]],[row-1,column-1]])

            
    return diagonals

score_matrix=get_input()
matches=find_matches(score_matrix)
print(score_matrix)
print("Matches : ")
print(matches)
diagonals=find_diagonals(score_matrix,matches)
print("Diagonals : ")
print(diagonals)

