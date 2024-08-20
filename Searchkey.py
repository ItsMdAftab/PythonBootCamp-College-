#searching is the proess of finding some particular element in the list .
#if the element is present in the list.
#1.linear search.
'''
l=[]
n=int(input("enter the size: "))
for i in range(n):
    l.append(int(input("enter the next element: ")))
print(l)
target=int(input("Enter target: "))
def linear(l,target):
    for i in range(len(l)):
        if target==l[i]:
            return 1
    return -1
result=linear(l,target)
if result!=-1:
    print("found")
else:
    print("not found")
    '''
#Binary search
#write a program to 
l=[]
n=int(input("enter the size: "))
for i in range(n):
    l.append(int(input("enter the next element: ")))
targe =45
l.sort()
low=0
high=len(l)-1
mid=int(low+high/2)
print(l[mid])
if target==a[mid]:
    return 1
elif a[mid]<target:
    low=mid+1
else :
    high=mid-1
return -1
result=binary(a,target)
if result!=-1:
    print("found")
else:
    print("not found")
    



    



