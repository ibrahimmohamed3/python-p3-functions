#!/usr/bin/env python3

def greeting():
    print(f"Hello, {name}")
greeting()   

def greet_programmer():
    print("Hello, programmer!")
greet_programmer()

def greet(name):
    print(f"Hello, {name}!")
greet("Ibrahim")    

def greet_with_default(name="programmer"):
    print(f"Hello, {name}")
greet_with_default("Ibrahim")    

def add(num1, num2):
    print(num1+num2)
add(2, 3)    

def halve(number):
    print(number/2)
halve(6)  
