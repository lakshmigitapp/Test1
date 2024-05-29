import functools
a=[1,2,3,4,5]

##def add(x,y):
##    return x+y

res=functools.reduce(lambda x,y:x+y,a)
print(res)
