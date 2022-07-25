import math
import sys
import numpy as np


def multiply():
    print("MULTIPLICATION")
    m_num_amount = int(input("How many numbers are we multiplying together? "))
    m_numbers_remaining = m_num_amount
    multiply_list = []
    for a in range(0, m_num_amount):
        m_num = float(input(f"Enter your numbers one at a time ({m_numbers_remaining}):"))
        m_numbers_remaining -= 1
        multiply_list.append(m_num)
    m_answer = np.prod(multiply_list)
    if m_answer > 10**70:
        print(f"Your answer is: {math.inf}")
    elif m_answer < -10**70:
        print(f"Your answer is: {-math.inf}")
    else:
        print(f"Your answer is: {m_answer}")
    m_end = input("Would you like to go back to the main menu? (Y/N): ").upper()
    if m_end == "Y":
        main_menu()
    else:
        multiply()


def divide():
    print("DIVISION")
    divide_list = []
    for b in range(0, 2):
        d_num = float(input(f"Enter your numbers one at a time:"))
        divide_list.append(d_num)
    print(f"Your answer is: {divide_list[0]/divide_list[1]}")
    d_end = input("Would you like to go back to the main menu? (Y/N): ").upper()
    if d_end == "Y":
        main_menu()
    else:
        divide()


def add():
    print("ADDITION")
    a_num_amount = int(input("How many numbers are we adding together? "))
    a_numbers_remaining = a_num_amount
    add_list = []
    for c in range(0, a_num_amount):
        a_num = float(input(f"Enter your numbers one at a time ({a_numbers_remaining}): "))
        a_numbers_remaining -= 1
        add_list.append(a_num)
    total_add = 0
    for i in add_list:
        total_add += i
    print(f"Your answer is: {total_add}")
    a_end = input("Would you like to go back to the main menu? (Y/N): ").upper()
    if a_end == "Y":
        main_menu()
    else:
        add()


def subtract():
    print("SUBTRACTION")
    s_num_amount = int(input("How many numbers are we subtracting from each other? "))
    s_numbers_remaining = s_num_amount
    subtract_list = []
    for d in range(0, s_num_amount):
        s_num = float(input(f"Enter your numbers one at a time ({s_numbers_remaining}): "))
        s_numbers_remaining -= 1
        subtract_list.append(s_num)
    total_subtract = subtract_list[0]
    for e in subtract_list[1:len(subtract_list)]:
        total_subtract -= e
    print(f"Your answer is: {total_subtract}")
    s_end = input("Would you like to go back to the main menu? (Y/N): ").upper()
    if s_end == "Y":
        main_menu()
    else:
        subtract()


def sqrt():
    print("SQUARE ROOT")
    sqrt_num = int(input("What number would you like to find the square root of? "))
    print(f"Your answer is: {math.sqrt(sqrt_num)}")
    sqrt_end = input("Would you like to go back to the main menu? (Y/N): ").upper()
    if sqrt_end == "Y":
        main_menu()
    else:
        sqrt()


def main_menu():
    while True:
        print("====================")
        print("=    Calculator    =")
        print("====================")
        option = input("Would you like to see what mathematical operations we have available? (Y/N) ").upper()
        if option == "Y":
            print("The operations we have available are as follows: ")
            print("Multiplication - multiply")
            print("Division - divide")
            print("Addition - add")
            print("Subtraction - subtract")
            print("Square Root - sqrt")
        else:
            print("Okay, let's get this calculation up and running!")
            operation_option = input("What operation should we perform? (Type the abbreviation in the list above, if you"
                                     " want to end program then type 'END') ")
            if operation_option == "multiply":
                multiply()
            elif operation_option == "divide":
                divide()
            elif operation_option == "add":
                add()
            elif operation_option == "subtract":
                subtract()
            elif operation_option == "sqrt":
                sqrt()
            elif operation_option == "END":
                print("EXITING PROGRAM")
                sys.exit()


main_menu()

