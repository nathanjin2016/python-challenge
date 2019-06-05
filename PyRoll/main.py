import os
import csv
path=("CSVFile/election_data.csv")
with open(path, 'r') as file:
    contents=csv.reader(file, delimiter=',')
    csv_header=next(contents)
    count=0
    num=0
    name=[]
    vote=[]
    i=0

    for row in contents:
        count+=1
        if row[2] not in name:
            name.append(row[2])

    vote=[0]*len(name)

# Need to re-read the file, or else row has already in last column of the file. 
with open(path, 'r') as file:  
    contents=csv.reader(file, delimiter=',')
    csv_header=next(contents)
    for row in contents:
        for i in range(len(name)):
            if row[2]==name[i]:        
                vote[i]+=1

print(f'Total Votes: {str(count)}')
print(name)

for y in range(len(name)):
    perc=round(vote[y]/count*100,0)
    print(f'{name[y]}:{perc}00% ({vote[y]})')

winner=name[vote.index(max(vote))]
print("Winner: "+str(winner))

# Write result to a txt file
path= os.path.join ("PythonChallenge","homework.txt")
with open(path, 'w', newline='') as file:
    contents = csv.writer(file, delimiter=',')
    contents.writerow(['Total Votes: '+str(count)])
    contents.writerow([str(name)])
    # Print result by name
    for y in range(len(name)):
        perc=round(vote[y]/count*100,0)
        contents.writerow([f'{name[y]}:{perc}00% ({vote[y]})'])
    contents.writerow(["Winner: "+str(winner)])
    