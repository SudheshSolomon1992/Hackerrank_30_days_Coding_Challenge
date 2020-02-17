#!/bin/python3

def main():
    input_array = []
    
    test_cases = int(input())

    for i in range(test_cases):
        input_data = input()
        input_array.append(input_data)
    
    odd_even_characters(input_array)

def odd_even_characters(input_array):

    for elements in input_array:
        even_array = []
        odd_array = []
        for index in range(len(elements)):
            if index%2 == 0:
                even_array.append(elements[index])
            else:
                odd_array.append(elements[index])

        print (str(even_array).replace("'",'').replace(',','').replace(' ','').replace('[','').replace(']','') + " " + str(odd_array).replace("'",'').replace(',','').replace(' ','').replace('[','').replace(']',''))

if __name__ == "__main__":
    main()
