import os
import csv
dir_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join (dir_path,"Resources", "budget_data.csv")
Number_Months = 0
Profit_Loss = 0
Lastmonth_change = 0
current_monthchange = 0
total_change = 0

total_changes =[]
months = []

with open (path) as csvfile:
    data_reader = csv.reader(csvfile)
    data_header = next(csvfile)
    
    for row in data_reader:
        Number_Months += 1
        current_monthchange = int(row[1])
        Profit_Loss += current_monthchange

        if (Number_Months ==1):
            Lastmonth_change = current_monthchange
            continue

        else:
            total_change = current_monthchange - Lastmonth_change
            months.append(row[0])
            total_changes.append(total_change)
            Lastmonth_change = current_monthchange

total_profitLoss = sum(total_changes)
average_profitLoss = round(total_profitLoss/(Number_Months - 1), 2)
biggest_change = max(total_changes)
lowest_change = min(total_changes)
biggest_change_index = total_changes.index(biggest_change)
lowest_change_index = total_changes.index(lowest_change)
Best_Month = months[biggest_change_index]
Worst_Month = months[lowest_change_index]

print("Financial Analysis")
print("-------------------")
print(f"Total Months: {Number_Months}")
print(f"Total: $ {Profit_Loss}")
print(f"average Change: ${average_profitLoss}")
print(f"Greatest Increase in Profits: {Best_Month} ${biggest_change}")
print(f"Greatest Decrease in Losses {Worst_Month} ${lowest_change}")

Budget_file = os.path.join("analysis", "BudgetData.txt")
with open(Budget_file, "w") as outfile:
    outfile.write("Financial Analysis\n")
    outfile.write("-------------------\n")
    outfile.write(f"Total Months: {Number_Months}\n")
    outfile.write(f"average Change: ${average_profitLoss}\n")
    outfile.write(f"Greatest Increase in Profits: {Best_Month} ${biggest_change}\n")
    outfile.write(f"Greatest Decrease in Losses {Worst_Month} ${lowest_change}\n")


  
        