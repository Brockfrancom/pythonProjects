#hemming distance dna
# HW4

from minEditDistanceDNA import dpMEDdna

def backtraceToFile(C, A, B, i, j):
    while(True):            
        if (i == 0) and (j == 0):
            return 
        nextVal = max(C[i,j-1], C[i-1,j], C[i-1,j-1])
          
        if C[i-1,j-1] == nextVal:
            if A[i-1] == B[j-1]:
                SC.append((A[i-1], '=', B[j-1]))
            else:
                SC.append((A[i-1], '->', B[j-1]))
            i -=1
            j-=1
            continue    
            #return backtraceToFile(C, A, B, i-1, j-1)

        if C[i-1, j] == nextVal:
            SC.append(('_', '->', B[j-1]))
            i-=1
            continue
            #return backtraceToFile(C, A, B, i-1, j)
        
        elif C[i, j-1] == nextVal:
            SC.append((A[i-1], '->', '_'))
            j-=1
            continue
            #return backtraceToFile(C, A, B, i, j-1)
        else:
            return

################################ Testing #####################################

def run():           
    #Human vs Neandertal test
    with open('Human.txt', 'r') as f:
        line = f.read()
        line1 = line.strip('\n')
        lengthL1 = len(line1)
    f.close()
    with open('Neander.txt', 'r') as m:
        line2 = m.read()
        line2 = line2.strip('\n')
        lengthL2 = len(line2)
    m.close()
    #calculate MED, also return the cache   
    result, cache = dpMEDdna(line1,line2,lengthL1,lengthL2)
    file = 'humanVsNeandertal.txt'
    SC = []
    backtraceToFile(cache,line1,line2,lengthL1,lengthL2)
    with open(file, 'w') as f:
        print("Score: " + str(result), file=f)
        for k in range(len(SC)-1, -1, -1):
            print(SC[k], file=f)
    f.close()
    
    #Human vs Great Ape test
    with open('Human.txt', 'r') as f:
        line = f.read()
        line1 = line.strip('\n')
        lengthL1 = len(line1)
    f.close()
    with open('GreatApe.txt', 'r') as m:
        line2 = m.read()
        line2 = line2.strip('\n')
        lengthL2 = len(line2)
    m.close()
    #calculate MED, also return the cache   
    result, cache = dpMEDdna(line1,line2,lengthL1,lengthL2)
    file = 'humanVsGreatApe.txt'
    SC = []
    backtraceToFile(cache,line1,line2,lengthL1,lengthL2)
    with open(file, 'w') as f:
        print("Score: " + str(result), file=f)
        for k in range(len(SC)-1, -1, -1):
            print(SC[k], file=f)
    f.close()
    
    #Great Ape vs Neandertal test
    with open('GreatApe.txt', 'r') as f:
        line = f.read()
        line1 = line.strip('\n')
        lengthL1 = len(line1)
    f.close()
    with open('Neander.txt', 'r') as m:
        line2 = m.read()
        line2 = line2.strip('\n')
        lengthL2 = len(line2)
    m.close()
    #calculate MED, also return the cache   
    result, cache = dpMEDdna(line1,line2,lengthL1,lengthL2)
    file = 'GreatApeVsNeandertal.txt'
    SC = []
    backtraceToFile(cache,line1,line2,lengthL1,lengthL2)
    with open(file, 'w') as f:
        print("Score: " + str(result), file=f)
        for k in range(len(SC)-1, -1, -1):
            print(SC[k], file=f)
    f.close()
