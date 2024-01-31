from common import readcsv
def CalcHighestOverCat(file):
    OverheadCatlist = []
    OverheadCatList = readcsv("Overheads.csv")

    HighestValue = OverheadCatList.pop()
    for Overhead in OverheadCatList:
        if float(Overhead[1]) > float(HighestValue[1]):
            HighestValue = Overhead
    print(f"[HIGHEST OVERHEAD] {HighestValue[0].upper()}: {HighestValue[1]}%")
    file.write(f"[HIGHEST OVERHEAD] {HighestValue[0].upper()}: {HighestValue[1]}%\n")