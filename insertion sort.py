#write a python program for creating a module with all arthmetic operation , finding factorial
#printing all the elements of the list:
def arth(a,b):
    print(a+b)
    print(a-b)
    print(a*b)
    print(a%b)
    print(a/b)
    print()
def fact(a):
    fact=1
    for i in range(1,a+1):
        fact*=i
    return fact
def prlist(l):
    for i in range(len(l)):
        print(l[i])
a=3
b=2
l=[1,2,3,4,5]
arth(a,b)
print(fact(a))
print()
prlist(l)





