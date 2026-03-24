#  Write a program to swap two numbers without using third variable. 

num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number:'))

num1 = num1 + num2  # 20 + 40 = 60
num2 = num1 - num2  #current value of num1 is 60 and num2 is 40, so 60 - 40 = 20
num1 = num1 - num2  #current value of num1 is 60 and num2 is 20, so 60 - 20 = 40

print(f'After swapping, the first number is: {num1}')
print(f'After swapping, the second number is: {num2}')