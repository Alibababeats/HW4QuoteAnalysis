"""
Ali Salem
Prof. Iskander
INST 326
12/5/2025
HW 4
"""

import pandas as pd

dfquotes = pd.read_csv("C:\\csv data\\quotes.csv")
print("Quotes DataFrame Head:")
print(dfquotes.head())

print("Quotes DataFrame Info:")
print(dfquotes.info())

print("Quotes DataFrame Stat Description:")
print(dfquotes.describe())