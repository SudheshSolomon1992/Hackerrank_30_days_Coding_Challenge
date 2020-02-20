#!/bin/python3

def factorial(n):
    if n == 1:
        return n
    elif n < 1:
        return ("N should not be less than 1")
    else:
        return n * factorial(n-1)

def main():
    number = int(input())
    print (factorial(int(number)))
        
if __name__ == "__main__":
    main()
