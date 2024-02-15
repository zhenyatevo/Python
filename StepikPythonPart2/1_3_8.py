def printab(a, b, **kwargs):
     print('positionl argument a ', a)
     print('positional argument b ', b)
     print('additional argumants:')
     for key in kwargs:
         print(key,kwargs[key])
         
printab(10, 20, c=30, d=40, jimmin=123)
# positionl argument a 10
# positional argument b 20
# additional argumants:
# d 40 
# jimmi 123
# c 30
