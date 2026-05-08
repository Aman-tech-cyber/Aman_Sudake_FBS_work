#1. To pass multiple values to function
#2. Mention asterisk (*) before parameter name
#3. Passed value will stored in tuple
#4. use for loop to iletrate individuals values from tuple

def add(*data):
    # print(type(data))
    sum = 0
    for val in data:
        # print(val)
        sum += val
    return sum
# add(10)
res = add(10, 20, 30)
# add (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)


print(res)