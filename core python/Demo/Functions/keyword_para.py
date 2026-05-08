#1. TO neglet postion para / arg concept
#2. Assigning value to parameter in function call
#3. flow from right to left
#4. parameter name in function call and function defination shoulfd be same.


def emp(id, name, sal):
    id_str = f'ID = {id}'
    name_str = f'NAME = {name}'
    sal_str = f'SALARY = {sal}'


    return f'{id_str}\n{name_str}\n{sal_str}'

i = 101
nm = 'ABC'
s = 15000

res = emp(name = nm, id = i, sal = s)

print (res)


# if we combine default  and keyworld conncet then we can randomly pass parameter to function.