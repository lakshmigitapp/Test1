for loop
--------
syntax:- for variable in object:
              block of statements
			  
			  
break   --exit from the loop
continue --skip the current iteration

range() is a function.

range(stop)
range(start,stop)
range(start,stop,step)


range(start,stop)
   start-->include
   stop -->exclude
   
range(10)  

range(-10) 

range(10,20)

range(10) -->range(0, 10)

for i in range(10):
    print(i)
  
0
1
2
3
4
5
6
7
8
9
for i in range(10):
    print(i,end=" ")

    
0 1 2 3 4 5 6 7 8 9 

for i in range(-10):
    print(i)

    

for i in range(10,20):
    print(i)

    
10
11
12
13
14
15
16
17
18
19
for i in range(20,10):
    print(i)

    
for i in range(10,20,2):
    print(i)

    
10
12
14
16
18
for i in range(10,20,-2):
    print(i)

    
for i in range(20,10,-2):
    print(i)

    
20
18
16
14
12
for i in range(1,100,2):
    print(i)

prints 1-100
    

for  i in range(-1,-1,-1):
    print(i)

    
for i in range(10,-1,-1):
    print(i)

    
10
9
8
7
6
5
4
3
2
1
0
for i in range(10,-1,-1):
    print(i)

    
10
9
8
7
6
5
4
3
2
1
0
for i in range(10,-1,-/
               
SyntaxError: incomplete input
for i in range(10,0,-1):
    print(i)

               
10
9
8
7
6
5
4
3
2
1

break

for i in range(1,10):
    if i==5:
       break
    print(i)
	
	
continue

for i in range(1,10):
    if i==5:
       continue
    print(i)
	
Nested loops
------------	
for i in range(1,5):
    for j in range(1,5):
	    print(i,j)
	print('----')
	
	
	
	
	i=1    j=1,2,3,4
	i=2    j=1,2,3,4
	i=3    j=1,2,3,4
	i=4    j=1,2,3,4
	
	1 1
	1 2
	1 3
	1 4 
	
	2 1
	2 2
	2 3
	2 4
	3 1
	3 2
	3 3 
	3 4
	
	
******
******
******

for i in range(1,4):
   for j in range(1,7):
       print('*',end=" ")
   print(' ')
   
   
* * * * * *
*         *
*         *
* * * * * *
	

* * * *
* * *
* *
*

for i in range(1,6):
   for j in range(0,6-i):
      print('*',end=" ")
   print()




for i in range(1,6):
	for j in range(1,i+1):
		print('*',end=" ")

i=1 j=1 * 
    j=2 
	 
	
i=2 j=1 * * 
    j=2 
	j=3 
	
i=3 j=1 * * *
    j=2
	j=3
	j=4 
i=4 j=1
      	


*
* *
* * *
* * * *
* * * * *







* * * * *
* * * *
* * *
* *
*

for i in range(1,6):
   for j in range(6-i):
      print('*',end=" ")
   print()


     * 
   * * *
 * * * * *
* * * * * * 

r1   4(i-1) spaces   1(2*1-1) star 
r2   3(i-1) spaces   3(2*2-1) star
r3   2(i-1) spaces   5(2*3-1) star
r4   1(i-1) space    7(2*4-1) star 
r5   0(i-1) space    9(2*5-1) star 

list 
-----
11 methods

append()
clear()
copy()
count()
index()
insert()
extend()
pop()
remove()
reverse()
sort()

list comprehension Technique
----------------------------
-generating the values from the list and store the values in the list.
 is called list comprehension technique.
 
variable=[expression for loop condition]

[x for i in range(1,101)] --error 'x' not defined

[i for i in range(1,101)] --generates 1 to 100

[i*i for i in range(1,101)] --square number from 1 to 100

with out comprehension technique
-------------------------------
x=[]
for i in range(1,101):
    x.append(i*i)
print(x)

with out comprehension technique
--------------------------------
x=[]
for i in range(1,101):
  if i%2==0:
    x.append(i*i)
print(x)

x=[i*i for i in range(1,101) if i%2==0]


names=['SHIVANSHISH','SUSHMITHA','RACHANA','HARISH','SHANKAR']

names.lower()

prices=[100,200,400,3,500,230,450,234]

max(prices)

names=['SHIVANSHISH','SUSHMITHA','RACHANA','HARISH','SHANKAR']
        S             S            R         H       S





-------------------------------------------
tuple
-----
-tuple is a datastructure it acts a container
-tuple is immutable object 
              we can't add a element
			  we can't modify a element 
			  we can't delete a element 
-tuple follows sequence of order of values.
-tuple allows homogenous and hetrogenous elements
-tuple is not growable and shrinkable.
-tuple allows indexing it contains +ve and -ve index.
-tuple allows duplicate values.


how to create a tuple
----------------------
1)()
   or
