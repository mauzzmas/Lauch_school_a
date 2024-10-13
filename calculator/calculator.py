import json

get_the_json = '/Users/mauzzammasood/messages.json'

with open(get_the_json, mode = 'r',  encoding = 'utf-8') as messages:
	input_data = json.load(messages)

def enter_num():
	global X, Y
	print(input_data["Greetings"]) 
	while True:
		try:
			X = float(input(input_data["EnterOne"]))
			break
		except ValueError:
			print(input_data["ErrorOne"])
	while True:
		try:
			Y = float(input(input_data["EnterTwo"]))
			break
		except ValueError:
			print(input_data["ErrorTwo"])
enter_num()
def enter_ops(X,Y):
	global procedure
	while True:
		procedure = input(input_data["EnterProc"])
		if procedure == 'addition':
			add_me = X + Y
			print(add_me)
			break
		if procedure == 'subtraction':
			subtract_me = X - Y
			print(subtract_me)
			break
		if procedure == 'multiplication':
			multiply_me = X * Y 
			print(multiply_me)
			break
		if procedure == 'division':
			print(extra_feature(X,Y, procedure))
			break
		if procedure == 'exponentiation':
			print(extra_feature(X,Y, procedure))
			break
		else:
			print(input_data["ErrorProc"])
def extra_feature(X,Y, procedure):
	if procedure == 'division':
			clarification = str(input(input_data["Clarity"]))
			if clarification == 'first':
				divide_me = Y/X
				return divide_me
			if clarification == 'second':
				divide_me = X/Y
				return divide_me
	if procedure == 'exponentiation':
			clarification = str(input(input_data["Clarity"]))
			if clarification == 'first':
				power_me = Y ** X
				return power_me
			if clarification == 'second':
				power_me = X ** Y
				return power_me
enter_ops(X,Y)
def last_check_in():
	while True:
		exit_program = input(input_data["Redo"])
		if exit_program == 'exit':
			print(input_data["Bye"])
			break
		else:
			enter_num()
			enter_ops(X,Y)
last_check_in()				







	