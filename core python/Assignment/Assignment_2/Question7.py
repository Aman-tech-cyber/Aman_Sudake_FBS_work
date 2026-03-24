# Find the sum of three-digit number.

num = int(input('Enter a three digit number:'))

digit1 = num // 100
digit2 = (num % 100) // 10
digit3 = num % 10

sum_of_digits = digit1 + digit2 + digit3

print(f'The sum of digits of {num} is: {sum_of_digits}')

