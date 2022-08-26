a = "Hello World" #str
print(type(a))

b = 20 #int
print(type(b))

c = 20.5 #float
print(type(c))

d = 1j #complex
print(type(d))

e = ["Indonesia", "Malaysia", "Laos"] #list
print(type(e))

f = ("Indonesia", "Malaysia", "Laos") #tuple
print(type(f))

g = range(6) #range
print(type(g))

h = {"Indonesia", "Malaysia", "Laos"} #set
print(type(h))

i = {"Indonesia":"Garuda", "Malaysia":"Harimau Malaya", "Laos":"Loas"} #dict
print(type(i))

j = {"Indonesia":"Garuda", "Malaysia":"Harimau Malaya", "Laos":"Loas"} #dict
print(type(j))

k = frozenset({"Indonesia", "Malaysia", "Laos"}) #frozenset
print(type(k))
print(k)

l = True #bool
print(type(l))
print(l)

m = b"Hello" #bytes
print(type(m))
# print(m)

n = bytearray(5) #bytearray
print(type(n))
# print(n)

o = memoryview(bytes(5)) #memoryview
print(type(o)) 
# print(o)

p = None
print(type(p)) #noneType
# print(p)