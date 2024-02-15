class MyList(list):
    def even_length(self):
        return len(self) % 2 == 0

x = MyList()
print(x) # []
x.extend([1, 2, 3, 4, 5])
print(x) # [1, 2, 3, 4, 5]
print(x.even_length()) # False
x.append(6)
print(x.even_length()) # True
