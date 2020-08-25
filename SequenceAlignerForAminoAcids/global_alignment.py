class global_aligner():
    def __init__(self,seq1,seq2):
        self.max_score=-99
        self.max_shift=-99
        self.shifted_seq=None

        self.table = [[ 4 , -1 , -2 , -2 ,  0 , -1 , -1 ,  0 , -2 , -1 , -1 , -1 , -1 , -2 , -1 ,  1 ,  0 , -3 , -2 ,  0 , -2 , -1 ,  0],
                 [-1 ,  5 ,  0 , -2 , -3 ,  1 ,  0 , -2 ,  0 , -3 , -2 ,  2 , -1 , -3 , -2 , -1 , -1 , -3 , -2 , -3 , -1 ,  0 , -1],
                 [-2 ,  0 ,  6 ,  1 , -3 ,  0 ,  0 ,  0 ,  1 , -3 , -3 ,  0 , -2 , -3 , -2 ,  1 ,  0 , -4 , -2 , -3 ,  3 ,  0 , -1],
                 [-2 , -2 ,  1 ,  6 , -3 ,  0 ,  2 , -1 , -1 , -3 , -4 , -1 , -3 , -3 , -1 ,  0 , -1 , -4 , -3 , -3 ,  4 ,  1 , -1],
                 [ 0 , -3 , -3 , -3 ,  9 , -3 , -4 , -3 , -3 , -1 , -1 , -3 , -1 , -2 , -3 , -1 , -1 , -2 , -2 , -1 , -3 , -3 , -2],
                 [-1 ,  1 ,  0 ,  0 , -3 ,  5 ,  2 , -2 ,  0 , -3 , -2 ,  1 ,  0 , -3 , -1 ,  0 , -1 , -2 , -1 , -2 ,  0 ,  3 , -1],
                 [-1 ,  0 ,  0 ,  2 , -4 ,  2 ,  5 , -2 ,  0 , -3 , -3 ,  1 , -2 , -3 , -1 ,  0 , -1 , -3 , -2 , -2 ,  1 ,  4 , -1],
                 [ 0 , -2 ,  0 , -1 , -3 , -2 , -2 ,  6 , -2 , -4 , -4 , -2 , -3 , -3 , -2 ,  0 , -2 , -2 , -3 , -3 , -1 , -2 , -1],
                 [-2 ,  0 ,  1 , -1 , -3 ,  0 ,  0 , -2 ,  8 , -3 , -3 , -1 , -2 , -1 , -2 , -1 , -2 , -2 ,  2 , -3 ,  0 ,  0 , -1],
                 [-1 , -3 , -3 , -3 , -1 , -3 , -3 , -4 , -3 ,  4 ,  2 , -3 ,  1 ,  0 , -3 , -2 , -1 , -3 , -1 ,  3 , -3 , -3 , -1],
                 [-1 , -2 , -3 , -4 , -1 , -2 , -3 , -4 , -3 ,  2 ,  4 , -2 ,  2 ,  0 , -3 , -2 , -1 , -2 , -1 ,  1 , -4 , -3 , -1],
                 [-1 ,  2 ,  0 , -1 , -3 ,  1 ,  1 , -2 , -1 , -3 , -2 ,  5 , -1 , -3 , -1 ,  0 , -1 , -3 , -2 , -2 ,  0 ,  1 , -1],
                 [-1 , -1 , -2 , -3 , -1 ,  0 , -2 , -3 , -2 ,  1 ,  2 , -1 ,  5 ,  0 , -2 , -1 , -1 , -1 , -1 ,  1 , -3 , -1 , -1],
                 [-2 , -3 , -3 , -3 , -2 , -3 , -3 , -3 , -1 ,  0 ,  0 , -3 ,  0 ,  6 , -4 , -2 , -2 ,  1 ,  3 , -1 , -3 , -3 , -1],
                 [-1 , -2 , -2 , -1 , -3 , -1 , -1 , -2 , -2 , -3 , -3 , -1 , -2 , -4 ,  7 , -1 , -1 , -4 , -3 , -2 , -2 , -1 , -2],
                 [ 1 , -1 ,  1 ,  0 , -1 ,  0 ,  0 ,  0 , -1 , -2 , -2 ,  0 , -1 , -2 , -1 ,  4 ,  1 , -3 , -2 , -2 ,  0 ,  0 ,  0],
                 [ 0 , -1 ,  0 , -1 , -1 , -1 , -1 , -2 , -2 , -1 , -1 , -1 , -1 , -2 , -1 ,  1 ,  5 , -2 , -2 ,  0 , -1 , -1 ,  0],
                 [-3 , -3 , -4 , -4 , -2 , -2 , -3 , -2 , -2 , -3 , -2 , -3 , -1 ,  1 , -4 , -3 , -2 , 11 ,  2 , -3 , -4 , -3 , -2],
                 [-2 , -2 , -2 , -3 , -2 , -1 , -2 , -3 ,  2 , -1 , -1 , -2 , -1 ,  3 , -3 , -2 , -2 ,  2 ,  7 , -1 , -3 , -2 , -1],
                 [ 0 , -3 , -3 , -3 , -1 , -2 , -2 , -3 , -3 ,  3 ,  1 , -2 ,  1 , -1 , -2 , -2 ,  0 , -3 , -1 ,  4 , -3 , -2 , -1],
                 [-2 , -1 ,  3 ,  4 , -3 ,  0 ,  1 , -1 ,  0 , -3 , -4 ,  0 , -3 , -3 , -2 ,  0 , -1 , -4 , -3 , -3 ,  4 ,  1 , -1],
                 [-1 ,  0 ,  0 ,  1 , -3 ,  3 ,  4 , -2 ,  0 , -3 , -3 ,  1 , -1 , -3 , -1 ,  0 , -1 , -3 , -2 , -2 ,  1 ,  4 , -1],
                 [ 0 , -1 , -1 , -1 , -2 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -1 , -2 ,  0 ,  0 , -2 , -1 , -1 , -1 , -1 , -1]]

        self.alphabet = ['A', 'R', 'N', 'D', 'C', 'Q', 'E', 'G', 'H', 'I', 'L', 'K', 'M', 'F', 'P', 'S', 'T', 'W', 'Y', 'V', 'B', 'Z', 'X']
        
        self.seq1=seq1.upper()
        self.seq2=seq2.upper()
        

    def score_shift_seq1(self,shift): #shift seq1'nin kaç index kayacağını belirtir.
        total_score = 0

        for i in range(len(self.seq1)):
            if i + shift >= len(self.seq2):
                break

            total_score += self.find_matrix_score(self.seq1[i], self.seq2[i+shift])
            #print("shift : " + str(shift) + " - " + self.seq1[i] + " " + self.seq2[i+shift] + " " + str(self.find_matrix_score(self.seq1[i], self.seq2[i+shift])))
        if total_score > self.max_score:
            self.max_score = total_score
            self.max_shift = shift
            self.shifted_seq = 1
            

    def score_shift_seq2(self,shift): #shift seq2'nin kaç index kayacağını belirtir.
        total_score = 0
            
        for i in range(len(self.seq2)):
            if i + shift >= len(self.seq1):
                break

            total_score += self.find_matrix_score(self.seq1[i+shift], self.seq2[i])
            #print("shift : " + str(shift) + " - " + self.seq1[i+shift] + " " + self.seq2[i] + " " + str(self.find_matrix_score(self.seq1[i], self.seq2[i+shift])))
        if total_score > self.max_score:
            self.max_score = total_score
            self.max_shift = shift
            self.shifted_seq = 2


    def find_matrix_score(self,aa1,aa2):
        aa1_index = None
        aa2_index = None
           
        for i in range(len(self.alphabet)):
            if aa1 == self.alphabet[i]:
                aa1_index = i
            if aa2 == self.alphabet[i]:
                aa2_index = i

            if aa1_index != None and aa2_index != None:
                break
                
        if aa1_index == None:
            raise Exception("Couldnt find amino acid \'" + aa1 + "\' in alphabet.")
        if aa2_index == None:
            raise Exception("Couldnt find amino acid \'" + aa2 + "\' in alphabet.")
                
        return self.table[aa1_index][aa2_index]

    def results(self):
        if self.shifted_seq==1:
            for i in range(self.max_shift):
                self.seq1='-'+self.seq1
        else:
            for i in range(self.max_shift):
                self.seq2='-'+self.seq2
                
        return self.seq1, self.seq2, self.max_score

    def run(self):
#        print("Shifting Sequence 1 : " + self.seq1)    
        for i in range(len(self.seq1)):
            self.score_shift_seq1(i)
# =============================================================================
#         print("\nMax Score : " + str(self.max_score) + " , Shift : " + str(self.max_shift))
#         print("------------------------------------------------------------------")
#         print("Shifting Sequence 2 : " + self.seq2)
# =============================================================================
        for i in range(len(self.seq2)):
            self.score_shift_seq2(i)
#        print("\nMax Score : " + str(self.max_score) + " , Shift : " +  str(self.max_shift))

        return self.results()

            
        
