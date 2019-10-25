# Define Variables
import os
import csv

csvpath = os.path.join('..','Resources', 'election_data.csv')
pyPoll_out_path = os.path.join('..','Output', 'pyPoll_out_file.csv')

vote_counter = 0 #Counter for each vote
total_votes = 0 #Sum of votes
candidate_votes_cnt = 0 #Sum of votes per candidate
candidate_votes_pct = 0 #Percentage of votes per candidate
my_cvs_array = []
my_candidates = []
my_voter_results = [0,0,0,0]
my_percentage_of_votes = [0.00,0.00,0.00,0.00]
max_votes = 0
winner = "TBD"

#Read all records from csv into imported_csv_table
with open(csvpath, newline='') as cvsfile:
    csvreader = csv.reader(cvsfile, delimiter=',')
    csv_header = next(csvreader)
    print(csv_header)

    # Read each row of data after the header
    for row in csvreader:
        my_cvs_array.append(row)

#Loop through the array and update Variables
#Per candidate, summarize the number of votes
#Append results to votes_summary_table
i = 0
for row in my_cvs_array:
    total_votes = total_votes + 1
    if not row[2] in my_candidates:
        my_candidates.append(row[2])
        #my_candidates.index(i).append(row[2])
print(my_candidates)

#Determine number of votes
i = 0
my_length = len(my_candidates)

for row in my_cvs_array:
    for i in range(0,my_length):
        if row[2] == my_candidates[i]:
            choice_index = i
            my_voter_results[choice_index] += 1

#Lastly determine Percentage of total votes and 'winner'
i = 0
for i in range(0,my_length):
    my_percentage_of_votes[i] = my_voter_results[i]/total_votes*100
    if my_voter_results[i] >= max_votes:
        max_votes=my_voter_results[i]
        winner=my_candidates[i]

#Print outcome to screen
print("*************************************************")
print("Election Results")
print("-------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------------------------")
for i in range(0, my_length): #print(votes_summary_table)
    print(f"{my_candidates[i]}: {my_percentage_of_votes[i]:.3f}%  ({my_voter_results[i]})" )
print("-------------------------------------------------")
print(f"Winner: {winner}")
print("*************************************************")

#Write results into file

with open(pyPoll_out_path, 'w', newline='') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["*************************************************"])
    csvwriter.writerow(["Election Results"])
    csvwriter.writerow(["-------------------------------------------------"])
    csvwriter.writerow([f"Total Votes: {total_votes}"])
    csvwriter.writerow(["-------------------------------------------------"])
    for i in range(0, my_length): #print(votes_summary_table)
        csvwriter.writerow([f"{my_candidates[i]}: {my_percentage_of_votes[i]:.3f}%  ({my_voter_results[i]})" ])
    csvwriter.writerow(["-------------------------------------------------"])
    csvwriter.writerow([f"Winner: {winner}"])
    csvwriter.writerow(["*************************************************"])