
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