# Author: Oboni Anower (oboni.anower@gmail.com)
#
# calc.py (c) 2023
#
# Description: Simple calculator
#              with error handling
#              options for user claculation (+, -, *, /, clr)
#              or show all the previously saved calculations
#

# Created:  1 February 2023  23:45:11
# Modified: 24 February 2023  20:01:09





# file created
# content written in file
with open('calc_equation.txt', 'a+') as eq:
    # functions
    # addition
    def add_num(num_1, num_2):
        print(f"{num_1} + {num_2} = {num_1 + num_2}\n")
        eq.write(str(num_1) + ' + ' + str(num_2) + ' = ' + str(num_1 + num_2) + '\n')

    # subtraction
    def subtract_num(num_1, num_2):
        print(f"{num_1} - {num_2} = {num_1 - num_2}\n")
        eq.write(str(num_1) + ' - ' + str(num_2) + ' = ' + str(num_1 - num_2) + '\n')

    # multiplication
    def multiply_num(num_1, num_2):
        print(f"{num_1} X {num_2} = {num_1 * num_2}\n")
        eq.write(str(num_1) + ' X ' + str(num_2) + ' = ' + str(num_1 * num_2) + '\n')

    # division
    def divide_num(num_1, num_2):
        try:
            print(f"{num_1} / {num_2} = {num_1 / num_2}\n")
            eq.write(str(num_1) + ' / ' + str(num_2) + ' = ' + str(num_1 / num_2) + '\n')
        except ZeroDivisionError:
            print(f"{num_1} / {num_2} = undefined\n")
            eq.write(str(num_1) + ' / ' + str(num_2) + ' = ' + 'undefined' + '\n')


    # Options for user_input or file read

    while True:
        options = input("u - user input"
                        "\nf - read from file"
                        "\ne - exit"
                        "\n>>")
        # User inputs
        if options == 'u':
            operator = input("[+] - add"
                             "\n[-] - subtract"
                             "\n[*] - multiply"
                             "\n[/] - divide"
                             "\n[c] - clear"
                             "\n>>")

            if operator == '+':
                while True:
                    try:
                        num1 = float(input("Enter the first number: "))
                        break
                    except ValueError:
                        print("Enter a valid number")

                while True:
                    try:
                        num2 = float(input("Enter the Second number: "))
                        break
                    except ValueError:
                        print("Enter a valid number")

                add_num(num1, num2)

            elif operator == '-':
                while True:
                    try:
                        num1 = float(input("Enter the first number: "))
                        break
                    except ValueError:
                        print("Enter a valid number")

                while True:
                    try:
                        num2 = float(input("Enter the Second number: "))
                        break
                    except ValueError:
                        print("Enter a valid number")

                subtract_num(num1, num2)

            elif operator == '*':
                while True:
                    try:
                        num1 = float(input("Enter the first number: "))
                        break
                    except ValueError:
                        print("Enter a valid number")

                while True:
                    try:
                        num2 = float(input("Enter the Second number: "))
                        break
                    except ValueError:
                        print("Enter a valid number")

                multiply_num(num1, num2)

            elif operator == '/':
                while True:
                    try:
                        num1 = float(input("Enter the first number: "))
                        break
                    except ValueError:
                        print("Enter a valid number")

                while True:
                    try:
                        num2 = float(input("Enter the Second number: "))
                        break
                    except ValueError:
                        print("Enter a valid number")

                divide_num(num1, num2)

            else:
                print('--OFF--')
                exit()

        # file read
        elif options == 'f':
            file_name = input("Enter the file name: ")
            try:
                with open(file_name, 'r') as eq_f:
                    f = eq_f.read()
                    print(f.strip())
                    print('\n--EXIT--')
                    exit()

            except FileNotFoundError:
                print("---File does not exist---")
                print("---enter a valid file name---\n")

        elif options == "e":
            print("--GOODBYE--")
            exit()

        else:
            print("INVALID OPTION SELECTED: TRY AGAIN!\n")
