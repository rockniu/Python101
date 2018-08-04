import numpy as np

a=(1,2,3,4)

x=np.array(a)


print 'x.shape=', x.shape
print 'x.ndim=', x.ndim
print 'x.max=', x.max(), 'x.min=', x.min()
print 'x.mean', x.mean()


b=[[1,2],[3,4]]
b.append([5,6])
b.append([7,8])
b.append([9,10])
y=np.array(b)

print y
print 'y.shape=', y.shape
print 'y.ndim=', y.ndim
print 'y.max(axis=0)=', y.max(axis=0)
print 'y.max(axis=1)=', y.max(axis=1)
print 'y.mean(axis=0)=', y.mean(axis=0)
print 'y.mean(axis=1)=', y.mean(axis=1)
print 'y.flatten=', y.flatten()