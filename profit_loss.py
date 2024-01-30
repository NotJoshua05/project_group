from common import readcsv,findTrend,top3List,getDailyDiff,getNegativeDaily

def ComputeProfitAndLos(file):
    netprofit = []
    netprofit = readcsv("Profits_and_Loss.csv")
    #dailyDiffList = getDailyCOHDiff(CashOnHand)
    dailyDiffList= getDailyDiff(0,4,netprofit)
    dailyNegList = getNegativeDaily(dailyDiffList)
    trend = findTrend[dailyDiffList]
    #print(trend)
    top3Highest=()
    top3Highest= top3List(dailyDiffList,trend)
    #print(top3Highest)
    if(trend == "Increasing"):
        print("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY")
        print(f"HIGHEST NET PROFIT SURPLUS] DAY: {top3Highest[0][1]} AMOUNT: SGD{top3Highest[0][0]}")
        file.write("[NET PROFIT SURPLUS] NET PROFIT ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n")
        file.write(f"[HIGHEST NET PROFIT SURPLUS] DAY:{top3Highest[0][1]} AMOUNT: SGD{top3Highest[0][0]}\n")
    elif(trend == "Decreasing"):
        print("[NET PRFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY")
        print(f"[HIGHEST PRFOIT DEFICIT] DAY: {top3Highest[0][1]} AMOUNT: SGD{top3Highest[0][0]}")
        file.write("[NET PROFIT DEFICIT] NET PROFIT ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n")
    elif(trend == "Fluctuating"):
        for item in dailyNegList:
            print(f"[NET PROFIT DEFICIT] DAY: {item[1]} AMOUNT: SGD{item[0]}")
            file.write(f"[NET PROFIT DEFICIT] DAY: {item[1]} AMOUNT: SGD{item[0]}\n")
        print (f"[HIGHEST NET PROFIT DEFICIT] DAY:{top3Highest[0][1]} AMOUNT: SGD{top3Highest[0][0]}")
        print (f"[2ND HIGHEST NET PROFIT DEFICIT] DAY:{top3Highest[1][1]} AMOUNT: SGD{top3Highest[1][0]}")
        print (f"[3RD HIGHEST NET PROFIT DEFICIT] DAY:{top3Highest[2][1]} AMOUNT: SGD{top3Highest[2][0]}")
        print (f"[HIGHEST NET PROFIT DEFICIT] DAY:{top3Highest[0][1]} AMOUNT: SGD{top3Highest[0][0]}\n")
        file.write (f"[2ND HIGHEST NET PROFIT DEFICIT] DAY:{top3Highest[0][1]} AMOUNT: SGD{top3Highest[1][0]}\n")
        file.write (f"[3RD HIGHEST NET PROFIT DEFICIT] DAY:{top3Highest[0][1]} AMOUNT: SGD{top3Highest[2][0]}\n")