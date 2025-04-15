# banks.py
# this program prompts the user for two inputs of cents amounts. it then outputs those combined, formatted in euro and cents.

# code creating user inputs is adjustd from Andrew's lab material.
# in the first amount, add your first amount of cents
centAmount1= int(input("Enter amount 1(in cents) here:"))
# in the second amount, add your second amount of cents
centAmount2 = int(input("Enter amount 2(in cents) here:"))

#add them together (will deal with making them euro + formatted in later step)
total_cents = (centAmount1 + centAmount2)

# take the cents and floor divide by 100 to get the euro amount. Floor division will give the rounded integer. then get the remainder separately using %. 
# source for operators: https://www.w3schools.com/python/python_operators.asp 
# source on why to use floor division instead of regular division: https://www.geeksforgeeks.org/floor-division-in-python/ 

euros = total_cents // 100
cents = total_cents%100

# print the statement and plug in the variables euros and cents. Format with a decimal point and a euro sign.
print (f"The sum of these is €{euros}.{cents}")