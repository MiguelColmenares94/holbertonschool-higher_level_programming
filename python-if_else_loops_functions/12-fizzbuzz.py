#!/usr/bin/python3


def fizzbuzz():

    for counter in range(1, 101):
        a = counter % 3
        b = counter % 5

        if a == 0 and b == 0:
            print("FizzBuzz ", end="")
        elif a == 0:
            print("Fizz ", end="")
        elif b == 0:
            print("Buzz ", end="")
        else:
            print("{:d} ".format(counter), end="")
