# project Collatz Sequence: Practice Project from the book
# automate the boring stuff chapter 3
# point to this is to also make a continue section after getting asked to continue or not.
# spacing could be wrong but it easier for me to see what is what
import sys


def collatz(number): # the function
    if number % 2 == 0: # for even numbers
        results = number // 2
    else:
        results = 3 * number + 1 # for odd numbers
    print(results)
    return results

while True: # main loop
    user_inputs = input("to quit 'Q' to continue 'C': ") # asking user to quit or continue

    if user_inputs == "C": # has user continue with program

        try:
            number = int(input("Enter a whole interger: ")) # asking user to input a whole number
            while collatz(number) != 1:
                number = collatz(number)

        except ValueError: # so if user does not input a interger it wont error out
            print("Please only use whole intergers only")

    elif user_inputs == "Q": # has user quit program
        print("Goodbye")
        sys.exit()

    else: # if user does not hit C or Q then it will show this message
        print('Please use uppercase "C" or "Q" to continue program')