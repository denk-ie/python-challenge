import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('analysis', 'analysis.txt')

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    
    csv_header = next(csvreader)
    
    totalmonths = sum(1 for row in csvreader)
    
    totalprofitloss = sum(1 for column[2] in csvreader)
    
    
with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile)

    csvwriter.writerow("Financial Analysis")

    csvwriter.writerow("----------------------------")
    
    csvwriter.writerow("Total Months: ", totalmonths)

#print("Financial Analysis")
#print("----------------------------")    
#print("Total Months: ", totalmonths)
#print("Total: $", totalprofitloss)
#print("Average Change: ")
#print("Greatest Increase in Profits: ")
#print("Greatest Decrease in Profits: ")