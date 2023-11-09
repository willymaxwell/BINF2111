#!/usr/bin/env/python3

def remainder(num1, num2):
    remainder=num1 % num2
    return remainder

def checkDivisibilityBy3(num1, num2):
    if ((num1 % 3) == 0):
        print(f"{num1} is divisible by 3.")
    if ((num2 % 3) == 0):
        print(f"{num2} is divisible by 3.")

def printQuotientBy3(num1, num2):
    quot1= num1/3
    quot2= num2/3
    print(f"Quotient of {num1} divided by 3: {quot1}")
    print(f"Quotient of {num2} divided by 3: {quot2}")

number1=15
number2=18

remainder_result=remainder(number1,number2)

print(f"Remainder when {number1} is divided by {number2}: {remainder_result}")

checkDivisibilityBy3(number1,number2)

printQuotientBy3(number1,number2)