2)tuple()

note:-    10,20,30,40  it is nothing tuple -->(10,20,30,40)

sequence of order of values			 
a
(40, 7, 90, 23, 45)

duplicate values
info=('darshan','darshan','free darshan','free darshana','sing with darshana')
info
('darshan', 'darshan', 'free darshan', 'free darshana', 'sing with darshana')


hetrogenous elements

info=('darshan',14,'tumkur','bachelor',True,3+4j)
info
('darshan', 14, 'tumkur', 'bachelor', True, (3+4j))


indexing
--------
a=(10,20,30,40)
a[0]
10
a[1]
20
a[2]
30
a[3]
40
a
a[4]

a[4]
IndexError: tuple index out of range

-ve indexing
------------
a[-3]
20

slicing concept in tuple
-----------------------
x=(10,20,30,40,50,60)
x[0:4]
(10, 20, 30, 40)
x[3:]
(40, 50, 60)
x[:3]
(10, 20, 30)

we can't modify a element
-------------------------
'tuple' object does not support item assignment
a[0]=100

tuple uses while loop
---------------------
while loop
a=(10,20,30,40,50,60)
print(a)
i=0
s=0
while i<len(a):
    s=s+a[i]
    i=i+1

print('sum of elements in tuple ',s)

tuple uses for loop
--------------------
for loop 
a=(10,20,30,40,50,60)
print(a)
s=0
for i in a:
    s=s+i

print('sum of elements in tuple ',s)

tuple concatination
--------------------
(10,20,30)+(40,50,60)
(10, 20, 30, 40, 50, 60)

tuple multplication
-------------------
(10,20,30)*3
(10, 20, 30, 10, 20, 30, 10, 20, 30)

unpack of tuple elements
----------------------
java,python,devops=(10,20,30)

java,python,devops=(10,20,30)
java
10
python
20
devops
30
java,python,devops=(10,20,30,40)
ValueError: too many values to unpack (expected 3)

java,python,devops=(10,20)
ValueError: not enough values to unpack (expected 3, got 2)

function on the tuple 
----------------------
max()
min()
avg=sum()/len()
sum()
all()
any()


a
(10, 20, 30, 40, 50, 60)
sum(a)
210
max(a)
60
min(a)
10
avg=sum(a)/len(a)
avg
35.0
all(a)
True
any(a)
True

methods in tuple
----------------
a
(10, 20, 30, 40, 50, 60)
a.count(40)
1
a.count(44)
0
a.index(40)
3
a.index(44)
ValueError: tuple.index(x): x not in tuple

tuple comprehension Technique
-----------------------------
-generating elements in the tuple and store the elements in tuple is called tuple 
 comprehension technique
 
variable=(expression forloop condition)

x=(i for i in range(1,101))
print(x) 
<generator object <genexpr> at 0x00000223209C31D0>

note:- tuple doesn't support comprehension technique



difference between list and tuple 
 
  list                              tuple 
  
list is a mutable object            tuple is immutable object.
list is slower                      tuple is fast 
list support comprehension          tuple doesn't support comprehension 
list is used where frequent         tuple is used where no modification 
updation is required                 is required.

set datastructure
-----------------
-set is a datastructure which acts a container
-set is a mutable object 
             add  a element 
			 modify a element
			 remove a element
-set is not ordered sequence values.
-set allow homogenous and hetrogenous elements.
-set doesn't support index.
-set doesn't allow duplicates.
-set is growable and shrinkable
-set allows only immutable objects.

how do you create a set ?

by default {} is a dictionary 

{}

and 

set()


a={}
type(a)
<class 'dict'>
a={10}
type(a)
<class 'set'>
a={10,20,5,12}
type(a)
<class 'set'>
b=set()
type(b)
<class 'set'>


a={10,2,3,4}
b={2,3,4,6}


while loop can't be applied on set.

for loop can be applied on set.

a={'apponix',10,20,'apponix'}
a
{10, 'apponix', 20}
for i in a:
    print(i)

    
10
apponix
20

indexing and slicing is not possible.


unpacking of set elements
--------------------------
java,python,devops={10000,20000,40000}
java
10000
python
20000
devops
40000

concatination of set objects are not possible.

set multiplication is not possible.

functions on the set.
--------------------
max()
min()
sum()
avg=sum()/len(v)
all()
any()

a={10,20,30,40,50,60}
a
{50, 20, 40, 10, 60, 30}
max(a)
60
min(a)
10
sum(a)
210
avg=sum(a)/len(a)
avg
35.0
all(a)
True
any(a)
True




