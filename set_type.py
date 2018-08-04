l = ['1',2, 3.0, 'String']
print (l)
l.append(2)
print (l)

s1=set(l);print (s1)
s1.add('rock');print (s1)
s2=set(['rock', 'niu', 4,5,6]);

print (s1.union(s2))

s3= s1.intersection(s2)
print (s3)
s4=s2.difference(s3)
print (s4)
s4.clear()
print (len(s4))

from random import randint
#list derfering
r1=[randint(0,10) for i in range(10)]
print (r1)

s5=set(r1)
print (s5)
