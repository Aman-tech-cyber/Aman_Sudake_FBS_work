def sos(n):
    if (n == 0):
        return 0
    else:
        print(n)
        return n+ sos(n - 1)

res =sos(n)
print(res);
