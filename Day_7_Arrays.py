#!/bin/python3

def main():
    
    number_of_elements = int(input())
    
    element = [int(n) for n in input().split()[:number_of_elements]]

    reverse(element)

def reverse(array):

    # reversed function is used to reverse an array in python3
    for element in reversed(array):
        print (element, end=" ")

if __name__ == "__main__":
    main()
