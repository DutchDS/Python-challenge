# Define Variables

period_count = 0 #Counter for Months
total_profit = 0 #Sum of Value over all months
change_profit = 0 #Sum of Vaue change for Month - Month-1
avg_profit = 0 #Change / Months-1
max_profit_change = 0 #Max of Change
min_profit_change = 0 #Min of Change
i = 1  #counter

my_array = ["Month","Profit","Change"]

#Read all records into an array


#Loop through the array and update Variables
#Months, Total change and Average Change
#Append Average Change to new array

period_count = 10
change_profit = 0

while i <= period_count:
    change_profit = change_profit + 13
    my_array.append(change_profit)
    print(my_array)
    i = i + 1


avg_profit = change_profit/(period_count)
#Loop through my array and find greatest increase and decrease



#Print outcome to screen
print("Financial Analysis")
print("-------------------------------------------------")
print(f"Total Months: {period_count}")
print(f"Total: {total_profit}")
print(f"Average Change: {avg_profit}")
print(f"Greatest Increase in Profits: {max_profit_change}")
print(f"Greatest Decrease in Profits: {min_profit_change}")

#Write results into file