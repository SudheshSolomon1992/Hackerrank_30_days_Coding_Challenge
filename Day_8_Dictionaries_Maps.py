#!/bin/python3

def get_phone_number(name_array, dictionary):
    for name in name_array:
        if name in dictionary:
            print (name + "=" + dictionary[name])
        else:
            print ("Not found")

def main():
    inp_count = 0
    name_array = []
    directory = {}

    number_of_inputs = int(input())

    while inp_count < number_of_inputs:
        user_input = input().split(' ')
        name = user_input[0]
        phone = user_input[1]
        directory[name] = phone
        inp_count = inp_count + 1
    try:
        while True:     
            user_name = input()   
            if user_name == "":       
                break       
            else:
                name_array.append(user_name)
    except:
        pass
    get_phone_number(name_array, directory)

if __name__ == "__main__":
    main()
