#import modules
import os
import csv

#declare path to csv file
csvpath = os.path.join('PyBank','Resources', 'budget_data.csv')

#create variable for list
monthly_change_list = []
date_list = []

#create counter variables
total_months = 0
total_profit = 0
total_change_profit = 0
initial_profit = 0

#open csv file using csvpath
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')  
    csv_header = next(csvreader)

    #begin for loop to determine total months, total profit, monthly change
    for row in csvreader:
        
        #add 1 to the total_months counter to determine total months for each row
        total_months = total_months + 1

        #add the value in the 2nd column to the total_profit counter to determine total profit for each row
        total_profit = total_profit + int(row[1])

        #subtract the value in the 2nd column from the initial profit 
        monthly_change = int(row[1]) - initial_profit

        #add the monthly change to the monthly change list
        monthly_change_list.append(monthly_change)

        #reset the initial profit value to the value in the current row
        initial_profit = int(row[1])

        #add the date to the date list
        date_list.append(row[0])

        #determine the greatest increase by finding the max value on the monthly change list
        greatest_increase = max(monthly_change_list)
        #determine the increase date by indexing the greatest increase and applying the index value to the date list
        increase_date = date_list[monthly_change_list.index(greatest_increase)]

        #determine the greatest decrease by finding the min value on the monthly change list
        greatest_decrease = min(monthly_change_list)
        #determine the greatest decrease by indexing the greatest decrease and applying the index value to the date list
        decrease_date = date_list[monthly_change_list.index(greatest_decrease)]

#create a function for the average of the monthly change list
def Average(list):
    return sum(list) / len(list)

#remove the first value in the monthly change list
monthly_change_list.pop(0)

#determine the average of the monthly change list
average = round(Average(monthly_change_list),2)

#print and export to a text file
Financial_Report = (
f"Financial Analysis\n"

f"\n-------------------------------\n"

f"\nTotal Months: {total_months}\n"

f"\nTotal: ${total_profit}\n"

f"\nAverage Change: ${average}\n"

f"\nGreatest Increase in Profits: {increase_date} (${greatest_increase})\n"

f"\nGreatest Decreasee in Profits: {decrease_date} (${greatest_decrease})")

print(Financial_Report)

financial_analysis = os.path.join('PyBank','Analysis','financial_analysis.txt')

with open(financial_analysis, "w") as text:
    text.write(Financial_Report)



        
  
