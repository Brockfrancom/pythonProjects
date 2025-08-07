#hemming distance spell check

def run():
    from minEditDistance import dpMED
    
    maxEditDistance = 0
    maxEditDistancePairs = []
    results = {}
    
    with open('words.txt', 'r') as f:
        for line in f:
            line = line.strip('\n')
            lineSplit = line.split(';')
            lineSplit2 = lineSplit[1].split(',')
            if len(lineSplit2) == 1:
                w1 = len(lineSplit[0]) 
                w2 = len(lineSplit[1])
                res = dpMED(lineSplit[0],lineSplit[1],w1,w2)
                if res > maxEditDistance:
                    maxEditDistance = res
                    maxEditDistancePairs = []
                    maxEditDistancePairs.append((lineSplit[0],lineSplit[1]))
                elif res == maxEditDistance:
                    maxEditDistancePairs.append((lineSplit[0],lineSplit[1]))
                try:
                    results[res] = results[res] + 1
                except Exception:
                    results[res] = 1
            else:
                for i in range(0, len(lineSplit2)):
                    w1 = len(lineSplit[0]) 
                    w2 = len(lineSplit2[i])
                    res = dpMED(lineSplit[0],lineSplit2[i],w1,w2)
                    if res > maxEditDistance:
                        maxEditDistance = res
                        maxEditDistancePairs = []
                        maxEditDistancePairs.append((lineSplit[0],lineSplit2[i]))
                    elif res == maxEditDistance:
                        maxEditDistancePairs.append((lineSplit[0],lineSplit[1]))
                    try:
                        results[res] = results[res] + 1
                    except Exception:
                        results[res] = 1
    f.close()
    
    with open('out.txt', 'w') as f2:   
        best = max(results, key=int)
        print("Edit Distance   Count", file=f2)
        for i in range(0, best+1):
            try:
                print(str(i) + "               " + str(results[i]), file=f2)
            except Exception:
                print(str(i) + "               0", file=f2)
        print("Pairs with the max edit distance:", file=f2)        
        for j in range(0, len(maxEditDistancePairs)):
            print(maxEditDistancePairs[j], file=f2)
    f2.close()    
    
    
    
    
    
    
