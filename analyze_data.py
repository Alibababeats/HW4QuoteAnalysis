"""
Ali Salem
Prof. Iskander
INST 326
12/5/2025
HW 4
"""

import pandas as pd

dfquotes = pd.read_csv("C:\\csv data\\quotes.csv") # read the data
print("Quotes DataFrame Head:") # print first 5 rows
print(dfquotes.head())

print("Quotes DataFrame Info:") # print info about the DataFrame
print(dfquotes.info())

print("Quotes DataFrame Stat Description:") # print basic statistical description of the DataFrame
print(dfquotes.describe()) 

# Single row by its label
singlerow = dfquotes.loc[52]
print("Single Row by Label:")
print(singlerow)

# Single row by its position
print("Single Row by Position:")
singlerowpos = dfquotes.iloc[200]
print(singlerowpos)

#sliced rows by label
sliced1 = dfquotes.loc[122:132, "Author"]
print("Sliced Rows by Label:")
print(sliced1)

#sliced rows by position
sliced2 = dfquotes.iloc[30:40]
print("Sliced Rows by Position:")
print(sliced2)

#single colummn
collumn = dfquotes["Author"]
print("Single Column:")
print(collumn)

#single cell
cell = dfquotes.iloc[205]
print("Single Cell:")
print(cell)