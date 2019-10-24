# Define Variables
import os
import csv

csvpath = os.path.join('..','Resources', 'election_data.csv')

vote_counter = 0 #Counter for each vote
total_votes = 0 #Sum of votes
candidate_votes_cnt = 0 #Sum of votes per candidate
candidate_votes_pct = 0 #Percentage of votes per candidate
my_cvs_array = []
my_candidates = []
my_voter_results = [0,0,0,0]
#votes_summary_table = []
winner = "TBD"

#Read all records from csv into imported_csv_table
with open(csvpath, newline='') as cvsfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(cvsfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    print(csv_header)

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
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

#Append Percentage of votes to votes_summary_table
#And determine 'winner'
i = 0

# for candidate in my_candidates:
#     for row in my_cvs_array:
#         if row[2] == str("Khan"):
#             vote_counter = vote_counter + 1

#     print(f"{candidate} Received {vote_counter} votes")

for row in my_cvs_array:
    if row[2] == my_candidates[0]:
        choice_index = 0
        my_voter_results[choice_index] += 1
    if row[2] == my_candidates[1]:
        choice_index = 1
        my_voter_results[choice_index] += 1    
    if row[2] == my_candidates[2]:
        choice_index = 2
        my_voter_results[choice_index] += 1    
    if row[2] == my_candidates[3]:
        choice_index = 3
        my_voter_results[choice_index] += 1


#Print outcome to screen

print("Election Results")
print("-------------------------------------------------")
print(f"Total Votes: {total_votes}")
print("-------------------------------------------------")
#Loop through my_array for votes per candicate
            #Print Column Headers
#print(votes_summary_table)
for i in range(0,4):
    print(f"Candidate {my_candidates[i]} received {my_voter_results[i]} votes" )
print("-------------------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------------------")


#Write results into file