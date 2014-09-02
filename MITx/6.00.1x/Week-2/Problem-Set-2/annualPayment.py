"""Find the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months"""

__author__ = 'Nicola Moretto'
__license__ = "GPLv2"

def annualPayment(balance, annualInterestRate):
    '''
    Return the minimum fixed monthly payment needed in order pay off a credit card balance within 12 months
    :param balance: Outstanding balance on the credit card
    :param annualInterestRate: Annual interest rate (as decimal, e.g. 0.08)
    :return: Minimum fixed monthly payment
    '''
    monthlyPayment = 10
    monthlyInterestRate = annualInterestRate / 12.0

    while True:
        monthlyBalance = balance
        totalPayment = balance
        for month in range(1, 13):
            monthlyUnpaidBalance = monthlyBalance - monthlyPayment
            interest = (monthlyBalance - monthlyPayment) * monthlyInterestRate
            totalPayment += interest
            monthlyBalance = monthlyUnpaidBalance + interest
        if totalPayment <= monthlyPayment*12:
            break
        else:
            monthlyPayment += 10

    return monthlyPayment