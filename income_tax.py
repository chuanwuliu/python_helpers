#!/usr/bin/python

import sys

def ind_tax(income):
    'Individual tax payable'

    assert income >= 0

    if income <= 18200:
        return 0
    elif income <= 37000:
        return 0.19 * (income - 18200)
    elif income <= 87000:
        return 0.325 * (income - 37000) + 3572
    elif income <= 180000:
        return 0.37 * (income - 87000) + 19822
    else:
        return 0.45 * (income - 180000) + 54232

income = int(sys.argv[1])

tax = ind_tax(income)
net_income = income - tax

print('Gross annual income: %d' %income)
print('Net annual income: %d' %net_income)
print('Net monthly income: %d' %(net_income/12.0))
print('Net weekly income: %d' %(net_income/52.0))