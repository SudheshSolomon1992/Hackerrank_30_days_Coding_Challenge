#!/bin/python3
def findBinary(number) : 
    binary = bin(number)[2:]
    return max(map(len, binary.split('0')))
      
def main():
    number = int(input())
    consecutiveOnes = findBinary(number)
    print (consecutiveOnes)

if __name__ == "__main__" : 
    main()
