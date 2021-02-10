# Min hemming distance algorithm
# 1/28/2020


def MED(A, B, i, j):
    if i==0: #first string is empty, return second string
        return j
    if j==0: #second string is empty, return first string 
        return i
    if i<0 or j<0:
        return 99999999999
    return min(MED(A, B, i-1, j)+1, MED(A, B, i, j-1)+1, (MED(A, B, i-1, j-1)+(A[i-1]!=B[j-1])))

def dpMED(A, B, m, n): 
    C2 = [[0 for x in range(0, n+1)] for y in range(0, m+1)]    
    for i in range(0, m+1): 
        for j in range(0, n+1):   
            #first string is empty, insert second string 
            if i == 0: 
                C2[i][j] = j  
            #second string is empty, insert first string 
            elif j == 0: 
                C2[i][j] = i 
            #characters are same, ignore them and continue
            elif A[i-1] == B[j-1]:
                C2[i][j] = C2[i-1][j-1]   
            #characters are different, find minimum 
            else: 
                C2[i][j] = 1 + min(C2[i][j-1], C2[i-1][j], C2[i-1][j-1])   
    return C2[m][n] 

################################## Testing ###################################
'''
A = "aaadsabedrc"
B = "arwfdsafadsfbd"
i=len(A)
j=len(B)

print(MED(A, B, i,j))

print(dpMED(A, B, i,j))
'''
