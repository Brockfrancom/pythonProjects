"""
Brock Francom
A02052161
CS-1440
Erik Falor
9/20/2018
2: The right data structure for the job
"""
from Report import Report
import sys
rpt = Report( )

#functions used to sort lists
def getElement10(lst):
    return int(lst[10])
def getElement8(lst):
    return int(lst[8])
def getElement9(lst):
    return int(lst[9])

#find the FIPS code for Cache County, Utah
area = "Cache County, Utah"
with open(sys.argv[1] + "/area_titles.csv") as f:
    pattern = area
    for line in f:
        if pattern in line:
            line = line.rstrip()
            field = line.split("\",\"")
            cache = field[0].strip("\"")
            
#open file and select lines to include(all industries)
with open(sys.argv[1] + "/2017.annual.singlefile.csv") as f:
    delim = ","
    first_line = f.readline()
    allData = []
    for line in f:
        line = line.rstrip()
        field = line.split(delim)
        if field[1] == '"0"' and field[2] == '"10"':
            allData.append(field)
#further refine data, removing duplicate areas            
while True:
    length = len(allData)
    i = 0
    for row in allData:
        if allData[i][0].strip("\'").strip("\"").startswith("C"):
            allData.pop(i)
            i -= 1
        if allData[i][0].strip("\'").strip("\"").startswith("U"):
            allData.pop(i)
            i -= 1
        if allData[i][0].strip("\'").strip("\"").startswith("M"):
            allData.pop(i)
            i -= 1
        if allData[i][0].strip("\'").strip("\"").endswith("000"):
            allData.pop(i)
            i -= 1
        i += 1
    if length == len(allData):
        break

#create a list and find the gross annual wages
totalAnnualWagesList = []
i = 0
for row in allData:
    totalAnnualWagesList.append(int(allData[i][10]))
    i += 1       
totalAnnualWages = 0
for i in totalAnnualWagesList:
    totalAnnualWages += i    
copyTotalAnnualWagesList = totalAnnualWagesList.copy() 

#find the unique wages
uniqueWages = []
i = 0
for row in totalAnnualWagesList:
    totalAnnualWagesList.pop(i)
    if row in totalAnnualWagesList:
        totalAnnualWagesList.insert(i, row)
        i += 1
    else:
        uniqueWages.append(row)
        totalAnnualWagesList.insert(i, row)
        i += 1

#find the distinct wages          
distinctWages = []
i = 0
for row in totalAnnualWagesList:
    if totalAnnualWagesList[i] not in distinctWages:
        distinctWages.append(totalAnnualWagesList[i])
        i += 1
    else:
        i += 1        
 
#find the gross number of establishments
numOfEstList = []
i = 0
for row in allData:
    numOfEstList.append(int(allData[i][8]))
    i += 1        
numOfEst = 0
for i in numOfEstList:
    numOfEst += i    
copyNumOfEstList = numOfEstList.copy()

#find the unique # of establishments    
uniqueEst = []
i = 0
for row in numOfEstList:
    numOfEstList.pop(i)
    if row in numOfEstList:
        numOfEstList.insert(i, row)
        i += 1
    else:
        uniqueEst.append(row)
        numOfEstList.insert(i, row)
        i += 1

#find the distinct # of establishments          
distinctEst = []
i = 0
for row in numOfEstList:
    if numOfEstList[i] not in distinctEst:
        distinctEst.append(numOfEstList[i])
        i += 1
    else:
        i += 1
                        
#find the gross annual employment level    
emplList = []
i = 0
for row in allData:
    emplList.append(int(allData[i][9]))
    i += 1
empl = 0
for i in emplList:
    empl += i
copyEmplList = emplList.copy()

#find the unique employment levels 
uniqueEmpl = []
i = 0
for row in emplList:
    emplList.pop(i)
    if row in emplList:
        emplList.insert(i, row)
        i += 1
    else:
        uniqueEmpl.append(row)
        emplList.insert(i, row)
        i += 1

#find the distinct employment levels           
distinctEmpl = []
i = 0
for row in emplList:
    if emplList[i] not in distinctEmpl:
        distinctEmpl.append(emplList[i])
        i += 1
    else:
        i += 1

#sort the list for wages        
testList1 = sorted(allData, key=getElement10, reverse=True)
a = 0
i = 0
while True:
    if "\"" + cache + "\"" == testList1[i][0]:
        a = i
        break
    else:
        i += 1
#sort the list for # of establishments
testList2 = sorted(allData, key=getElement8, reverse=True)
b = 0
i = 0
while True:
    if "\"" + cache + "\"" == testList2[i][0]:
        b = i
        break
    else:
        i += 1
