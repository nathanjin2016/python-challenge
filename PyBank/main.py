import os
import csv
csvpath='csvfile/Budget_data.csv'
with open(csvpath, 'r') as csvfile:
    contents = csv.reader(csvfile, delimiter=',')
    csv_header = next(contents)
    num=0
    net=0
    cal=[]
    date=[]
    total=0
    x=1
    big=0
    small=0
    for row in contents:
        num+=1
        net+=float(row[1])
        cal.append(row[1])
        date.append(row[0])
    print(len(cal))
    print(len(date))

    while x < len(cal):
        change=float(cal[x])-float(cal[x-1])
        total+=change
        if change>big:
            big=change
            BigDate=date[x]
        elif change<small:
            small=change
            SmallDate=date[x]
        x=x+1
    ave_change=round(total/(len(cal)-1),2)


print(f'The total number of months is: {num}')
print(f'Total net amount is: ${net}')
print(f'Average change is: ${ave_change}')
print(f'Greatest Increase in Profits: {str(BigDate)} (${str(big)})')
print(F'Greatest Decrease in Profits: {str(SmallDate)} (${str(small)})')

