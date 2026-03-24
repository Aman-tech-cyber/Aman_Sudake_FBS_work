# Write a program to enter P, T, R and calculate Compound Interest. 

P = int(input('Enter the principal amount:'))
R = int(input('Enter the rate of interest:'))
T = int(input('Enter the time period:'))

compound_interest = P * (1 + R/100) ** T - P
print(f'compound_interest is:',compound_interest)
        