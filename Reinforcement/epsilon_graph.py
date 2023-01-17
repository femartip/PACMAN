import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

f = open("epsilon.txt", "r")
# Convert text file to dataframe
df = pd.read_csv(f, sep=" ", header=None)
df.columns = ["epsilon"]
# Delete duplicates from dataframe
df = df.drop_duplicates()
# Set index to number of rows
df.index = np.arange(1, len(df) + 1)
print(df)
# Plot dataframe
df.plot()
# Add label to x axis
plt.xlabel("Episode")
# Add label to y axis
plt.ylabel("Epsilon")
plt.show()

