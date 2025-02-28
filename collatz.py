### collatz.py ###


# Step 1: Get the user to input an integer.

# Step 2: The instructions say positive integer.i kept writing this as an if statement and crashing the program at the first step. Then asked chatgpt what was wrong
# and it said the program had no instruction to continue when i used a negative value and that's why it just stopped. While statement allows it to continue

# Step 3: the instructions say it should stop at 1. so when input is not 1, start the next bit of the program. 
# had to check W3 schools on correct syntax combining ifs and whiles: https://www.w3schools.com/python/python_while_loops.asp 

# Step 4: check if the input is an even number. do this by doing user input % 2, which gives us remainder.
# if its 0, then its an even number. Saw this in Andrew's lab for this week isEven.py and consulted:
# https://www.geeksforgeeks.org/what-is-a-modulo-operator-in-python/ 
# if condition is met, divide user input by 2.

#Step 5: else if the input is uneven (i.e. the remainder is not zero), then first multiply it by 3 and then add 4.

#Step 6: The instructions say print on one line so edited the print statement once everything was done.  

user = int(input("Please enter a positive integer: "))

while user <= 0:
    print("Error: Please enter a positive number.")
    user = int(input("Please enter a positive integer: "))

while user != 1:
    print(user, end=" ")  # Print numbers on the same line with spaces
    if user % 2 == 0:
        user //= 2
    else:
        user = (user * 3) + 1

print(user)

