import os
import csv
import numpy as np

#Define Variables
NAME_INDEX = 2
Candidate=[]

#Set input and output paths
CSV_PATH = os.path.join('Resources','election_data.csv')
OUTPUT_PATH = os.path.join("analysis","Results.txt")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

#Read the file and append into lists of unique Candidates
with open(CSV_PATH) as csvfile:
    csvreader = csv.reader(csvfile,delimiter=',')
    csv_header = next(csvreader)
    for row in csvreader:
        Candidate.append(row[NAME_INDEX])
candidate_list=np.unique([Candidate], return_index = True)     
print(f"Election Results")
print(f"------------------------------------------")
length = len(Candidate)
print(f"Total Votes: {length}") 
print(f"------------------------------------------")
count = np.unique(Candidate, return_counts=True)
candidates_dictionary = {}

#Calculate total votes and percentages per Candidate. Determine the Winner
with open(OUTPUT_PATH, 'w') as output_file:
    output_file.write("Election Results\n")
    output_file.write("------------------------------------------\n")
    output_file.write("Total Votes:"+ str(length)+"\n")
    output_file.write("------------------------------------------\n")
    for i in range(len(count)+1):
        candidates_dictionary[count[0][i]] = count[1][i]
        key_list = list(candidates_dictionary.keys())
        percent = round((count[1][i]/length)*100,3)
        results = (f'{key_list[i]}: {percent}% ({count[1][i]})\n')
        output_file.write(results)
        print(results)
    print(f"------------------------------------------")
    max_value = max(candidates_dictionary, key=lambda x:candidates_dictionary[x])
    print(f'Winner: {max_value}')
    print(f"------------------------------------------")
    output_file.write("------------------------------------------\n")
    output_file.write("Winner:"+ str(max_value)+"\n")
    output_file.write("------------------------------------------\n")
 
    