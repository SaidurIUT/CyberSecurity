# Task1: 1. You are given 2 CSV files: users.csv and pass.csv.
# Use this CSV files to collect data and create custom keyword as follows:
# User[First 3 Letter]:Pass[Last 4 Letter]
# Example: If the username is ‘Xenophilius’ and password is ‘abcd!@#$’, the keyword will be ‘Xen!@#$’. Take the CSV files as input and output it in keywords.txt.
# Please properly comment your works and provide the .py files and the keywords.txt.





fileusers = open("users.csv", "r")              # opens the users.csv file for read
filepass = open("pass.csv", "r")                # opens the pass.csv file for read
filekeyword = open("keywords.txt", "w")         # opens the pass.csv file for write

users_lines = fileusers.readlines()             # every line of fileusers is now an element of usersd_lines array

for lineusers in users_lines:                   # runes a for loop 
    lineusers = lineusers.strip()

    filepass.seek(0)  # Reset pass.csv to the beginning
    for linepass in filepass:
        linepass = linepass.strip()

        users = lineusers[:3] 

        password = linepass[-4:]

        keyword = users + password + "\n"

        filekeyword.write(keyword)

fileusers.close()                              #closes the file
filepass.close()                               #closes the file
filekeyword.close()                            #closes the file
