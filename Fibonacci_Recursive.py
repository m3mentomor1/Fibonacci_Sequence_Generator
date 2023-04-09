
# ------------------------------------------------------
# File Name: Fibonacci_Recursive.py
# ------------------------------------------------------
# Date Finished: 07-30-2022
# ------------------------------------------------------
# Description:
# This is a simple recursively calculated fibonacci 
# sequence generator that takes an integer input from 
# a user, then uses that input as the number of terms 
# in the sequence.
# ------------------------------------------------------

from functools import lru_cache

print("\n---------- Fibonacci Sequence Generator ----------\n")

while True:
    try:       
        # Number of terms                                                                              
        n = int(input("Enter no. of terms to generate\n(Note: Term count starts at 0): "))      
        if n < 1:                                                   
            print("Input must be a positive integer!\n")            
        else:                                                       
            break                                                   
    except:                                                         
        print("Invalid input! Try again.\n")                        


@lru_cache(maxsize=None)    # Optimizes the recursion implementation

# Recursive function:
def f(n): 

    # Base case 1:
    if n == 1:
        return 0 # Returns the 1st term of the sequence if number of terms is 1

    # Base case 2:
    elif n == 2:
        return 1 # Returns the 2nd term of the sequence if number of terms is 2
    
    # Recursive case:
    elif n > 2:
        # Calculates & returns the next terms 
        # of the sequence using a recursive call:
        return f(n - 1) + f(n - 2) 


print("\nFibonacci Sequence:")

# Prints the sequence starting from the first 
# term up to the last calculated term based 
# on the inputted number of terms:
for n in range(1, n+1):     
    print(f(n), end="  ")   

print("\n\n--------------------------------------------------\n")

