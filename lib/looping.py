#!/usr/bin/env python3

def happy_new_year():
    # code goes here!
    count=10
    while count > 0:
        print(count)
        count -= 1
    print("Happy New Year!")
            
    
happy_new_year()


int_list=list()
def square_integers(int_list):
    # code goes here!
    for num in int_list:
        print(num * num)
    pass
square_integers([1,2,3,4,5])

def fizzbuzz():
    # code goes here!
    i=1
    while i <=100:
        if i % 3 ==0 and i % 5 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)
        i += 1
    pass
fizzbuzz()