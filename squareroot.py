# followed along with instructions here, specifically the second easier version cos i was confused by the guesses input in the first one:
# https://runestone.academy/ns/books/published/thinkcspy/MoreAboutIteration/NewtonsMethod.html 

# n is going to be defined by the user.
n = float(input("Please enter a positive number: "))

#re-used this from my collatz.py file. 
# according to https://math.mit.edu/~stevenj/18.335/newton-sqrt.pdf, the guess has got to be bigger than 0.
# so while the input is less than or equal to 0, produce an error message for user.
while n <= 0:

        print("Error: Please enter a positive number.")
        n = int(input("Please enter a positive number: "))

# the function takes one input. the user input for which we'll find the square root.
def sqrt(n):
# this is our first guess at what the square root is.
    approx = 0.5 * n
# this is the formula for newtons method. You add the approximate root with the original number divided by the approximate root and divide by 2.
# for example: x = (x + n / x) / 2
# See: https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# im multiplying by 0.5 instead of dividing by 2 but its the same.
    betterapprox = 0.5 * (approx + n/approx)
    while betterapprox != approx:
        # this is the new approximation. keep looping.
        approx = betterapprox
    return approx

print(f"The square root of {n} is approximately {sqrt(n)}")


        