from common import readcsv,findTrend,top3List,getDailyDiff,getNegativeDaily

def ComputeProfitAndLos(file):
    netprofit = []
    netprofit = readcsv("Profits_and_Loss.csv")
    #dailyDiffList = getDailyCOHDiff(CashOnHand)
    getDailyDiff = getDailyDiff(0,4,netprofit)
    DailyNegList = getNegativeDaily(dailyDiffList)
    trend = findTrend[dailyDiffList]
    #print(trend)
    top3Highest=()
    top3Highest= top5list(dailyDiffList,trend)
    #print(top3Highest)
    