first_day={'teju','rachana','prince'}
second_day={'prince','avinash','shankar'}

first_day-second_day --> 'teju','rachana'

second_day-first_day -->'avinash','shankar'

a={1,2,3}
b={3,4,5}


a-b ==>1,2 
b-a ==>4,5



a={1,2,3}
b={3,5,6}
a.difference(b)  -->1,2
b.difference(a) --->5,6

a.difference_update(b) -->1,2 
a -->1,2
b-->{3,5,6}
------------------------------

add()
clear()
copy()
discard()
difference()
difference_update()
intersection()
intersection_update()
remove()
pop()
update()
union()
symmetric_difference()
symmetric_difference_update()
isdisjoint
issubset
issuperset












--------------------------------------
set comprehension technique
--------------------------
generating elements in the set and storing the values in the set is called set comprehension technique.

syntax:-  {expression forloop condition}


x={i for i in range(1,101)}
print(x)

x={i*i*i for i in range(1,101)}
print(x)

frozenset is a immutable object.

fruits = {"Apple", "Banana", "Cherry", "Apple", "Kiwi"}
          
frozenset(fruits)
          
frozenset({'Banana', 'Cherry', 'Kiwi', 'Apple'})
basket=frozenset(fruits)
          
basket
          
frozenset({'Banana', 'Cherry', 'Kiwi', 'Apple'})
basket.add('dragonfruit')
          
Traceback (most recent call last):
  File "<pyshell#14>", line 1, in <module>
    basket.add('dragonfruit')
AttributeError: 'frozenset' object has no attribute 'add'

dictionary
----------
-dictionary is a datastructure acts as container 
-dictionary is a mutable object 
                  add a key values
				  modify key values
				  delete the key value
-dictionary contains key:value pair 
-each key:value pair is called as element or item
-key always must be unique 
-values can be may be duplicates.
-key must be immutable 
-values can be mutable or immutable 
-key and values can be both hetrogenous or homogenous elements.
-there is no index concept we can access values by using key.

we can create dictionary 2 ways

1){}
   or
2)dict()

1)x={'btech': 2010, 'mtech': 2012, 'phd': 2023}


2)dict()

y=dict(btech=2010,mtech=2012,phd=2023)
          
y
          
{'btech': 2010, 'mtech': 2012, 'phd': 2023}

crud/curd operation
--------------------
create-->adding-->addking key and value 
read-->fetching -->key value 
update-->modify   -->key value 
delete-->remove  -->key value 

y
          
{'btech': 2010, 'mtech': 2012, 'phd': 2023}
y['btech']
          
2010
y['mtech']
          
2012
y['phd']
          
2023
y['mba']
          
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    y['mba']
KeyError: 'mba'
y['btech']=2009
          
y
          
{'btech': 2009, 'mtech': 2012, 'phd': 2023}
del y['btech']
          
y
          
{'mtech': 2012, 'phd': 2023}
y['mba']=2020
          
y
          
{'mtech': 2012, 'phd': 2023, 'mba': 2020}
y['mtech']=2020
          
y
          
{'mtech': 2020, 'phd': 2023, 'mba': 2020}
y={'mtech': 2020, 'phd': 2023, 'mba': 2020,'mtech
   
SyntaxError: incomplete input
y={'mtech': 2020, 'phd': 2023, 'mba': 2020,'mtech':2022}
   
y
   
{'mtech': 2022, 'phd': 2023, 'mba': 2020}
y['btech']
   
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    y['btech']
KeyError: 'btech'
y.get('btech')
   


by applying for loop on dictionary we get only keys

info
{'java': 10000, 'python': 12000, 'devops': 13000, 'fsd': 50000, 'adf': 40000}
for i in info:
    print(i)

    
java
python
devops
fsd
adf

unpacking of dictionary
-----------------------
a,b,c={'java':12000,'python':13000,'devops':40000}
a
'java'
b
'python'
c
'devops'

functions on the dictionary

max()
min()
sum()
avg
all()
any()

methods in the dictioary

10 methods

clear()
copy()
get()
update(dict)
pop()
popitem()
items()
keys()
values()
setdefault()

dictionary comprehension technique
----------------------------------
-generating elements in the dictionary and store the items in the dictionary 

variable={expression forloop condition}


{t:t for t in range(1,101)}

{t:t*t for t in range(1,101)}

{t:t*t for t in range(1,101) if t%2==0}

info=[('siva','m',2000,10),('avinash','m',3000,10),('sushmitha','f',40000,20),
('rachana','f',35000,10),('tejashiwini','f',23000,20)]

o/p

{'m':5000,'f':98000}



FUNCTIONS
---------
-is a group of statement to perform the task.
-every function has name.
-every function is object.
-we should define the function and we should call the function.
-we can call the function any number of times.

below are the built in functions.
-print()
-id()
-type()
-len()

how to define the function
---------------------------
syntax:-  def functioname(parameter):
               statement1
			   statement2
			   :
			   :
			   statementn

how to call the function
------------------------
   functioname()


def avi_func():
    print('my name is avinash iam an actor')


rachana=avi_func
rachana()


note:- variable can act as a function  by taking functionname into a variable.

def addition():
    a=10
	b=20
	c=a+b
	print(c)

  
x=addition  
x()	

parameters
---------
while defining function declaring a variable is called as parameters

1)non-default 
2)default 
3)arbitary parameter

