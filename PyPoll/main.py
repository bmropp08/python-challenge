import os
import csv
Candidate=[]
csvpath = os.path.join('PyPoll','Resources','election_data.csv')
with open(csvpath) as csvfile:
    csvreader=csv.reader(csvfile,delimiter=',')
    #print (csvreader)
    csv_header=next(csvreader)
    print(f"CSV Header:{csv_header}")
    for row in csvreader:
        Candidate.append(row[2])
    #print(Candidate) 
    print(f"Election Results")
    print(f"------------------------------------------")
    length = len(Candidate)
    print(f"Total Votes: {length}") 
    print(f"------------------------------------------")
    Charles=[]
    Diana=[]
    Raymon=[]
    for candid in Candidate:
        if candid == "Charles Casper Stockham":
            Charles.append(candid)
        elif candid == "Diana DeGette":
            Diana.append(candid)
        else:
            Raymon.append(candid)
    #print(len(Charles))
    #print(len(Diana))
    #print(len(Raymon))
    charles_percent= (len(Charles)/length)*100
    diana_percent= (len(Diana)/length)*100
    Raymon_percent= (len(Raymon)/length)*100
    print(f"Charles Casper Stockham:  {(round(charles_percent,3))}% ({len(Charles)})")
    print(f"Diana DeGette:  {(round(diana_percent,3))}% ({len(Diana)})")       
    print(f"Raymon Anthony Doane:  {(round(Raymon_percent,3))}% ({len(Raymon)})")    
    print(f"------------------------------------------")
    if len(Charles)> len(Diana) and len(Charles)>len(Raymon):
        print(f"Winner: Charles Casper Stockham")
    elif len(Diana)> len(Charles) and len(Diana)>len(Raymon):
        print(f"Winner: Diana DeGette")
    else:
        print(f"Winner: Raymon Anthony Doane")
        

