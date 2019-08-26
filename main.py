# Modules
import os
import csv
#Initialization 
candidates =[]
votes = []
# Set path for file
csvpath = os.path.join("election_data.csv")
# Open the CSV
with open(csvpath, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvreader)
    # Loop through the data 
    for row in csvreader:
        # Appending unique candidates in the list and their corresponding vote-count tally list initializing it with zero
        if row[2] not in candidates:
            candidates.append(row[2])
            votes.append(0)
        # If row match the candidates, increment the corresponding vote-count tally list
        if row[2] in candidates:
            index = candidates.index(row[2])
            votes[index] = votes[index] + 1

# Finding total number of candidates 
num_candidates = len(candidates)

print(" Election Results\n")
print("------------------------------------\n")
print(f" Total Votes : {sum(votes)}\n")
print("------------------------------------\n")

for i in range(num_candidates):
    percent_votes = (votes[i]/sum(votes))*100
    print(f"{candidates[i]}: "+"{:.2f}".format(percent_votes)+"% ("+f"{votes[i]})"+"\n")

winner_index = votes.index(max(votes))
print("------------------------------------\n")
print(f" Winner: {candidates[winner_index]}\n")
print("------------------------------------\n")

# Specify the file to write to
output_path = os.path.join( "analysis.txt")

# Open the file using "write" mode. Specify the variable to hold the contents
with open(output_path, 'w', newline='') as datafile:
    datafile.write(" Election Results\n")
    datafile.write("------------------------------------\n")
    datafile.write(f" Total Votes : {sum(votes)}\n")
    datafile.write("------------------------------------\n")

    for i in range(num_candidates):
        
        datafile.write(f"{candidates[i]}: "+"{:.2f}".format(percent_votes)+"% ("+f"{votes[i]})"+"\n")


    datafile.write("------------------------------------\n")
    datafile.write(f" Winner: {candidates[winner_index]}\n")
    datafile.write("------------------------------------\n")