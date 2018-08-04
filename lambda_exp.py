print (range(10))
s6=set(range(10))
f=lambda x:x*2;
print (map(f,s6))
print (map(lambda x:x*3, s6))

s5=s6.copy();

def fun1(x):
    return x**2
def fun2(x):
    return x%2==0
def fun3(x,y):
    return x+y

print ("map...")
s6=map(fun1, s5)
print (s6);print(type(s6))

print ("filter")
s7=filter(fun2, s6)
print (s7)
print(type(s7))
print ('reduct')
l8=reduce(fun3, s6)
print (l8)

