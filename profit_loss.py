from common import readcsv,findTrend,top3List,getDailyDiff,getNegativeDaily

def ComputeProfitAndLos(file):
    grossprofit = []
    grossprofit = readcsv("Profits_and_Loss.csv")