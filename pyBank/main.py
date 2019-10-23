# Define Variables
import os
import csv

csvpath = os.path.join('Resources', 'budget_data.csv')

period_count = 0 #Counter for Months
total_profit = 0 #Sum of Value over all months
change_profit = 0 #Sum of Vaue change for Month - Month-1
change_profit_total = 0 #Needed for average
profit_prev_month = 0 #Placeholder for previouw month value
avg_profit = 0 #Change / Months-1
max_profit_change = 0 #Max of Change
max_month = "TBD"
min_profit_change = 0 #Min of Change
min_month = "TBD"
i = 1  #counter

my_array = []
my_profit = []

with open(csvpath, newline='') as cvsfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(cvsfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #  print(csv_header)

    # Read each row of data after the header
    for row in csvreader:
        #print(row)
        my_array.append(row)
#Read all records into an array


#Loop through the array and update Variables
#Months, Total change and Average Change
#Append Average Change to new array

j = 0 #to skip header row

for row in my_array:
    period_count = period_count + 1
    total_profit = total_profit + int(row[1])
    if j != 0:
        change_profit = int(row[1]) - profit_prev_month
        my_profit.append(change_profit)
    profit_prev_month = int(row[1])
    change_profit_total = change_profit_total + change_profit
    if change_profit < min_profit_change:
        min_profit_change = change_profit
        min_month = str(row[0])
    if change_profit > max_profit_change:
        max_profit_change = change_profit
        max_month = str(row[0])
    #print(my_profit[0])
    j = 1
    i = i + 0

avg_profit = change_profit_total/(period_count-1)
#Loop through my array and find greatest increase and decrease



#Print outcome to screen
print("Financial Analysis")
print("-------------------------------------------------")
print(f"Total Months: {period_count}")
print(f"Total: {total_profit}")
print(f"Total Change: {change_profit_total}")
print(f"Average Change: {avg_profit}")
print(f"Greatest Increase in Profits: {max_month} (${max_profit_change})")
print(f"Greatest Decrease in Profits: {min_month} (${min_profit_change})")

#Write results into file