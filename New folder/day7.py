Data Structures
---------------
list is a data structure and acts as a container object.
list a mutable object.
          add a element
		  modify a element
		  delete a element.
list is a order sequence value.
list is a growable and shrinkable.
list have a index with +ve index and -ve index.
list homogenous elements and also hetrogenous elements.
list allows duplicate values.

how to create a list?
2 ways

[] 

and 
list()
-------------------------

list()
[]
a=[]
a
[]
type(a)
<class 'list'>
len(a)
0
b=list()
b
[]
type(b)
<class 'list'>
len(b)
0
---------------------------------
[]
[20]
[20]
[20,30,40]
[20, 30, 40]
[40,2,30]
[40, 2, 30]
['teju',20,False,'bnagar',560079]
['teju', 20, False, 'bnagar', 560079]
['teju',20,False,'bnagar',560079][0]
'teju'
info_tej=['teju',20,False,'bnagar',560079]
info_tej[0]
'teju'
info_tej[4]
560079
info_tej[0]='meju'  //update
info_tej[0]
'meju'
del info_tej[1]    //delete
info_tej
['meju', False, 'bnagar', 560079]
a=['teju',20,False,'bnagar',560079]
info_tej
['meju', False, 'bnagar', 560079]
a=info_tej
a
['meju', False, 'bnagar', 560079]
info_tej
['meju', False, 'bnagar', 560079]
[10,10,10,20,30,40]
[10, 10, 10, 20, 30, 40]

how to do create a list?
[] -->empty list

using while loop

#items=[10,10,20,30,40,50]
#i=0
#s=0
#while i<len(items):
#    s=s+items[i]
#    i+=1
#print('total bill by teju is ',s)

using for loop
-
items=[10,10,20,30,40,50]
s=0
for i in items:
    s=s+i

print('total bill is ',s)

unpacking 
---------

   java,python,devops=[10200,1400,3000]

   a=[10,20,30,40]
   
   
   x=[10,20,30]
   y=[40,50,60]
   x+y  --> list concationation
   x+y
   [10, 20, 30, 40, 50, 60]
   
   list mulitiplication
   -------------------
   x=[10,20,30]
   x=[10,20,30]*2
   x
   [10, 20, 30, 10, 20, 30]

   Functions on the list 
   ---------------------
   a=[10,20,30,40,90,23,45,67]
   max(a)
   90
   min(a)
	10
   sum(a)
	325
   avg=sum(a)/len(a)
   all(a)
	True
	any(a)
	True
   a=[0,10,20]
   all(a)
   False
   any(a)
  True
  a=[0,0,0]
  any(a)
  False
  
  
 











    