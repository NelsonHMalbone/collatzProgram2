# project Collatz Sequence: Practice Project from the book
# automate the boring stuff chapter 3
# point to this is to also make a continue section after getting asked to continue or not.
import sys


def collatz(number):
    if number % 2 == 0:
        results = number // 2
    else:
        results = 3 * number + 1
    print(results)
    return results

while True:
    try:
        number = int(input("Enter a whole interger: "))
        while collatz(number) != 1:
            number = collatz(number)
            sys.exit()
    except ValueError:
        print("Please only use whole intergers only")