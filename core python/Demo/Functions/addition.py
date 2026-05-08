def addition():
    num1 = int(input('Enter first number: '))
    num2 = int(input('Enter second number: '))
    sum = num1 + num2
    print('The sum of', num1, 'and', num2, 'is:', sum)

addition()
# print(num1)#This will give an error because num1 is a local variable. 
#  and it is only accessible within the function.
#  It cannot be accessed outside the function.