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
print(f"Average Change: ${averagechange:.2f}")
print(f"Greatest Increase in Profits: {max_change_month} (${max_change})")
print(f"Greatest Decrease in Profits: {min_change_month} (${min_change})")

with open(output_path, 'w', newline='') as csvfile:

    csvfile.write("Financial Analysis\n")
    csvfile.write("----------------------------\n")       
    csvfile.write(f"Total Months: {totalmonths} \n")
    csvfile.write(f"Total:  ${totalnetamount} \n")
    csvfile.write(f"Average Change:  ${averagechange:.2f} \n")
    csvfile.write(f"Greatest Increase in Profits: {max_change_month} (${max_change}) \n")
    csvfile.write(f"Greatest Decrease in Profits: {min_change_month} (${min_change}) \n")