# at this point, all i know is i need a number and i need a number and a tolerance level:
# https://www.geeksforgeeks.org/find-root-of-a-number-using-newtons-method/ 

def squareRoot(n, l) :

    # n is going to be defined by the user.
    n = float(input("Please enter a positive number: "))

    #re-used this from my collatz.py file. 
    # according to https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf, the guess has got to be bigger than 0.
    # so while the input is less than or equal to 0, produce an error message for user.
    while n <= 0:

        print("Error: Please enter a positive number.")
        user = int(input("Please enter a positive number: "))
