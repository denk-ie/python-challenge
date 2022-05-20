import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('analysis', 'analysis.txt')

print("Financial Analysis")
print("----------------------------")

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    
    csv_header = next(csvreader)
    
    #for row in csvreader: