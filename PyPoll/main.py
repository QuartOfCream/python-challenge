import pandas as pd
import os
import numpy as np
import sys 


csv_file = "election_data.csv"
election_df = pd.read_csv(csv_file)

total_votes = len(election_df["Voter ID"].unique())

print(total_votes)

list_candidates = election_df["Candidate"].unique()
print(list_candidates)

list = election_df["Candidate"].value_counts()
print(list)

khan_df = election_df.loc[election_df["Candidate"] == "Khan"]
khan = len(khan_df.value_counts())
khan_percent = khan / total_votes
print("Khan", khan, khan_percent)

correy_df = election_df.loc[election_df["Candidate"] == "Correy"]
correy = len(correy_df.value_counts())
correy_percent = correy / total_votes
print("Correy", correy, correy_percent)

li_df = election_df.loc[election_df["Candidate"] == "Li"]
li = len(li_df.value_counts())
li_percent = li / total_votes
print("Li", li, li_percent)

otooley_df = election_df.loc[election_df["Candidate"] == "O'Tooley"]
otooley = len(otooley_df.value_counts())
otooley_percent = otooley / total_votes
print("O'Tooley", otooley, otooley_percent)

print("Winner: Khan")
    
with open('pypoll_results_file.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("Total Vote: " + str(total_votes) + "\n")
    text.write("Khan" + ": " + str(khan_percent) +"% (" + str(khan) + ")""\n")
    text.write("Correy" + ": " + str(correy_percent) +"% (" + str(correy) + ")""\n")
    text.write("Li" + ": " + str(li_percent) +"% (" + str(li) + ")""\n")
    text.write("O'Tooley" + ": " + str(otooley_percent) +"% (" + str(otooley) + ")""\n")
    text.write("The winner is: Khan \n")
