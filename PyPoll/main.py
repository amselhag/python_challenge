import os
import csv

election_data_csvpath= os.path.join('election_data.csv')

with open(election_data_csvpath, newline='') as csvfile:

    election= csv.reader(csvfile, delimiter= ',')
    election_header= next(election)
   
    
    voter_ID=[]
    county=[]
    candidate=[]

    for rows in election:
        voter_ID.append(rows[0])
        county.append(rows[1])
        candidate.append(rows[2])
        
#print(voter_ID)
#print(county)
#print(candidate)

total_votes=int(len(voter_ID))


candidates=[]

for items in candidate:
    if items not in candidates:
        candidates.append(items)
        

        
voting_results=[]
voting_results_percent = []

for i in range (0, len(candidates)):
    
    voting_results.append(candidate.count(candidates[i]))
    voting_results_percent.append(candidate.count(candidates[i])/total_votes*100)


rounded_percentage=[]

winner_index = voting_results.index(max(voting_results))

print('Election Results')
print("-----------------------")
print(f'Total votes: {total_votes}')
print("-----------------------")
for i in range (0, len(candidates)):
        print(f'{candidates[i]}: {voting_results_percent[i]:0.3f}% ({voting_results[i]})')
print("-----------------------")
print (f'winner: {candidates[winner_index]}')
print("-----------------------")

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