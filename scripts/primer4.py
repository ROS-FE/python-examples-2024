#! /usr/bin/python3
import time


#+ - * / % // **
#| & ^ << >>
#and or not
# == > < <=
# None - spremenljivka is not None

if None is None:
    if 1 == 1:
        pass
elif None is not None:
    pass
else:
    pass

#while True:
#    pass

for i in range(10):
    print(i)

for i in range(88, 103,5):
    print(i)

test = [6, 3, 5]

for st in test:
    print(st)

test2 = [x for x in test if x>4]
print(test2)

while True:
    pass
    if True == True:
        break

def imeFunkcije(a, b):
    a = 7
    b = b**2
    return a*b +a/b

fun1 = lambda a: a+a**2
def fun1(a):
    return a+a**2

def main():
    print("Hello world!")

if __name__ == "__main__":
    main()