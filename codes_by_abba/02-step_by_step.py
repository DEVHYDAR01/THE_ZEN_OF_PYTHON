#!/usr/bin/python3
'''
Takes string and writes it letter by letter till complete then back
'''


def begin_game(string_name):
    for i in range(len(string_name)):
        print(string_name[:i+1])


    for i in range(len(string_name)-2, -1, -1):
            print(string_name[:i+1])


input_string = input("Enter name, string or word of choice:  ")

begin_game(input_string)
