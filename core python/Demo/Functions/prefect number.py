# write a program to check whether a number is perfect or not

def chkperfect():
    num = int(input('Enter number:'))
    sum = 0
    for i in range (1, num):
        if(num % i == 0):
            sum += i

    
    if(sum == num):
        print(f'{num} is a perfect number,')
    else:
        print(f'{num} is not a perfect number,')

chkperfect()




