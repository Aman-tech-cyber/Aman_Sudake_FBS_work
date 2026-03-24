num = 25
for i in range(2, num):
    print(i)
    if(num % i == 0):  # module(%) is use to calculate reminder
        print(f'{num} is not a prime number.')
        break
else:
    print(f'{num} is a prime number.')