non-default : are defined at the defining a function.
              they are positional based.
			  compulsory provide the value.
	def addition(a,b):
     c=a+b
	 print(c)

addition() -error
addition(20,30)		  
			  
default parameter:are defined at the time of defining a function,
                  parameter we need to supply the value.
				  optional to provide the value.
				  
def addition(a=20,b=40):
     c=a+b
	 print(c)


addition()

arbitary parameter:- single variable can take zero or more values.

                    *variable.
					note:- internally arbitary parameter work as tuple.
					
def addition(*a):
     type(a)
	 print(a)


addition()


Arguments
----------
-while calling a function defining value/variable is called arguments

arguments are of two types

1)non-keyword arguments:- are positon based arguments
   def addition(x,y):
    z=x+y
    print(z)

addition(40,55)

-here 40,55 are non-keyword arguments.
   
2)keyword arguments :- name based arguments.

   def addition(x,y):
    z=x+y
    print(z)

addition(x=40,y=55)

 here x=40,y=55 are keyword arguments.


return statement
----------------
-whenever control is reached to return keyword in the function.
-function returns by default none and end the function.
-we can write multiple return statements.
-once first return statement reached and ignores the remaining statements.


def addition(x,y):
    z=x+y
    return 

output=addition(20,40)
print(output)

none 


def addition(x,y):
    z=x+y
    return None

output=addition(20,40)
print(output)

none 


def addition(x,y):
    z=x+y
    

output=addition(20,40)
print(output)

none 

def addition(x,y):
    z=x+y
    return
    return
    return 20

output=addition(20,40)
print(output)

abs(-10)  ->is a built in function returns the positive value.


own function by lakshmi
-----------------------

def abs_lak(a):
    if a<0:
        return -a
    else:
        return a

res=abs_lak(24)
print(res)


variables inside the functions
------------------------------
1)local variable
2)global variable


func1.py
-------------
institue_name='apponix'

def f1_avinash():
    pen1='brigh'
    print(institue_name)
    print('my pen name is ',pen1)

def f2_harish():
    pen2='doms'
    print(institue_name)
    print('my pen is ',pen3)

def f3_prince():
    pen3='linc'
    print(institue_name)
    print('my pen is ',pen)

f1_avinash()
f2_harish()
f3_prince()







Recursive function invocation
-----------------------------
-calling the function by itself is called recursive invocation.
-recursive invocation leads the infinity.
-to restrict the invocation we are using while loop in below example.

i=1
def func():
    global i
    print('hi')
    while i<5:
        i=i+1
        func()

func()


advantage
---------
below example.

factorial  of given number
---------------------------

5! = 5*4*3*2*1

def recur_fact(num):
    if num==1:
        return 1
    else:
        return num*recur_fact(num-1)

res=recur_fact(5)
print(res)


Lambda function/Anonymous function
-----------------------------------
-lambda function also as anonymous function
-by using lambda keyword we can define the anomyous functions
-we can't call the lambda functions
-is used execute only one time.


normal function
---------------
def addition(a,b):
     return a+b
	 
res=addition(5,6)
print(res)
	 
syntax:-  lambda  arguments :expression

def addition(a,b):
     return a+b
	 
res=addition(5,6)
print(res)

res=lambda a,b:a+b
output=res(10,20)
print(output)



Higher order function :-> function(function)

map()
filter()
reduce()

map(function, sequnce)



lb=[1,2,3,4,5,6,7,8]

def modf(x):
   return x+2
   
   
map(modf,lb)
   
--------------------------
z=[12,13,14,15,16]

r=list(map(lambda x:x+2,z))
print(r)


filter(function,object)

a=[1,2,3,4,5,6,7,8,9,10]

def even(x):
    if x%2==0:
	   return x 
	   
res=list(filter(even,a))
print(res)



reduce(function,object)

     a=[1,2,3,4,5]


     def add(x,y):
	     return x+y 

res=reduce(add,a)
print(res)

lambda

res=reduce(lambda x,y:x+y,a)
print(res)
























































