import pandas as pd
import numpy as np
import os
import sys

csvpath = os.path.join("resources", "budget_data.csv")

budget_df = pd.read_csv(csvpath)

sys.stdout = open("PyBank_Results.txt", "w")

total_months = len(budget_df["Date"].unique())
print(total_months)

total_pl = budget_df["Profit/Losses"].sum()
"${:,.2f}".format(total_pl)
print(total_pl)

average_change = int(total_pl / total_months)
"${:,.2f}".format(average_change)
print(average_change)

greatest = budget_df.max()
print(greatest)

least = budget_df.min()
print(least)

sys.stdout.close()