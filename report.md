The dataset was retrieved from github and it contains motivational quotes and their authors from people like benjamin franklin, to plato. 

What did I do with pandas?
- Import the CSV file
- obtained basic information with the .head(), .describe(), and .info() functions
- Retreived a row by label and position
- Sliced rows by label and position
- Retrieved a single collumn
- Retrieved a cell
- Created two seperate filters and then combined them into a 3rd filter
- Added a new column that tells us the length of characters in their quote (single characters not word count)
- Deleted the column that was added
- Added back the deleted column for numerical data to be able to perform the group by function
- Used groupby function to find who has the highest character count in descending order