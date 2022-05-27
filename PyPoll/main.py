import os
import csv

csvpath = os.path.join('Resources', 'election_data.csv')
output_path = os.path.join('analysis', 'analysis.txt')
totalvotes = 0
names = []
khan_votes = 0
correy_votes = 0
li_votes = 0
otooley_votes = 0

with open(csvpath) as csvfile:

    csvreader = csv.reader(csvfile, delimiter = ',')
    csv_header = next(csvreader)
    
    for row in csvreader:
        
        totalvotes += 1
        newcandidate = row[2]
        
        if newcandidate not in names:
            names.append(newcandidate)
            
        if newcandidate == "Khan":
            khan_votes += 1
            
        if newcandidate == "Correy":
            correy_votes += 1
            
        if newcandidate == "Li":
            li_votes += 1
            
        if newcandidate == "O'Tooley":
            otooley_votes += 1

khan_percent = (khan_votes/totalvotes)*100
correy_percent = (correy_votes/totalvotes)*100
li_percent = (li_votes/totalvotes)*100
otooley_percent = (otooley_votes/totalvotes)*100

print("Election Results")
print("-------------------------")       
print(f"Total Votes: {totalvotes}")
print("-------------------------")  
print(f"{names[0]}: {khan_percent:.3f}% ({khan_votes})")
print(f"{names[1]}: {correy_percent:.3f}% ({correy_votes})")
print(f"{names[2]}: {li_percent:.3f}% ({li_votes})")
print(f"{names[3]}: {otooley_percent:.3f}% ({otooley_votes})")
print("-------------------------")
print(f"Winner: {names[0]}")
print("-------------------------")

with open(output_path, 'w', newline='') as csvfile:

    csvfile.write("Election Results\n")
    csvfile.write("-------------------------\n")       
    csvfile.write(f"Total Votes: {totalvotes}\n")
    csvfile.write("-------------------------\n")
    csvfile.write(f"{names[0]}: {khan_percent:.3f}% ({khan_votes})\n")
    csvfile.write(f"{names[1]}: {correy_percent:.3f}% ({correy_votes})\n")
    csvfile.write(f"{names[2]}: {li_percent:.3f}% ({li_votes})\n")
    csvfile.write(f"{names[3]}: {otooley_percent:.3f}% ({otooley_votes})\n")
    csvfile.write("-------------------------\n")
    csvfile.write(f"Winner: {names[0]}\n")
    csvfile.write("-------------------------\n")