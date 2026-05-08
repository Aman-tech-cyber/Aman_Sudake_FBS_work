def emp(id, name, sal):
    id_str = f'ID = {id}'
    name_str = f'NAME = {name}'
    sal_str = f'SALARY = {sal}'

    # to return one value
    return f'{id_str}\n{name_str}\n{sal_str}'

    # to return multiple value
    # return id_str, name_str, sal_str

# default parameter ka value flow karneka 
i = 101
nm = 'ABC'
s = 15000

# to get 1 returning value
res = emp(i, nm, s)

# to det multiple returning value
# res1, res2, res3 = emp(i, nm, s)

print(res)