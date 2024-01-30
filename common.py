from pathlib import Path
# Import csv module
import csv
def readcsv(filename):
    csvdata=[]
#create a path object for text.txt
    file_path = Path.cwd()/"csv.reports"/filename    
