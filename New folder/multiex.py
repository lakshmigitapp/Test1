class Finance:
    def __init__(self):
        self.__revenue=10000
        self.number_of_sales=14
    def display(self):
        print(self.__revenue)
        
f1=Finance()
print(f1.__dict__)


