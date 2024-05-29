# for i in range(1,5):
#     for j in range(1,7):
#         if i==1 or j==1 or j==6 or i==4:
#             print('*',end=" ")
#         else:
#             print(' ',end=" ")
#     print()

# for i in range(1,6):
#     for j in range(1,i+1):
#         print("*",end=" ")
#     print()     

# for i in range(1,6):
#    for j in range(1,i+1):
#        print("*",end=" ")
#    print()
# for i in range(1,5):
#    for j in range(5-i):
#       print('*',end=" ")
#    print()
    
    
for i in range(1,6): 
    for j in range(1,6-i):
        print(" ",end=" ")
    for k in range(0,2*i-1):
        print("*",end=" ")
    print()
        

