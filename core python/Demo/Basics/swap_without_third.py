x = 10 
y = 20

print(f'Before swapping: x = {x}, y = {y}')

x = x + y  # x = 10 + 20 = 30
y = x - y  # y = 30 - 20 = 10
x = x - y  # x = 30 - 10 = 20

#method
x, y = y, x
print(f'After swapping: x = {x}, y = {y}')