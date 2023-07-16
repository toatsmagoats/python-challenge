#import modules
import os
import csv

#declare path to csv file
csvpath = os.path.join('PyPoll','Resources','election_data.csv')

#create list for variables
candidates_list = []
candidate_votes = []
percent_votes = []

#create counter for total votes
total_votes = 0

#open csv file
with open(csvpath) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')
    csv_header = next(csvreader)

    #determine total votes, unique candidates, and votes for candidates using for loop
    for row in csvreader:

        #add 1 to the total_votes counter
        total_votes += 1

        #create variable to store candidate's name
        candidate_name = str(row[2])

        #if the candidate's name is not in the candidates_list...
        if candidate_name not in candidates_list:
            #append the candidates name into the candidates_list
            candidates_list.append(candidate_name)
            #append 1 vote to the candidate_votes list
            candidate_votes.append(1)
        
        #if the candidate's name is in the candidates_list...
        else:
            #set the index variable to the index of the candidate's name on the candidates_list
            index = candidates_list.index(candidate_name)
            #add 1 vote to the index of that candidate in candidate_votes list
            candidate_votes[index] += 1

    #determine vote percentages for each candidate with for loop
    for votes in candidate_votes:
        
        #percentage votes = candidate votes / total votes * 100
        percentage = (votes/total_votes) * 100
        #format to 3 decimal places and include % sign
        percentage = "%.3f%%" % percentage
        #append the percentages to the percent_votes list
        percent_votes.append(percentage)

    #determine the winning candidate using the maximum value in the candidate_votes list
    winning_candidate = max(candidate_votes)
    #set the index variable to the index of the maximum value in candidate_votes list
    index = candidate_votes.index(winning_candidate)
    #declare the winner variable as the candidate in the candidates_list that has the same index as the maximum candidate votes
    winner = candidates_list[index]

#print election results to terminal
print(f"Election Results")

print(f"\n-----------------------------\n")

print(f"Total Votes: {total_votes}\n")

print(f"-----------------------------")

#use for loop to print the results for each of the candidates
for i in range(len(candidates_list)):
    print(f"\n{candidates_list[i]}: {str(percent_votes[i])} ({str(candidate_votes[i])})")

print(f"\n-----------------------------\n")

print(f"Winner: {winner}")

print(f"\n-----------------------------\n")

#declare path to text file
Election_Results = os.path.join('PyPoll','Analysis','Election_Results.txt')

#open text file and write the results
with open(Election_Results,"w") as text:

    text.write(f"Election Results\n")

    text.write(f"\n-----------------------------\n")

    text.write(f"\nTotal Votes: {total_votes}\n")

    text.write(f"\n-----------------------------")

    for i in range(len(candidates_list)):
        text.write(f"\n{candidates_list[i]}: {str(percent_votes[i])} ({str(candidate_votes[i])})\n")

    text.write(f"\n-----------------------------\n")

    text.write(f"\nWinner: {winner}\n")

    text.write(f"\n-----------------------------\n")