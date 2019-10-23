# Define Variables
import os
import csv

csvpath = os.path.join('..', 'Resources', 'election_data.csv')

vote_counter = 0 #Counter for each vote
total_votes = 0 #Sum of votes
candidate_votes_cnt = 0 #Sum of votes per candidate
candidate_votes_pct = 0 #Percentage of votes per candidate
imported_csv_table = ["Month","Profit","Change"]
votes_summary_table = ["Candidate","Votes","Percentage"]
winner = "TBD"

# Specify the file to write to


#Read all records from csv into imported_csv_table


#Loop through the array and update Variables
#Per candidate, summarize the number of votes
#Append results to votes_summary_table


#Append Percentage of votes to votes_summary_table
#And determine 'winner'


#Print outcome to screen

print("Election Results")
print("-------------------------------------------------")
print(f"Total Votes: {vote_counter}")
print("-------------------------------------------------")
#Loop through my_array for votes per candicate
            #Print Column Headers
print(votes_summary_table)
print("-------------------------------------------------")
print(f"Winner: {winner}")
print("-------------------------------------------------")


#Write results into file