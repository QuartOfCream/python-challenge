import pandas as pd
import numpy as np
import os
import sys

csv_path = ("budget_data.csv")
budget_df = pd.read_csv(csv_path)

total_months = len(budget_df["Date"].unique())
print(str(total_months) + " months")

total_pl = budget_df["Profit/Losses"].sum()
"${:,.2f}".format(total_pl)
print(str(total_pl) + " total P/L")

average_change = int(total_pl / total_months)
"${:,.2f}".format(average_change)
print(str(average_change) + " average change")

greatest = budget_df.max()
print(greatest)

least = budget_df.min()
print(least)

with open('pybank_results_file.txt', 'w') as text:
    text.write("Election Results\n")
    text.write("Total Months: " + str(total_months) + "\n")
    text.write("Total Profits/Losses" + str(total_pl) + "\n")
    text.write("Average Change" + ": " + str(average_change) +"$" "\n")
    text.write("Greatest" + ": " + str(greatest) +"$" "\n")
    text.write("Least" + ": " + str(least) +"$" "\n")
    text.write("------------------------------------- \n")