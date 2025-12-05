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

#filtered rows
filter1 = dfquotes[dfquotes["Author"] == "Socrates"] # first filter
print("All quotes by Socrates:")
print(filter1)

#second filter
filter2 = dfquotes[(dfquotes["Author"] == "Plato") | (dfquotes["Author"] == "Epictetus")] 
print("All quotes by Plato and Epictetus:")
print(filter2)

#combined filters
Greek_philosophers = pd.concat([filter1, filter2])
print("All Quotes from greek philosophers")
print(Greek_philosophers) #did not implement .head here as only 2 out of the three authors show up at the top

"""
You will then show that you can add and remove columns. Create a new column in your DataFrame based on an existing column. 
For instance, by multiplying or transforming numeric values, or by combining two columns into one. 
Give the new column a clear name. 
Afterward, remove a column that you no longer need using the .drop() method with axis=1, 
and print the new list of columns to confirm that the column was removed.
"""
# Adding a new column based on existing data
dfquotes["Quote Character length"] = dfquotes["Quote"].apply(len)
print("DataFrame with New Column called Quote Character length:")
print(dfquotes.columns)

# Removing the newly added column
dfquotes = dfquotes.drop("Quote Character length", axis=1)
print("Current Columns in DataFrame:")
print(dfquotes.columns)