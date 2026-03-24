#x = input('Enter number 1:')
#print(type(x))

#Take input from user and add two numbers
num1 = int(input('Enter number 1:'))
num2 = int(input('Enter number 2:'))

#Perform addition
sum = num1 + num2

#display result
# print('Addition is',sum)  #Here there is space afer the addition because of (there are str and int datatypes in print function so python adds space by default)
# print('Addition is ' + str(sum))  #Here we are converting int to str so that there is no space in between

#f- string use to create string with variables
# print (f'Addition id {sum},')
print('Adition of '+str(num1)+' & '+str(num2)+' is '+str(sum)+'.')
print(f'Addition of {num1} and {num2} is {sum}.')


