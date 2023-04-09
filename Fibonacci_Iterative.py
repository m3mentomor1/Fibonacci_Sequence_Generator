
# ------------------------------------------------------
# File Name: Fibonacci_Iterative.py
# ------------------------------------------------------
# Date Finished: 07-29-2022
# ------------------------------------------------------
# Description:
# This is a simple iteratively calculated fibonacci 
# sequence generator that takes an integer input from 
# a user, then uses that input as the number of terms 
# in the sequence.
# ------------------------------------------------------

print("\n------- Fibonacci Sequence Generator -------\n")

while True:
    try:   
        # Number of terms                                                                                                     
        nth = int(input("Enter no. of terms to generate\n(Note: Term count starts at 0): "))   
        if nth <= 0:                                                  
            print("Input must be a positive integer!\n")              
        else:                                                         
            break                                                     
    except:                                                           
        print("Invalid input! Try again.\n")                          


def main():
    
    sequence = [0, 1] # First 2 terms as a list.
    count = 2         # Iteration/loop counter.

    msg = "\nFibonacci Sequence:"

    if nth == 1:
        print(msg + "\n", [sequence[0]], sep="") # Prints the first term of the sequence if number of terms is 1
    
    else:
        print(msg)

        # Iterates the calculation of the next terms in the sequence:
        while count < nth:
            sequence.append(sequence[count-1] + sequence[count-2])  # Adds the newly calculated terms to the list. 

        print(sequence)

main()

print("\n--------------------------------------------\n")