#sort the list for employment
testList3 = sorted(allData, key=getElement9, reverse=True)
c = 0
i = 0
while True:
    if "\"" + cache + "\"" == testList3[i][0]:
        c = i
        break
    else:
        i += 1
    
#open file and select lines to include(software industry)
with open(sys.argv[1] + "/2017.annual.singlefile.csv") as f:
    delim = ","
    first_line = f.readline()
    softData = []
    for line in f:
        line = line.rstrip()
        field = line.split(delim)
        if field[1] == '"5"' and field[2] == '"5112"':
            softData.append(field)
#further refine data, removing duplicate areas                      
while True:
    length2 = len(softData)
    i = 0
    for row in softData:
        if softData[i][0].strip("\'").strip("\"").startswith("C"):
            softData.pop(i)
            i -= 1
        if softData[i][0].strip("\'").strip("\"").startswith("U"):
            softData.pop(i)
            i -= 1
        if softData[i][0].strip("\'").strip("\"").startswith("M"):
            softData.pop(i)
            i -= 1
        if softData[i][0].strip("\'").strip("\"").endswith("000"):
            softData.pop(i)
            i -= 1
        i += 1
    if length2 == len(softData):
        break

#find the gross annual wages
totalAnnualWagesList = []
i = 0
for row in softData:
    totalAnnualWagesList.append(int(softData[i][10]))
    i += 1
totalAnnualWages2 = 0
for i in totalAnnualWagesList:
    totalAnnualWages2 += i    
copyTotalAnnualWagesList = totalAnnualWagesList.copy()

#find the unique wages    
uniqueWages2 = []
i = 0
for row in totalAnnualWagesList:
    totalAnnualWagesList.pop(i)
    if row in totalAnnualWagesList:
        totalAnnualWagesList.insert(i, row)
        i += 1
    else:
        uniqueWages2.append(row)
        totalAnnualWagesList.insert(i, row)
        i += 1

#find the distinct wages          
distinctWages2 = []
i = 0
for row in totalAnnualWagesList:
    if totalAnnualWagesList[i] not in distinctWages2:
        distinctWages2.append(totalAnnualWagesList[i])
        i += 1
    else:
        i += 1

#find the gross number of establishments
numOfEstList = []
i = 0
for row in softData:
    numOfEstList.append(int(softData[i][8]))
    i += 1        
numOfEst2 = 0
for i in numOfEstList:
    numOfEst2 += i    
copyNumOfEstList = numOfEstList.copy()        
 
#find the unique # of establishments    
uniqueEst2 = []
i = 0
for row in numOfEstList:
    numOfEstList.pop(i)
    if row in numOfEstList:
        numOfEstList.insert(i, row)
        i += 1
    else:
        uniqueEst2.append(row)
        numOfEstList.insert(i, row)
        i += 1

#find the distinct # of establishments          
distinctEst2 = []
i = 0
for row in numOfEstList:
    if numOfEstList[i] not in distinctEst2:
        distinctEst2.append(numOfEstList[i])
        i += 1
    else:
        i += 1
        
#find the gross annual employment level                    
emplList = []
i = 0
for row in softData:
    emplList.append(int(softData[i][9]))
    i += 1
empl2 = 0
for i in emplList:
    empl2 += i
copyEmplList = emplList.copy()

#find the unique employment levels 
uniqueEmpl2 = []
i = 0
for row in emplList:
    emplList.pop(i)
    if row in emplList:
        emplList.insert(i, row)
        i += 1
    else:
        uniqueEmpl2.append(row)
        emplList.insert(i, row)
        i += 1

#find the distinct employment levels           
distinctEmpl2 = []
i = 0
for row in emplList:
    if emplList[i] not in distinctEmpl2:
        distinctEmpl2.append(emplList[i])
        i += 1
    else:
        i += 1

#sort the list for wages
testList4 = sorted(softData, key=getElement10, reverse=True)
d = 0
i = 0
while True:
    if "\"" + cache + "\"" == testList4[i][0]:
        d = i
        break
    else:
        i += 1
#sort the list for # of establishments
testList5 = sorted(softData, key=getElement8, reverse=True)
e = 0
i = 0
while True:
    if "\"" + cache + "\"" == testList5[i][0]:
        e = i
        break
    else:
        i += 1
#sort the list for employment
testList6 = sorted(softData, key=getElement9, reverse=True)
g = 0
i = 0
while True:
    if "\"" + cache + "\"" == testList6[i][0]:
        g = i
        break
    else:
        i += 1

