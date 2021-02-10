"""
=======================================================
module: dcorr.py
Brock Francom
A02052161
=======================================================
"""
import numpy as np
def direct_corr(f, d):
    """
    Computes direct correlation matrix C b/w fixed and dancer.
    """
    Fnr, Fnc = np.shape(f)
    Dnr, Dnc = np.shape(d)
    C = np.zeros((Fnr+Dnr-1, Fnc+Dnc-1))
    Cnr, Cnc = np.shape(C)  
    #align matricies
    #calculate value
    #insert into C              
    for row in range(0, Cnr):
        for col in range(0, Cnc):
            value = 0
            X = Cnr-row-Fnr
            Y = Cnc-col-Fnc
            # print("X, Y: " + str(X) + ", " + str(Y))
            # print("row, col: " + str(row) + ", " + str(col))
            one = 0
            two = 0
            for y in range(abs(Y), Fnr):
                for x in range(abs(X), Fnc):
                    # print("Value: f["+str(x)+","+str(y)+"] * d["+str(two)+","+str(one)+"]")
                    value += f[x,y] * d[two, one]
                    
                    two += 1
                one += 1
                two = 0
            one = 0
            two = 0     
            C[row, col] = value
    return C


