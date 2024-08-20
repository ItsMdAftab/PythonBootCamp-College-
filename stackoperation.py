stack=[]
size=int(input("enter the size of stack "))
def push(stack,item):
    if len(stack)==size:
        print("overflow")
        return
    else :
        stack.append(item)
def pop():
    
    if len(stack)==0:
        print("stack underflow")
    else:
        stack.pop()
    print(len(stack))
def display():
    print(stack)
def peek():
    n=len(stack)
    print(stack[n-1])
#push operation for saving data in stack
#pop operation for retriving data from stack
print('menu 1.push 2.pop 3.display 4.peek 5.exit')
l=10
while l!=0 :
    ch = int(input("enter the choice"))
    if (ch==1):
        item=int(input("Enter element"))
        push(stack,item)
        print(len(stack))
    elif ch==2:
        pop()
    elif ch==3:
        display()
    elif ch==4:
        peek()
    elif ch==5 :
        l=0
    else :
        print("enter the correct choice ")
