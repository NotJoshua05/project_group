from common import readcsv, getDailyDiff, findTrend, getNegativeDaily, top3List
def ComputeCOH(file):
    CashOnHand = []
    CashOnHand = readcsv("Cash_On_Hand.csv")
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
        print(f'[HIGHEST CASH SURPLUS] DAY: {top3Highest[0][1]}, AMOUNT: SGD{top3Highest[0][0]}')
        file.write('[CASH SURPLUS] CASH ON EACH DAY IS HIGHER THAN THE PREVIOUS DAY\n')
        file.write(f'[HIGHEST CASH SURPLUS] DAY: {top3Highest[0][1]}, AMOUNT: SGD{top3Highest[0][0]}\n')
    elif(trend == "Decreasing"):
        print('[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY')
        print(f'[HIGHEST CASH DEFICIT] DAY: {top3Highest[0][1]}, AMOUNT: {top3Highest[0][0]}')
        file.write('[CASH DEFICIT] CASH ON EACH DAY IS LOWER THAN THE PREVIOUS DAY\n')
        file.write(f'[HIGHEST CASH DEFICIT] DAY: {top3Highest[0][1]}, AMOUNT: SGD{top3Highest[0][0]}\n')
    elif(trend == "Fluctuating"):
        for item in dailyNegList:
            print(f'[CASH DEFICIT] DAY:{item[1]}, AMOUNT: SGD{item[0]}')
            file.write(f'[CASH DEFICIT] DAY:{item[1]}, AMOUNT: SGD{item[0]}\n')
        print(f'[HIGHEST CASH DEFICIT] DAY:{top3Highest[0][1]}, AMOUNT: SGD{top3Highest[0][0]}')
        print(f'[2ND HIGHEST CASH DEFICIT] DAY:{top3Highest[1][1]}, AMOUNT: SGD{top3Highest[1][0]}')
        print(f'[3RD HIGHEST CASH DEFICIT] DAY:{top3Highest[2][1]}, AMOUNT: SGD{top3Highest[2][0]}')
        file.write(f'[HIGHEST CASH DEFICIT] DAY:{top3Highest[0][1]}, AMOUNT: SGD{top3Highest[0][0]}\n')
        file.write(f'[2ND HIGHEST CASH DEFICIT] DAY:{top3Highest[1][1]}, AMOUNT: SGD{top3Highest[1][0]}\n')
        file.write(f'[3RD HIGHEST CASH DEFICIT] DAY:{top3Highest[2][1]}, AMOUNT: SGD{top3Highest[2][0]}\n')