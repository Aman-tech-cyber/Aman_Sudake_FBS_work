#* python is the auto restructive language
## numeric
#1. int
#int x : variable declaration - not availabe in python
x = 10 #variable intialization
       # type is use to identify the value of x 

#2. float
x = 3.14



#3. complex
x = 3 + 5j  #real + imaginary (3 is real number and 5j is imaginary number)


##Test
#1. string
x = 'Hello, World!'
x = "Hello, World!"

x = "student's data"
x = 'student\'s data'
x = '''
this first line
this is second line
'''

"""
this is first line
this is second line
"""


##Sequential
#1. list
x = [10, 20, 30, 40] #they are maintain in the maintain

#2. tuple
x = (10, 20, 30, 40)


#3. range
x = range(1, 10)


##Set type
#1. set
x = {10, 20, 30, 40}  #they are not maiintain in sequential order

#2.Frozenset
x = frozenset({10, 20, 30, 40, 'a'})


##Mapping 
#1. dict
x = {1: 'name',2: 'John',3:'age'} #in dict key:value pair


##boolean
#1. bool
x = True
x = False

##Nonetype none
x = None  
print(type(x))
#print(x)




##Binary
#1.bytes
b1 = b"Hello"  #ACSII bytes
b2 = bytes([65, 66, 67]) #bytes from list of integers(A, B, C)

print(b1)
print(b2)
print(b1[0])

#2.bytearray
ba = bytearray(b"Hello")
ba[0] = 74  # Change 'H' (72) to 'J' (74)

print(ba)         # bytearray(b'Jello')
print(ba.decode())# 'Jello

#3.memoryview
data = bytearray(b"Python")
mv = memoryview(data)

print(mv[0])   # 80 (ASCII for 'P')
mv[0] = 74     # Change 'P' to 'J'
print(data)    # bytearray(b'Jython')

#9146043651
