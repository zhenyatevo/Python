class Counter:
    def __init__(self, start = 0):
        self.count = start


Counter # class object
x = Counter(10) # x is instance object
x.count = 0 # 0
x.count +=1
