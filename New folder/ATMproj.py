upin=int(input('Enter your pin'))

f=open('pin.txt')
fpin=int(f.read())



if upin==fpin:
    print('pin is correct')
    fb=open('bal.txt','r')
    bal=int(fb.read())
    fb.close()
    print('your balance is ',bal)
    print("Enter your choice 1.withdraw 2.deposit")
    n=int(input())
    if n==1:
        print('Enter the amount withdraw')
        amount=int(input())
        bal=bal-amount

    elif(n==2):
        print('Enter the amount deposit')
        amount=int(input())
        bal=bal+amount
    f=open('bal.txt','w')
    f.write(str(bal))
    f.close()

    
    

else:
    print('incorrect pin')
