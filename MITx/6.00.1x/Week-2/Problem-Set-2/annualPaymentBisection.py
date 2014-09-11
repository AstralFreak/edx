"""Find the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months with bisection method"""

__author__ = 'Nicola Moretto'
__license__ = "MIT"

def annualPaymentBisection(balance, annualInterestRate):
    '''
    Find the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months with bisection method
    :param balance: Outstanding balance on the credit card
    :param annualInterestRate: Annual interest rate (as decimal, e.g. 0.08)
    :return: Minimum fixed monthly payment
    '''
    monthlyInterestRate = annualInterestRate / 12.0
    precision = 0.01
    low = balance/12.0
    high = (balance * (1 + monthlyInterestRate)**12)/12.0
    monthlyPayment = (low+high)/2

    while True:
        monthlyBalance = balance
        totalDuePayment = balance
        for month in range(1, 13):
            monthlyUnpaidBalance = monthlyBalance - monthlyPayment
            interest = (monthlyBalance - monthlyPayment) * monthlyInterestRate
            totalDuePayment += interest
            monthlyBalance = monthlyUnpaidBalance + interest
        if abs(totalDuePayment-monthlyPayment*12) < precision:
            break
        elif totalDuePayment < monthlyPayment*12:
            high = monthlyPayment
        else:
            low = monthlyPayment
        monthlyPayment = (low+high)/2

    return monthlyPayment