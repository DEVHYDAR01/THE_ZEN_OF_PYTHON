#!/usr/bin/python3
''' Making a step like pyraimid using a for loop '''
print("PYRAMID STEPS")
input_num = int(input("Enter number: \n"))
if input_num < 101:
    total_len = []
    for num in range(input_num):
        total_len += '#'
        print(total_len)
else:
    print("Number is too huge!!!")
