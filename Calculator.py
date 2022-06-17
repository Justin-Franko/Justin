from math import prod
from re import I
from tkinter import END
num = 0
while(num == 0):
    firstnum = input("Enter first number ")
    Secnum = input("Enter Second number ")

    print("\n")
    print("Enter the Number of which Operation you would like to use:\n")
    print("1. Add")
    print("2. Sub")
    print("3. Multiply")
    print("4. Divide")
    print("5. Leave")

    operation = input("Enter which Operation: ")
    print("\n")
    if operation == "1" :
        print("The Sum is equal to: ")
        sum = int(firstnum) + int(Secnum)
        print(sum)
    if operation == "2" :
        print("The difference is equal to: ")
        diff = int(firstnum) - int(Secnum)
        print(diff)
    if operation == "3" :
        print("The Product is equal to: ")
        product = int(firstnum) * int(Secnum)
        print(product)
    if operation == "4" :
        print("The divident is equal to: ")
        div = int(firstnum) / int(Secnum)
        print(div)
    if operation == "5":
        num = 1


