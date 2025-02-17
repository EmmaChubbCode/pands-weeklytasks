#accounts.py
# this program asks users to enter their account numbers and then displays it back to them but X's out everything except the last four digits of the number

#create a user input where they enter their account numbers
account_num = input("Please enter an 10 digit account number:")

#use negative indexing because we want to focus on last numbers of the account.
# so working backwards its -1, -2, -3, -4 for last 4 digits. so go from fourth last to the end in the code. 
# splicing/indexing resource: https://www.pythonforbeginners.com/python-strings/string-splicing-in-python 

last_four = account_num[-4:]
print(last_four)

# Got stuck here and did some googling. Found this: https://stackoverflow.com/questions/9730653/is-there-a-better-way-to-mask-a-credit-card-number-in-python 

# This should calculate the length of the hidden portion without putting any constraints on how many they input
hidden_num = len(account_num) - 4

#print Xs for however many hidden numbers, then show the last four only.
print ("X" * hidden_num + last_four)