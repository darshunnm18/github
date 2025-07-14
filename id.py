a=100
b=100
c=100
d=a
print(a==b==c==d)
#same memory is shared 
#same output
print(a is b)
print(b is c)
print(a is c)
print("==========")
x=10
print(x)
y=x
print(y)
print(x is y)
x=20
print(x)
print(x is y)
print("==========")
x=10
print(x)
print(id(x))
x=20
print(x)
print(id(x))
x=30
print(x)
print(id(x))
      