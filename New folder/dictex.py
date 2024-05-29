info=[('raju','m',20000,10),('rani','f',30000,20),('raja','m',40000,10),('joker','m',100000,20),('ari','f',200000,10)]
total={}
for i in info:
    print(i)
    gen=i[1]
    sal=i[2]
    print(gen,sal)
    if total.get(gen)==None:
        total[gen]=sal
    else:
        total[gen]+=sal
print(total)
