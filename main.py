from cash_on_hand import readcsv,getDailyDiff,findTrend,top3List
from profit_loss import ComputeProfitAndLos
from cash_on_hand import ComputeCOH
from overheads import CalcHighestOverCat
from pathlib import Path

fw = Path.cwd()/"summary_report.txt"
with fw.open(mode = "w", encoding='UTF-8') as file:
    CalcHighestOverCat(file)
    ComputeCOH(file)
    ComputeProfitAndLos(file)