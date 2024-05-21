#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    i = 10
    while i > 0:
        print(i)
        i -= 1
    print ("Happy New Year!")

def square_integers(int_list):
    # code goes here!
    int_list = [1,2,3,4,5]
    square_nums = [num * num for num in int_list]
    return square_nums

def fizzbuzz():
    # code goes here!
    i = 1
    while i <= 100:
        if (i % 3 == 0) and (i % 5 == 0):
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1
        
