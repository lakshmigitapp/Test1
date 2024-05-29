import pickle

#serialization
data=[['shivanish',7369,800],['sagina',7599,1600],['teju',100,700]]
f=open('picfile.txt','wb')
pickle.dump(data,f)
f.close()
