from common import readcsv, getDailyDiff, findTrend, getNegativeDaily, top3List
def ComputCOH(file):
    CashOnHand = []
    CashOnHand = readcsv("Cash-On-Hand.csv")
    #dailyDiffList = getDailyCOHDiff(CashOnHand)
    dailyDiffList = getDailyDiff(0, 1, CashOnHand)
    trend = findTrend(dailyDiffList)
    #print(trend)
    dailyNegList = getNegativeDaily(dailyDiffList)
    top3Highest = []
    top3Highest = top3List(dailyDiffList, trend)
    #print(top3Highest)
    #for item in top3Highest:
        #print("day:",item[1],"diff:",item[0])
    if(trend == "Increasing"):
        print('[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY')
        print(f'[HIGHEST CASH SURPLUS] DAY: {top3Highest[0][1]} AMOUNT: SGD{top3Highest[0][0]}')
        file.write('[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        file.write(f'[HIGHEST CASH SURPLUS] DAY: {top3Highest[0][1]} AMOUNT: SGD{top3Highest[0][0]}\n')