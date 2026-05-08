def sq(x):
    return x * x

data = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# res = list(map(sq, data))
res = list(map(lambda x: x * x , data))
print(res)