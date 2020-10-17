import os
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))
path = os.path.join (dir_path,"Resources", "election_data.csv")

votes = []
candidate = []


with open(path) as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ',')
    print(csvreader)
    csv_header = next(csvreader)
    print(f"CSV Header: {csv_header}")

    for column in csvreader:
        votes.append(column[0])
        candidate.append(column[2])

Total_Votes = (len(votes))
print(f"Total Votes {Total_Votes}")
Correy = int(candidate.count("Correy"))
Li = int(candidate.count("Li"))
Khan = int(candidate.count("Khan"))
Tooley = int(candidate.count("0'Tooley"))

Khan_Percentage= (Khan/Total_Votes)*100
Tooley_Percentage= (Tooley/Total_Votes)*100
Li_Percentage= (Li/Total_Votes)*100
Correy_Percentage= (Correy/Total_Votes)*100

print(f"Correy: {Correy_Percentage}% ({Correy}")
print(f"Khan: {Khan_Percentage}% ({Khan}")
print(f"Li: {Li_Percentage}% ({Li}")
print(f"Correy: {Tooley_Percentage}% ({Tooley}")

if Khan > Correy > Li > Tooley:
    Winner="Khan"
elif Correy > Khan > Tooley > Li:
    Winner="Correy"
elif Tooley > Khan > Li > Correy:
    Winner="Tooley"
elif Li > Khan > Corry > Tooley:
    Winner="Li"
print(f"Winner {Winner}")

output_path = os.path.join("analysis","election.txt")
with open(output_path,"w",newline='') as txtfile:
    txtfile.write(f'Total Votes: {Total_Votes}')
    txtfile.write(f'Khan: {Khan_Percentage}%({Khan}')
    txtfile.write(f'Correy: {Correy_Percentage}%({Correy}')
    txtfile.write(f'Li: {Li_Percentage}%({Li}')
    txtfile.write(f'Tooley: {Tooley_Percentage}%({Tooley}')
    txtfile.write(f"Winner:{Winner}")
    txtfile.close()
