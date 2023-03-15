import os
import csv

#Define Variables
Date =[]
Profit_Loss=[]
total_diff=[]

#Set input and output paths
CSV_PATH = os.path.join('Resources','budget_data.csv')
OUTPUT_PATH = os.path.join("analysis","Results.txt")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Read the file and append into lists
with open(CSV_PATH) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=',')
    csv_header=next(csvreader)
    for row in csvreader:
        Date.append(row[0])
        Profit_Loss.append(int(row[1]))
    length = len(Date)
    x = sum(Profit_Loss)

    #Delete first cell in Date column so that the Dates rows match profit change
    Date.pop(0)

    #Calculate changes per month, average change overall, and max/min dates
    for number in range(1,len(Profit_Loss)):
            total_diff.append(Profit_Loss[number]-Profit_Loss[number-1])
            average_total_diff=round(sum(total_diff)/((len(Profit_Loss))-1),2)
            max_profit_change=max(total_diff)
            min_profit_change=min(total_diff)
            max_profit_change_date = str(Date[total_diff.index(max(total_diff))])
            min_profit_change_date = str(Date[total_diff.index(min(total_diff))])

results = ("Financial Analysis\n"
       "------------------------------------------\n"     
       f"Total Months: {length}\n"
       f"Total: ${x}\n"
       f"Avereage Profit Change: ${average_total_diff}\n"
       f"Greatest Increase in Profits: {max_profit_change_date} (${max_profit_change})\n"
       f"Greatest Decrease in Profits: {min_profit_change_date} (${min_profit_change})\n"
)

with open(OUTPUT_PATH, 'w') as output_file:
    output_file.write(results)
    print(results)