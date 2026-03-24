#1. pass: to neglect expected indentation error
for i in range (1, 10):
    pass                 


#2. break: to terminate loop
for i in range (1, 5):
    if(i == 3):
        break
    print(i)


#3. continue: stop current interation (in contine the code run ani jethe 3 = 3 yeil te break honar ani pudhache run honar)
for i in range (1, 5):  # means continue does not concantrate on loops to executive
    if(i == 3):
        continue
    print(i)


#4. else: else will execute when the loop will fully executed 
for i in range(1, 6):
    if(1 == 3):
        break
else:
    print('Else block executive')