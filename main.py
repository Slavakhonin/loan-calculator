import math
import argparse

# Credit calculator


parser = argparse.ArgumentParser()
parser.add_argument("-t", "--type", choices=["annuity", "diff"],
                    help="You need to choose only one type of payment from the list.")
parser.add_argument("--payment")
parser.add_argument("--principal")
parser.add_argument("--periods")
parser.add_argument("--interest")

args = parser.parse_args()

if args.interest is None:
    print("Incorrect parameters")
    exit()

if args.type is None:
    print("Incorrect parameters")
    exit()

# if args.type == "annuity" and args.payment is None:
#     print("Incorrect parameters")
#     exit()

loan_parameters = [args.type, args.payment, args.principal,
                   args.periods, args.interest]

print(loan_parameters)


# print('''
# What do you want to calculate?
# type "n" for number of monthly payments,
# type "a" for annuity monthly payment amount,
# type "p" for loan principal:
# ''')
# payment_type = str(input())


def monthly(loan, month_payment, interest):
    # print("Enter the loan principal:")
    # loan = int(input())
    #
    # print("Enter the monthly payment:")
    # month_payment = int(input())
    #
    # print("Enter the loan interest:")
    # interest = float(input())
    #print(loan, month_payment, interest)
    monthly_interest = interest / 1200
    #print(monthly_interest)
    x = month_payment / (month_payment - monthly_interest * loan)
    #print(x)
    y = 1 + monthly_interest
    #print(y)
    number_month = math.ceil(math.log(x, y))

    if number_month % 12 == 0:
        years = number_month / 12
        print("It will take " + str(int(years)) + " years to repay this loan!")
    else:
        years = number_month // 12
        months = number_month % 12
        print("It will take " + str(years) + " years and " + str(months) + " month to repay this loan!")

    print("Overpayment = ", math.ceil(month_payment * number_month - loan))


def anuity_principal(payment, periods, interest):
    # print("Enter the annuity payment:")
    # payment = float(input())
    #
    # print("Enter the number of periods:")
    # periods = int(input())
    #
    # print("Enter the loan interest:")
    # interest = float(input())

    monthly_interest = interest / 1200

    i = math.pow((1 + monthly_interest), periods)

    x = payment / ((monthly_interest * i) / (i - 1))

    print("Your loan principal = ",  int(x), "!")
    print("Overpayment = ", math.ceil(payment * periods - x))

def annuity(loan, periods, interest):
    # print("Enter the loan principal:")
    # loan = int(input())
    #
    # print("Enter the number of periods:")
    # periods = int(input())
    #
    # print("Enter the loan interest:")
    # interest = float(input())

    monthly_interest = interest / 1200

    i = math.pow((1 + monthly_interest), periods)

    annuityp = loan * ((monthly_interest * i) / (i - 1))

    print("Your annuity payment = ", math.ceil(annuityp))
    print("Overpayment = ", math.ceil(math.ceil(annuityp) * periods - loan))

def payments_each_month(principal, periods, interest):
    i = interest / 1200
    m = 1
    total_payment = 0
    while m < 11:
        each_month = principal / periods + i * (principal - principal * (m - 1) / periods)
        print("Month {}: payment is {}".format(m, math.ceil(each_month)))
        m += 1
        total_payment += math.ceil(each_month)
    print("Overpayment = ", math.ceil(total_payment - principal))

# how many month it needs to be repaid
if loan_parameters[0] == 'diff' and loan_parameters[1] is None:
    payments_each_month(int(loan_parameters[2]), int(loan_parameters[3]), float(loan_parameters[4]))
    # print(payments(loan))
elif loan_parameters[0] == "annuity" and loan_parameters[1] is None:
    annuity(int(loan_parameters[2]), int(loan_parameters[3]), float(loan_parameters[4]))
elif loan_parameters[0] == "annuity" and loan_parameters[3] is None:
    monthly(int(loan_parameters[2]), int(loan_parameters[1]), float(loan_parameters[4]))
elif loan_parameters[0] == "annuity":
    anuity_principal(int(loan_parameters[1]), int(loan_parameters[3]), float(loan_parameters[4]))


    # monthly()
    # print(payments(loan))

# write your code here
