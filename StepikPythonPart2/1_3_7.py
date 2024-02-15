def printab(a, b, *args):
    print('positional argument a ', a)
    print('positional argument b', b)
    print('additional arguments:')
    for arg in args:
        print(arg)

printab(10, 20, 30, 40, 50)
# positional argument a 10
# positional argument b 20
# additional arguments:
# 30
# 40
# 50
