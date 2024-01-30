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