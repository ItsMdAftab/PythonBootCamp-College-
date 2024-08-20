#queue
#front rear
#the rear will be deleted first
#first in first out
queue=[]
size=int(input("enter the size of queue:"))
def insert(queue,item):
    if len(queue)==size:
        print("overflow")
    else:
        queue.append(item)
def delete():
    if len(queue)==0:
        print("overload")
    else :
        queue.pop(0) #first in first out need to be removed
def display():
    print(queue)
print('menu 1.insert 2.delete 3.display  4.exit')
l=1
while l!=0 :
    ch = int(input("enter the choice"))
    if (ch==1):
        item=int(input("Enter element"))
        insert(queue,item)
    elif ch==2:
        delete()
    elif ch==3:
        display()
    elif ch==4 :
        l=0
    else :
        print("enter the correct choice ")


    
