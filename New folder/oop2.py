class Father:
    def __init__(self):
        print('father constructor called')
        self.vehicle='scooter'
        print(self.vehicle)

class Son(Father):
    
    def __init__(self):
        super().__init__()
        print('son constructor called')
        self.vehicle='BMW'
        print(self.vehicle)


s=Son()
