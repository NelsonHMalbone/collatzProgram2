# project Collatz Sequence: Practice Project from the book
# automate the boring stuff chapter 3
# point to this is to also make a continue section after getting asked to continue or not.
# import sys


def collatz(number):
    if number % 2 == 0: # for even numbers
        results = number // 2
    else:
        results = 3 * number + 1 # for odd numbers
    print(results)
    return results

while True: # main loop
    try:
        number = int(input("Enter a whole interger: ")) # asking user to input a whole number
        while collatz(number) != 1:
            number = collatz(number)
    except ValueError:
        print("Please only use whole intergers only")