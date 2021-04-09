'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
PV = 50000
r = 2.5
n = 30
FV = PV * (1+r/100)**n
print(f"Future value is {FV}")