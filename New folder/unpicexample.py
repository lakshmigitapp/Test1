import pickle

f=open('picfile.txt','rb')
data=pickle.load(f)
print(data)
