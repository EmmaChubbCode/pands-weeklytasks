#accounts.py
# this program asks users to enter their account numbers and then displays it back to them but X's out everything except the last four digits of the number

#create a user input where they enter their account numbers
account_num = input("Please enter an 10 digit account number:")

# my first attempt i erroneously allowed users to input any data type, symbols, letters etc.
# i want to stick with my slicing method below so i need to keep my input as a string.
# i found the isdigit method here: https://www.codecademy.com/resources/docs/python/strings/isdigit
# according to the source above, it " checks if all the elements in the string are digits"

# this while loop was added last to make the program loop back around and not end if it encountered an input error.
# you can only get out of this while loop if the input is all digits. I wrote infinity loops by accident a few times before i got this right.
# see: https://realpython.com/python-while-loop/  
while account_num.isdigit() == False:
    # this error message is printed if the input is not all digits. 
    print("Error: Please enter a valid account number.")
    # then we ask the user to enter their account number again.
    account_num = input("Please enter an 10 digit account number:")

#use negative indexing because we want to focus on last numbers of the account.
# so working backwards its -1, -2, -3, -4 for last 4 digits. so go from fourth last to the end in the code. 
#splicing/indexing resource: https://www.pythonforbeginners.com/python-strings/string-splicing-in-python 
last_four = account_num[-4:]

# the remainder of the code is adapted from this approach here: https://stackoverflow.com/questions/9730653/is-there-a-better-way-to-mask-a-credit-card-number-in-python  
# This should calculate the length of the hidden portion without putting any constraints on how many they input
hidden_num = len(account_num) - 4

#print Xs for however many hidden numbers, then show the last four only.
print ("X" * hidden_num + last_four)
