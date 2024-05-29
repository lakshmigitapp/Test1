f=open('samp.txt','r')
head=f.readline()
lines=f.readlines()
print(lines)
info={}
for line in lines:
    w=line.strip().split(',')
    sal=int(w[-2])
    sx=w[2]
    if info.get(sx)==None:
        info[sx]=sal
    else:
        info[sx]+=sal
print(info)
