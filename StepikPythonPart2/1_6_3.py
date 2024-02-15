class EvenLengthMixin:
    def even_length(self):
        return len(self) % 2 ==0


class MyList(list, EvenLengthMixin):
    def pop(self):
        x = super(MyList, self).pop()
        print('Last value is', x)
        return x

ml = MyList([1, 2, 4, 17])
z = ml.pop() # Last  value is 17
print(z) # 17
print(ml) # [1, 2, 4]
