"""Print the credit card balance for the first year with minimum monthly payment"""

__author__ = 'Nicola Moretto'
__license__ = "GPLv2"

def minimumPayment(balance, annualInterestRate, monthlyPaymentRate):
    '''
    Print the credit card balance for the first year with minimum monthly payment
    :param balance: Outstanding balance on the credit card
    :param annualInterestRate: Annual interest rate (as decimal, e.g. 0.08)
    :param monthlyPaymentRate: Minimum monthly payment rate (as decimal, e.g. 0.02)
    '''
    monthlyBalance = balance
    monthlyInterestRate = annualInterestRate / 12.0
    totalPayment = 0

    for month in range(1, 13):
        print "Month: " + str(month)
        monthlyMinimumPayment = monthlyBalance * monthlyPaymentRate
        totalPayment += monthlyMinimumPayment
        print("Minimum monthly payment: " + format(monthlyMinimumPayment, '.2f'))
        monthlyUnpaidBalance = monthlyBalance - monthlyMinimumPayment
        monthlyInterest = monthlyUnpaidBalance * monthlyInterestRate
        monthlyBalance = monthlyUnpaidBalance + monthlyInterest
        print("Remaining balance: " + format(monthlyBalance, '.2f'))

    print("Total paid: " + format(totalPayment, '.2f'))
    print("Remaining balance: " + format(monthlyBalance, '.2f'))