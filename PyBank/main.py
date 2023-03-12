import os
import csv
Date =[]
Profit_Loss=[]
total_diff=[]
csvpath = os.path.join('PyBank','Resources','budget_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #print (csvreader)
    csv_header=next(csvreader)
    #print(f"CSV Header:{csv_header}")
    for row in csvreader:
        Date.append(row[0])
        Profit_Loss.append(int(row[1]))
    #print(Profit_Loss)
    #print(Date)
    print(f"Financial Analysis")
    print(f"------------------------------------------")
    length = len(Date)
    print(f"Total Months: {length}")
    def total(Profit_Loss):
        total=0.0
        for number in Profit_Loss:
            total += number
        return total
    x=total(Profit_Loss)
    print(f"Total: ${x}")
    Date.pop(0)
    #print(Date)
    for number in range(1,len(Profit_Loss)):
            total_diff.append(Profit_Loss[number]-Profit_Loss[number-1])
            #new=list(zip(Date,total_diff))
            #print(new)
            average_total_diff=sum(total_diff)/((len(Profit_Loss))-1)
            max_profit_change=max(total_diff)
            min_profit_change=min(total_diff)
            max_profit_change_date = str(Date[total_diff.index(max(total_diff))])
            min_profit_change_date = str(Date[total_diff.index(min(total_diff))])
print("Avereage Profit Change: $", (average_total_diff))
print("Greatest Increase in Profits:", max_profit_change_date,"($", max_profit_change,")")
print("Greatest Decrease in Profits:", min_profit_change_date,"($", min_profit_change,")")

