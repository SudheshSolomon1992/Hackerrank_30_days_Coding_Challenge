#!/bin/python3

def multiples(number):
    for i in range(1,11):
        print (str(number) + " x " + str(i) + " = " + str(number * i))

def main():
    number = int(input())
    multiples(number)

if __name__ == '__main__':
    main()
