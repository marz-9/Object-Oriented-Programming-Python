from math import *
def sqrtfind(x):

    l=1
    h=x
    if (x==1 or x==0):
        return x
    
    while l<=h:
        mid=(l+h)//2
        if (mid*mid==x):
            return mid
        elif (mid*mid<x):
            l=mid+1   
        else:
            h=mid-1
    return -1
                


n=int(input("Enter a number:"))
reslt=print("Your target is in index: ",sqrtfind(n))


#     sq=[]
#     if (n>0):
#         j=n
#         while (j>=0):
#             for x in range (int(sqrt(n))+1):
#                 sq.append(int(sqrt(n)))
#     else:
#         print("Please enter non-negative number") 