#create 1st list of top 5
topFive1 = []
i = 0
while i < 5:
    area = testList1[i][0]
    with open(sys.argv[1] + "/area_titles.csv") as f:
            pattern = area
            for line in f:
                if pattern in line:
                    line = line.rstrip()
                    field = line.split("\",\"")
                    area1 = field[1].strip("\"")
                    topFive1.append([area1, int(testList1[i][10])])
                    i += 1
#create 2nd list of top 5
topFive2 = []
i = 0
while i < 5:
    area = testList2[i][0]
    with open(sys.argv[1] + "/area_titles.csv") as f:
            pattern = area
            for line in f:
                if pattern in line:
                    line = line.rstrip()
                    field = line.split("\",\"")
                    area1 = field[1].strip("\"")
                    topFive2.append([area1, int(testList2[i][8])])
                    i += 1
#create 3rd list of top 5
topFive3 = []
i = 0
while i < 5:
    area = testList3[i][0]
    with open(sys.argv[1] + "/area_titles.csv") as f:
            pattern = area
            for line in f:
                if pattern in line:
                    line = line.rstrip()
                    field = line.split("\",\"")
                    area1 = field[1].strip("\"")
                    topFive3.append([area1, int(testList3[i][9])])
                    i += 1
#create 4th list of top 5
topFive4 = []
i = 0
while i < 5:
    area = testList4[i][0]
    with open(sys.argv[1] + "/area_titles.csv") as f:
            pattern = area
            for line in f:
                if pattern in line:
                    line = line.rstrip()
                    field = line.split("\",\"")
                    area1 = field[1].strip("\"")
                    topFive4.append([area1, int(testList4[i][10])])
                    i += 1
#create 5th list of top 5
topFive5 = []
i = 0
while i < 5:
    area = testList5[i][0]
    with open(sys.argv[1] + "/area_titles.csv") as f:
            pattern = area
            for line in f:
                if pattern in line:
                    line = line.rstrip()
                    field = line.split("\",\"")
                    area1 = field[1].strip("\"")
                    topFive5.append([area1, int(testList5[i][8])])
                    i += 1
#create 6th list of top 5
topFive6 = []
i = 0
while i < 5:
    area = testList6[i][0]
    with open(sys.argv[1] + "/area_titles.csv") as f:
            pattern = area
            for line in f:
                if pattern in line:
                    line = line.rstrip()
                    field = line.split("\",\"")
                    area1 = field[1].strip("\"")
                    topFive6.append([area1, int(testList6[i][9])])
                    i += 1
                           
#change all the data fields to match the program results.
rpt.all.count                    = length

rpt.all.total_pay                = totalAnnualWages
rpt.all.unique_pay               = len(uniqueWages)
rpt.all.distinct_pay             = len(distinctWages)
rpt.all.per_capita_avg_wage      = totalAnnualWages / empl
rpt.all.cache_co_pay_rank        = a + 1

rpt.all.total_estab              = numOfEst
rpt.all.unique_estab             = len(uniqueEst)
rpt.all.distinct_estab           = len(distinctEst)
rpt.all.cache_co_estab_rank      = b + 1

rpt.all.total_empl               = empl
rpt.all.unique_empl              = len(uniqueEmpl)
rpt.all.distinct_empl            = len(distinctEmpl)
rpt.all.cache_co_empl_rank       = c + 1

rpt.all.top_annual_wages         = topFive1
rpt.all.top_annual_estab         = topFive2
rpt.all.top_annual_avg_emplvl    = topFive3

rpt.soft.count                   = length2

rpt.soft.total_pay               = totalAnnualWages2
rpt.soft.unique_pay              = len(uniqueWages2)
rpt.soft.distinct_pay            = len(distinctWages2)
rpt.soft.per_capita_avg_wage     = totalAnnualWages2 / empl2
rpt.soft.cache_co_pay_rank       = d + 1

rpt.soft.total_estab             = numOfEst2
rpt.soft.unique_estab            = len(uniqueEst2)
rpt.soft.distinct_estab          = len(distinctEst2)
rpt.soft.cache_co_estab_rank     = e + 1

rpt.soft.total_empl              = empl2
rpt.soft.unique_empl             = len(uniqueEmpl2)
rpt.soft.distinct_empl           = len(distinctEmpl2)
rpt.soft.cache_co_empl_rank      = g + 1

rpt.soft.top_annual_wages        = topFive4
rpt.soft.top_annual_estab        = topFive5
rpt.soft.top_annual_avg_emplvl   = topFive6

#print the report
print(rpt)
