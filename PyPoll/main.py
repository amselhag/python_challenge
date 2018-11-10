import os
import csv

#selectin the path 
election_data_csvpath= os.path.join('election_data.csv')

#opening the CSV file
with open(election_data_csvpath, newline='') as csvfile:

    election= csv.reader(csvfile, delimiter= ',')
    election_header= next(election)
   
 #convert each column to a list
    
    voter_ID=[]
    county=[]
    candidate=[]

    for rows in election:
        voter_ID.append(rows[0])
        county.append(rows[1])
        candidate.append(rows[2])
        

#calculate the total votes and change it to integer

total_votes=int(len(voter_ID))

#creating a new list called candidates that take unique values of the candidates 
candidates=[]

for items in candidate:
    if items not in candidates:
        candidates.append(items)
        

#creating 2 lists one with voting results and the percentages by using the count function
voting_results=[]
voting_results_percent = []


for i in range (0, len(candidates)):
    
    voting_results.append(candidate.count(candidates[i]))
    voting_results_percent.append(candidate.count(candidates[i])/total_votes*100)

#finding the index value of the max to obtain the winner
winner_index = voting_results.index(max(voting_results))

#print the results

print('Election Results')
print("-----------------------")
print(f'Total votes: {total_votes}')
print("-----------------------")
for i in range (0, len(candidates)):
        print(f'{candidates[i]}: {voting_results_percent[i]:0.3f}% ({voting_results[i]})')
print("-----------------------")
print (f'winner: {candidates[winner_index]}')
print("-----------------------")

#open a text file and prin the results to that file
with open('out.txt', 'w') as output:
    print('Election Results', file=output)
    print("-----------------------", file=output)
    print(f'Total votes: {total_votes}', file=output)
    print("-----------------------", file=output)
    for i in range (0, len(candidates)):
        print(f'{candidates[i]}: {voting_results_percent[i]:0.3f}% ({voting_results[i]})', file=output)
    print("-----------------------", file=output)
    print (f'winner: {candidates[winner_index]}', file=output)
    print("-----------------------", file=output)
    
    output.close