# Define Variables
import os
import csv

csvpath = os.path.join('..', 'Resources', 'budget_data.csv')
pyBank_out_path = os.path.join('..', 'Output', 'pyBank_out_file.csv')


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

my_array = []

with open(csvpath, newline='') as cvsfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(cvsfile, delimiter=',')

    # Read the header row first (skip this step if there is now header)
    csv_header = next(csvreader)
    #  print(csv_header)

    # Read each row of data after the header
    # Read all records into an array
    for row in csvreader:
        my_array.append(row)

#Loop through the array and update Variables
#Months, Total change and Average Change
#Append Average Change to new array

i = 0  #counter
j = 0 #to skip header row

for row in my_array:
    period_count = period_count + 1 #Count the number of months
    total_profit = total_profit + int(row[1]) #Keep adding to the overal total
    if j == 1:
        change_profit = int(row[1]) - profit_prev_month #Calculate Change to previous month, starting second month
    profit_prev_month = int(row[1])
    change_profit_total = change_profit_total + change_profit
    if change_profit < min_profit_change: #Set Greatest Decrease month and value
        min_profit_change = change_profit
        min_month = str(row[0])
    if change_profit > max_profit_change: #Set Greatest Increase month and value
        max_profit_change = change_profit
        max_month = str(row[0])
    #print(my_profit[0])
    j = 1
    my_array[i].append(change_profit)
    i = i + 1

#Determine Average Profit
avg_profit = change_profit_total/(period_count-1)

#I wanted to practice adding to my array
#for a in my_array:
#    print(my_array.index(a),a)

#Print outcome to screen
print("Financial Analysis")
print("-------------------------------------------------")
print(f"Total Months    : {period_count}")
print(f"Total           : ${total_profit}")
print(f"Average Change  : ${avg_profit:.2f}")
print(f"Greatest Increase in Profits: {max_month}  (${max_profit_change})")
print(f"Greatest Decrease in Profits: {min_month}  (${min_profit_change})")

with open(pyBank_out_path, 'w', newline='') as csvfile:

    # Initialize csv.writer
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(["Financial Analysis"])
    csvwriter.writerow(["-------------------------------------------------"])
    csvwriter.writerow([f"Total Months    : {period_count}"])
    csvwriter.writerow([f"Total           : ${total_profit}"])
    csvwriter.writerow([f"Average Change  : ${avg_profit:.2f}"])
    csvwriter.writerow([f"Greatest Increase in Profits: {max_month} ($  {max_profit_change})"])
    csvwriter.writerow([f"Greatest Decrease in Profits: {min_month} ($  {min_profit_change})"])