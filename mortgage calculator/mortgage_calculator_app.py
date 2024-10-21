import locale
import json


GET_THE_JSON = '/Users/mauzzammasood/mort_messages.json'

with open (GET_THE_JSON, mode = 'r', encoding = 'utf-8') as messages:
    input_data = json.load(messages)

print("Welcome this is the monthly mortgage and car payment calculator!!!")

'''	
	The check_loan function will take the users data about the total loan amount.
	The function also takes a string value and will condition whether the string value,
	and checks if it is able to pass as a float when converted. In addition the function will
	replace the '$' if part of the expression
'''

def check_loan():
    global new_loan
    while True:
        loan_amount = input(input_data['GetLoan'])
        if '$' in loan_amount:
            new_loan = loan_amount.replace('$', '')
            try:
                new_loan = float(new_loan)
                break
            except ValueError:
                print(input_data['ErrorMessageOne'])
        else:
            try:
                new_loan = float(loan_amount)
                break
            except ValueError:
                print(input_data['ErrorMessageOne'])
check_loan()

'''
	The user_interest_data function will take the users data about monthly APR. The function
	similarly to the check_loan will try to condition on returning a value on whether or not
	it returns a valid float type. The function will replace '%' if part of the expression.
'''

def user_interest_data():
    global monthly_interest_rate
	
    while True:
        monthly_interest_rate = input(input_data["InterestMessage"])
        if "%" in monthly_interest_rate:
            new_string = monthly_interest_rate.replace('%','')
            try:
                float(new_string)
            except ValueError:
                print(input_data["ErrorMessageTwo"])
				#works
            monthly_interest_rate = float(new_string)/100
            break
        else:
            try:
                float(monthly_interest_rate)
                break
            except ValueError:
                print(input_data["ErrorMessageTwo"])
    monthly_interest_rate = float(monthly_interest_rate)/12

user_interest_data()

'''
	The user_data_years function will try to differentiate whether the number input, is either
	is to be evaluated in terms of years or months. If it is years it will convert to months and check
	if it can be converted to a valid float type, for months it will just check the input
'''

def user_data_years():
    global duration 
	
    loan_duration = input(input_data["DurationMessage"])
	
    while loan_duration not in ['annual', 'monthly']:
        print(input_data["DurationError"])
        loan_duration = input()
	
    if loan_duration == 'annual':
        while True:
            duration = input(input_data["YearsMessage"])
            try:
                float(duration)
                break
            except ValueError:
                print(input_data["ErrorMessageThree"])
    duration = float(duration)*12
    if loan_duration == 'monthly':
        while True:
            duration = input(input_data["MonthsMessage"])
            try:
                float(duration)
                break
            except ValueError:
                print(input_data["ErrorMessageFour"])

user_data_years()

'''
	Calculation is where the magic happens the function takes three parameters from the previous
	three functions and calculates the monthly payments (THESE ARE PAYMENTS TO BE MADE EVERY MONTH ONLY)
'''		

def calculation(new_loan, monthly_interest_rate, duration):
	
    p = new_loan
    j = monthly_interest_rate
    n = duration
    m = p * (j / (1 - (1 + j) ** (-n)))
    monthly_payments = '${:,.2f}'.format(m)
    print(f'Your monthly payments are {monthly_payments}')

calculation(new_loan, monthly_interest_rate, duration)



