import json

GET_THE_JSON = '/Users/mauzzammasood/messages.json'

with open(GET_THE_JSON, mode = 'r',  encoding = 'utf-8') as messages:
    input_data = json.load(messages)

""" The function enter_num takes in input from user and verifies 
	if the input are float numbers."""

def enter_num():
    global var_one, var_two
    print(input_data["Greetings"])
    while True:
        try:
            var_one = float(input(input_data["EnterOne"]))
            break
        except ValueError:
            print(input_data["ErrorOne"])
    while True:
        try:
            var_two = float(input(input_data["EnterTwo"]))
            break
        except ValueError:
            print(input_data["ErrorTwo"])
enter_num()

""" The function enter_ops asks the users arithmetic operations they would 
	like to perform. If the users enter addition, subtraction or multiplication 
	the module will evaluate the operation, however if the user requests 
	exponentiation and division the variables are passed to function that adds 
	in extra features and the function isn't immediately called. """

def enter_ops(var_one, var_two):
    global calc_ops
    while True:
        calc_ops = input(input_data["EnterProc"])
        if calc_ops == 'addition':
            add_me = var_one + var_two
            print(add_me)
            break
        if calc_ops == 'subtraction':
            subtract_me = var_one - var_two
            print(subtract_me)
            break
        if calc_ops == 'multiplication':
            multiply_me = var_one * var_two
            print(multiply_me)
            break
        if calc_ops == 'division':
            print(extra_feature(var_one, var_two, calc_ops))
            break
        if calc_ops == 'exponentiation':
            print(extra_feature(var_one, var_two, calc_ops))
            break
        else:
            print(input_data["ErrorProc"])

""" The extra_feature function evaluates the arithmetic operations exponentation 
	and division, with the additional feature of asking the user the placement 
	of the variables in terms of the operation itself. """

def extra_feature(var_one, var_two, calc_ops):
    if calc_ops == 'division':
        try:
            clarification_of_ops = str(input(input_data["Clarity"]))
            if clarification_of_ops == 'first':
                divide_me = var_two/var_one
                return divide_me
            if clarification_of_ops == 'second':
                divide_me = var_one/var_two
                return divide_me
        except ZeroDivisionError:
            print("You are dividing by zero my guy! Try again!")
    if calc_ops == 'exponentiation':
        clarification_of_ops = str(input(input_data["Clarity"]))
        if clarification_of_ops == 'first':
            power_me = var_one ** var_two
            return power_me
        if clarification_of_ops == 'second':
            power_me = var_one ** var_two
            return power_me
enter_ops(var_one, var_two)

""" The function last_check_in checks if the user would like to terminate 
	the program or continue calculating."""

def last_check_in():
    while True:
        exit_program = input(input_data["Redo"])
        if exit_program == 'exit':
            print(input_data["Bye"])
        else:
            enter_num()
            enter_ops(var_one, var_two)
last_check_in()