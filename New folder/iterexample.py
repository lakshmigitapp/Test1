def outer():
    a=10
    def inner(b):
      print(a+b)
    return inner
   

res=outer()
res(40)
