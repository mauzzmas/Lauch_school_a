def check_me_out():
	global x, y
	while True:
		try :
			x = float(input('Please enter first number:'))
		except ValueError :
			print('Invalid type please type in a valid number')
		try :
			y = float(input('Please enter second number:'))
		except ValueError :
			print('Invalid type please type in a valid number')
		break
	final_result(x,y)

def final_result(x,y):

	procedure = input("Please enter operation you want to perform addition, multiplication, division, subtraction, or exponentiation:")
	#procedure = input()

	while procedure not in ['addition', 'subtraction', 'multiplication', 'division', 'exponentiation']:
		print("Please enter addition, subtraction, multiplication, division, exponentiation:")
		procedure = input()
		break

	if procedure == 'addition':
		addition = x + y
		print(addition)

	if procedure == 'subtraction':
		subtraction = x - y
		print(subtraction)

	if procedure == 'division':

		clarification = input("Which number is the denominator first or second?:")

		while clarification not in ['first', 'second']:
			print("Please enter either first or second:")
			clarification = input()
			break
		
		if clarification == 'first':
			division = x/y
			print(division)
		
		if clarification == 'second':
			division = y/x
			print(division)

	if procedure == 'exponentiation':

		clarification = input('Which number is exponent first or second?:')

		while clarification not in ['first', 'second']:
			print("Please Enter either first or second")
			clarification = input()
			break

		if clarification == 'first':
			exponentiation = y ** x
			print(exponentiation)

		if clarification == 'second':
			exponentiation = x ** y
			print(exponentiation)


check_me_out()