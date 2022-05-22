import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')
output_path = os.path.join('analysis', 'analysis.txt')
totalmonths = 0
totalnetamount = 0
previousnet = 0
netchangelist = []
change = 0
max_change = 0
min_change = 0
max_change_month = ""
min_change_month = ""

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        totalmonths += 1
        totalnetamount += int(row[1])

        if totalmonths > 1:
            change = int(row[1]) - previousnet
            netchangelist.append(change)

        previousnet = int(row[1])
        
        if change > max_change:
            max_change = change
            max_change_month = row[0]
            
        if change < min_change:
            min_change = change
            min_change_month = row[0]

            
averagechange = sum(netchangelist)/(totalmonths - 1)

print("Financial Analysis")
print("----------------------------")       
print("Total Months: ", totalmonths)
print("Total: ", totalnetamount)
print("Average Change: ", "$",round(averagechange, 2))
print(f"Greatest Increase in Profits: , max_change_month, (${max_change})")
print(f"Greatest Decrease in Profits: , min_change_month, (${min_change})")

with open(output_path, 'w', newline='') as csvfile:

    csvwriter = csv.writer(csvfile)
    csvfile.write("Financial Analysis")
    csvfile.write("----------------------------")       
    csvfile.write("Total Months: ", totalmonths)
    csvfile.write("Total: ", totalnetamount)
    csvfile.write("Average Change: ", "$",round(averagechange, 2))
    csvfile.write(f"Greatest Increase in Profits: , max_change_month, (${max_change})")
    csvfile.write(f"Greatest Decrease in Profits: , min_change_month, (${min_change})")