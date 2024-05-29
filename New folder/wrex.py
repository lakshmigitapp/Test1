
data='all studens are stupids'
f=open('pp.txt','w')
f.write(data)
f.close()
with open('pp.txt','r+') as devil:
    text=devil.read()
    print(text)
    print('cur posi ' ,devil.tell())
    devil.seek(16)
    print('cur posi',devil.tell())
    devil.write('gems!!!')
    devil.seek(0)
    text=devil.read()
    print(text)
    


 

