# Write a program to enter P, T, R and calculate simple Interest. 

P = int(input('Enter the principal amount:'))
R = int(input('Enter the rate of interest:'))
T = int(input('Enter the time period:'))
simple_interest = P * R * T / 100
print(f'Simple interest is :',simple_interest)