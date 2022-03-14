#use type() function to print the data variable 
x = 5  # x =  5, here 5 is the integer 
print(type(x))

y = "i am adult"# here y variable is the string 
print(type(y)) 

z =20.9   
print(type(z))

e = 1j
print(type(e))

t = ["apple", "banana", "cherry"]
print(type(t))

s =  ("apple", "banana", "cherry")
print(type(y))

t = range(20)
print(type(t))

l = {"name" : "John", "age" : 36}		
print(type(l))

c = {"apple", "banana", "cherry"}		
print(type(c))

i = frozenset({"apple", "banana", "cherry"})	
print(type(i))

k = True
print(type(k))	

b = b"Hello"
print(type(b))
	
m = bytearray(5)	
print(type(m))

l = memoryview(bytes(5))
print(type(l))
