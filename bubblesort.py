#sorting : arrange element in particluar order (accesding or descending : )
"""
sorting techniques :
1. bubble sort
2.selection sort
3.insertion sort

BUBBLE SORT:
it arrange the element either in assending or desending order
it compares the first two element and swap
"""
"""
l=[100,1,2,3,4,6,7,4,3,2]
for i in range(len(l)):
    for j in range(i,len(l)):
        if (l[i]>l[j]):
            t=l[j]
            l[j]=l[i]
            l[i]=t
            
print(l)
"""
#Selection sort example:
"""
selection sort is an algorithm that selects the smallest element
from an unsorted list in each iteration and places that element
at the beginning of the unsorted list .
"""
A=[3,4,5,7,8,0]

for i in range(len(A)):
    min_idxs=i
    for j in range(i+1,len(A)):
        if A[min_idx]>A[j]:
            min_idx=j
        A[i],A[min_idx]=A[min_idx],A[i]
print("sorted array")
for i in range(len(A)):
    print("%d"%A[i])

