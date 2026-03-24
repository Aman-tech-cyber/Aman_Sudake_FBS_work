# Program to Find the Roots of a Quadratic Equation 

a = int(input('Enter the value of a:'))
b = int(input('Enter the value of b:'))
c = int(input('Enter the value of c:'))

d = b ** 2 - 4 * a * c

root1 = (-b + d ** 0.5) / (2 * a)
root2 = (-b - d ** 0.5) / (2 * a)
print(f'The roots of the quadratic equation is: {root1} and {root2}')