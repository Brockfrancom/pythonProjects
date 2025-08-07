def makeNumberPyramid(num):
    numDigits = len(str(num))
    numCharsInRow = ((numDigits+1)*num)-1
    output = ""
    for i in range(1,num+1):
        s = ""
        for j in range(0,i):
            s += str(i)+" "
        output += ('{:^'+str(numCharsInRow)+'}').format(s.strip())+'\n'
    return output

if __name__ == "__main__":
    num = int(input("Enter the number of rows: "))
    output = makeNumberPyramid(num)
    print(output)
