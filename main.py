# project Collatz Sequence: Practice Project from the book
# automate the boring stuff chapter 3
# point to this is to also make a continue section after getting asked to continue or not.

import sys
def collatz(num):
    if num % 2 == 0:  # for the even numbers
        result = num // 2
    elif num % 2 == 1: # the odd numbers
        result = 3 * num + 2

    while result == 1:
        print(result)
        sys.exit()

    while result !=1:
        print(result)
        num = result
        return collatz(num)

print("enter a number: ")
try:
    num = int(input())
    collatz(num)
except ValueError:
    print("You must use a Interger number")
