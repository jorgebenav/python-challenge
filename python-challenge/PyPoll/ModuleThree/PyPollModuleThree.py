 
import csv
import os

pollraw = os.path.join('..', 'Resources', 'module_election_data.csv')

output_path = r'C:\Users\AndBe\Desktop\ASU Data\Homework\Starter_Code\PyPoll\ModuleThree\election_results.txt'

with open(pollraw) as pollcsv:
    pollread = csv.reader(pollcsv, delimiter=',')
    next(pollread, None) 
    total_votes = 0
    cand_votes = {}

    for row in pollread:
        total_votes += 1
        cand_name = row[2]

        if cand_name in cand_votes:
            cand_votes[cand_name] += 1
        else:
            cand_votes[cand_name] = 1

win = None
max_votes = 0

with open(output_path, 'w') as file:
    output_line = f"Total Votes: {total_votes}\n"
    print(output_line, end='')  
    file.write(output_line + "\n") 

    
    for candidate, votes in sorted(cand_votes.items()):
        vote_percentage = (votes / total_votes) * 100
        output_line = f"{candidate}: {vote_percentage:.3f}% ({votes})\n"
        print(output_line, end='') 
        file.write(output_line)  

    for candidate, votes in cand_votes.items():
        if votes > max_votes:
            max_votes = votes
            win = candidate

    output_line = f"\nWinner: {win}\n"
    print(output_line, end='') 
    file.write(output_line)  

print(f"Results have been written to {output_path}")
