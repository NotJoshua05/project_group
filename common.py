from pathlib import Path
# Import csv module
import csv
def readcsv(filename):
    csvdata=[]
#create a path object for text.txt
    file_path = Path.cwd()/"csv.reports"/filename
# open file with .open() to return a file object
# create 'reader' object and print line if file path exists
    with file_path.open(mode = "r", encoding='UTF-8') as file:
# instantiate a reader object
        reader = csv.reader(file)
        next(reader)
        for line in reader:
            csvdata.append(line)
            #print(line)
        return csvdata

def getDailyDiff(c1, c2,cohlist):
    '''
    this function will return a list
    that contain list of [dailydiff, day]
    '''
    dailyList = []
    prevCoh = 0
    row =0
    for item in cohlist:
        if row == 0:                        
            diff = 0
        else:
            diff = float(item[c2])-prevCoh
            #insert diff first so that can use list sort later to find top3
            dailyList.append( [int(diff),item[c1]])
            
        prevCoh = float(item[c2])
        #print(item[c1]," diff: ", diff)
        
        row +=1
    return dailyList


def findTrend(dailyChgList):
    DecCount = 0
    IncCount = 0
    zeroCount = 0
    for dailyChg,day in dailyChgList:
        if(dailyChg <0):
            DecCount +=1
        elif(dailyChg >0):
            IncCount +=1
        else:
            zeroCount +=1
    if(IncCount>0 and DecCount==0 and zeroCount==0 ):
        return "Increasing"
    elif(IncCount==0 and DecCount>0 and zeroCount==0 ):
        return "Decreasing"
    #10 10 10 0 0 0 
    #10 10 10 -10 -10
    elif(IncCount>0 and (DecCount >0 or zeroCount>0) ):
        return "Fluctuating"
    #-10 -10 -10 0 0 0 
    #10 10 10 -10 -10
    elif( (IncCount>0 or zeroCount >0)and DecCount >0 ):
        return "Fluctuating"
    else:
        return "Undefined"

def top3List(dflist,trnd):
    sortlist =[]
    if(trnd == "Fluctuating" or trnd == "Decreasing"):        
        dflist.sort()
        for idx in range(3):
            sortlist.append([dflist[idx][0]*-1,dflist[idx][1]])
    elif(trnd == "Increasing"):
        dflist.sort(reverse=True)
        for idx in range(3):
            sortlist.append(dflist[idx])

    return sortlist

def getNegativeDaily(ddlist):
    dNegList=[]
    for item in ddlist:
        if int(item[0])<0:
            dNegList.append([int(item[0])*-1,item[1]])
    return dNegList