def g():
    print("I m in function g")
def f():
    print("I m in function f")
    g()
    print("I am in function f")
print("I an outside of any function")
f()
print("I am outside of any function")
