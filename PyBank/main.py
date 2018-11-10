import os
import csv

#finding the path to the file
csvpath=os.path.join('budget_data.csv')

#opening the CSV file

with open(csvpath, newline='') as csvfile:

    reader=csv.reader(csvfile, delimiter=',')
    csv_header = next(reader)
   
   #creating two lists months and profit_losses to store each column
    months= []
    profit_losses=[]
    
    for rows in reader:
        months.append(rows[0])
        profit_losses.append(int(rows[1]))
        
#calculated the number of rows by taking the len of the months list

Total_months= len(months)
Total= sum(profit_losses)


#finding the maximum from the porfit losses column
maximum = max((profit_losses))

#created a new list called monthly_change

monthly_change=[]

for i in range (1, Total_months):
    change = profit_losses[i] - profit_losses[i-1]
    
    monthly_change.append(change)
    

average_change= sum(monthly_change)/len(monthly_change)

greatest_increase= max(monthly_change)
greatest_decrease=min(monthly_change)


index_max = monthly_change.index(greatest_increase)
index_min= monthly_change.index(greatest_decrease)


greatest_month=months[index_max+1]
lowest_month= months[index_min+1]

#printing the results to the terminal
print("   finacial analysis    ")
print("---------------------------")
print(f'Total Months: {Total_months}')
print(f'Total: ${Total}')
print(f'Average Change: ${round(average_change,2)}')
print(f'Greatest Increase in Profits: {greatest_month[3:]} (${greatest_increase})')
print(f'Greatest decrease in Profits: {lowest_month [3:]} (${greatest_decrease})')


#creating a text file and saving the results
with open('out.txt', 'w') as output:
    print("   finacial analysis    ", file=output)
    print("---------------------------", file=output)
    print(f'Total Months: {Total_months}', file=output)
    print(f'Total: ${Total}', file=output)
    print(f'Average Change: ${round(average_change,2)}', file=output)
    print(f'Greatest Increase in Profits: {greatest_month[3:]} (${greatest_increase})', file=output)
    print(f'Greatest decrease in Profits: {lowest_month [3:]} (${greatest_decrease})', file=output)

    
    output.close

