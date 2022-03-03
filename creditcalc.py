import argparse
import math

# Create parser object for command line args
parser = argparse.ArgumentParser(description='This program prints recipes \
consisting of the ingredients you provide.')

# Arg definitions
parser.add_argument('--type', choices=['annuity', 'diff'])
parser.add_argument('--payment')
parser.add_argument('--principal')
parser.add_argument('--periods')
parser.add_argument('--interest')

# Arg object = parser
args = parser.parse_args()
# The nominal declaration doesn't work here, specify in every if statement instead :(
# nominal = float(args.interest) / 12 * 100

# Set variables equal to entered command line args
# total = 0

# If user enters diff as an argument
if args.type == "diff":
    # If user enters loan principal, loan period and interest
    if args.principal and args.periods and args.interest:
        total = 0
        # Calculate nominal
        nominal = float(args.interest) / (12 * 100)

        # Calculate differential
        for i in range(0, int(args.periods)):
            differential = math.ceil(int(args.principal) / int(args.periods) + nominal * (int(args.principal) - int(args.principal) * i / int(args.periods)))
            print(f'Month {i + 1}: payment is {differential}')
            total = total + differential
            # print(f'Running Total: {total}')

        print(f'\nOverpayment = {total - int(args.principal)}')

    else:
        print("Incorrect differential parameters.")

# If user enters annuity as an argument
elif args.type == "annuity":

    # If user enters loan principal, loan period and interest
    if args.principal and args.periods and args.interest:

        # Calculate nominal
        i = float(args.interest) / (12 * 100)

        # Calculate monthly payment
        annuity = math.ceil(int(args.principal) * ((i * math.pow(1 + i, int(args.periods))) / (math.pow(1 + i, int(args.periods)) - 1)))
        print(f'Your annuity payment = {annuity}!')
        print(f'\nOverpayment = {annuity * int(args.periods) - int(args.principal)}')

    elif args.payment and args.periods and args.interest:

        # Calculate nominal
        i = float(args.interest) / (12 * 100)

        # Calculate principle
        principal = math.floor(int(args.payment) / ((i * math.pow(1 + i, int(args.periods))) / (math.pow(1 + i, int(args.periods)) - 1)))

        print(f'Your loan principal = {principal}!')

        print(f'\nOverpayment = {(int(args.payment) * int(args.periods)) - principal}')


    elif args.principal and args.payment and args.interest:

        # Calculate nominal
        i = float(args.interest) / (12 * 100)

        # Calculate loan_period
        # periods = math.log(payment / (payment - i * principal), 1 + i)
        periods = math.log(int(args.payment) / (int(args.payment) - i * int(args.principal)), 1 + i)
        periods = math.ceil(periods)

        and_ = ""

        number_years = str(periods // 12) + ' years' 
        number_months = str(periods % 12) + ' months' 

        if periods // 12 != 0 and periods % 12 != 0:
            and_ = " and "

        elif periods // 12 == 0:
            number_years = ""

        elif periods % 12 == 0:
            number_months = ""

        # Length of time needed to repay loan
        print(f'It will take {number_years}{and_}{number_months} to repay this loan!')
        # print(f'It will take {periods} months to repay this loan!')
        print(f'\nOverpayment = {(periods * int(args.payment)) - int(args.principal)}')

    else:
        print("Incorrect annuity parameters.")

else:
    print("Incorrect parameters.")


