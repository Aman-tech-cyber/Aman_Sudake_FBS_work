#1. To pass multiple keyword arguments to a function
#2. Mentioned 2 asterisk(*) before para name
#3. passed value and attributes name will store in dictionary
#4. Use for loop on dict.items() to get key and value individually

def emp(**data):
    for i, j in data.items():
        print(i, ':', j)

emp(id = 101, name = 'ABC', sal = 15000, exp = 3, age = 35,flat_no = 407)