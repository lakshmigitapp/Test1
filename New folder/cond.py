name='tejashwini'
name[0:9:1]
'tejashwin'
name[0:9:2]
'tjswn'
name[0:9:3]
'taw'
name[0:9:-1]
''
name[9:0:-1]
'iniwhsaje'
name[::-1]
'iniwhsajet'
   
   
string methods
--------------
a='lakshmi'
a.capitalize()
'Lakshmi'
a='lakshmi narayana'
a.capitalize()
'Lakshmi narayana'
a.title()
'Lakshmi Narayana'
a.upper()
'LAKSHMI NARAYANA'
a.lower()
'lakshmi narayana'
a='sAjiNa'
a.swapcase()
'SaJInA'

name='lakshmi narayana'
name.find('y')
12
name.find('ya')
12
name.find('ay')
11
name='lakshmi narayana'
name.find('a')
1
name.find('a',9,16)
9
name.find('g',9,16)
-1

find()
------
format method()
---------------
index()

name='lakshmi narayana'
name.index('y')
12
name.index('a',9,16)
9
name.index('g',9,16)
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    name.index('g',9,16)
ValueError: substring not found


join() method
-------------

'lak'+'shmi'-->lakshmi  

'lakshmi'-->'l#a#k#s#h#m#i'

'#'.join('lakshmi')


lakshmi --> l a k s h m i 

' '.join('lakshmi')

'#'.join('lakshmi')
'l#a#k#s#h#m#i'
name='#'.join('lakshmi')
name
'l#a#k#s#h#m#i'

name='teju'
'@'.join(name)
't@e@j@u'
name='rachana ramesh'
' '.join(name)
'r a c h a n a   r a m e s h'

strip()
------
lstrip()
-------
rstrip()
-------


name='     prince    '
name
'     prince    '
name.strip()
'prince'
name.lstrip()
'prince    '
name.rstrip()
'     prince'

split()
-------
txt='welcome to apponix'
txt
'welcome to apponix'
txt.split()
['welcome', 'to', 'apponix']
txt.split('l')
['we', 'come to apponix']
txt.split('a')
['welcome to ', 'pponix']
txt.split('e')
['w', 'lcom', ' to apponix']
txt='welcome,satyabama,teastal'
txt.split(',')
['welcome', 'satyabama', 'teastal']
txt='welcome,satyabama teastall'
txt.split()
['welcome,satyabama', 'teastall']
txt='teju'
txt.split('k')
['teju']


control flow statement
----------------------
-used to control the flow of statement in python.
-in python statements will be execute from top to bottom.

conditional statements
-----------------------
1)simple if
2)if..else..
3)elif 
4)nested if


looping statements
------------------
1)while loop
2)for loop



simple if :-
-----------
if block checks the condition .if condition is true execute the block 
otherwise skip the block.

syntax:-  if condition:
             statement
			 statement
			 statement
		  statment

print('start')
age=10
if age>=18:
    print('your are old enough to vote')
	print('iam learning python from lakshmi')
print('end of my program')


print('start the kick')
beer_price=200
if beer_price<240:
    print('enjoy the drink alone')
    print('boring')
print('end of kick')

if..else..
===========
syntax:-  if condition:
              block of statements
		  else:
		      block of statements
			  
if condition is true then execute the true block 
else execute the false block			  

print('shankar program started')
raining=True
if raining:
   print('take the umbrella and go to movie')
else:
   print('watch movie in hotstar')
print('shankar program ended')


a=10
b=20 

if a>b:
   print(' a is bigger')
else:
   print('b is bigger')


elif condition:
    block of statements
	
	
-elif condition can not be used individually, we must use if before elif.
-after if condition we can have number of elif conditions.



print(' program started')
a=30
b=30

if a>b:
    print('a is bigger')
elif a==b:
    print(' a and b are same')
else:
   print('b is bigger')

print(' program ended')



at among 3 numbers?

print('start')
a=10
b=20
c=30
if a>b:
   print('a is bigger')
elif a>c:
   print('a is bigger')
elif b>c:
   print('b is bigger')
else:
   print('c is bigger')
print('end')

a=20
b=60
c=40

big=a 
if b>big:
   big=b
if c>big;
   big=c 

print('biggest is ',big)  




Nested if 
----------
if block inside if block is called nested if.

syntax:-  if condition:
             statemetns
			 if condition:
			     statement
			 else:
			     statements
		 else:
		     statements 
			 
age=16
graduated=False
hasLicense=True

if age>=18:
   print('you are eligible for driving test')
   if graduated:
       print('you are graduated very good')
   if hasLicense:
       print('enjoy the driving')
else:
   print('wait for youngagement')

Looping statement
-----------------
-are used to execute the statements repeatdly.
-write once and execute several times.

1)while loop 
2)for loop 

while loop:-
----------
sytnax:-   while condition:
                statement1
				statement2
				 :
				 :
				statementn
           main statement

1-10 

i=10
while i>=1:
    print(i)
    i=i-1

1-10  even number

i=1
while i<=100:
    if i%2==0:
        print(i)
    i+=1

break statement:-
---------------
break statement is used in looping statements.
break statement is exit from the loop.

1-20
 5 exit

i=1
while i<=20:
    print(i)
    if i==5:
        break;
    i+=1
print('end of program')


while condition:
    block of statemetns
else:
    block of statements


i=1
while i<=10:
    print(i)
    if i==3:
        break
    i+=1
else:
   print('end of program')
    print('end of program')


for loop
--------
syntax:-   for variable in object:
               block of statements
			   
			  
ex1:-   for i in 'lakshmi':
            print(i) 
			
		l
		a 
		k 
		s 
		h 
		m 
		i 

ex2:-   for i in 'lakshmi':
           print(i,end=" ")
		   
		l a k s h m i


















