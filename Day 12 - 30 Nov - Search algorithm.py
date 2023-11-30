def binarysearch(key, list1):
    
    
    l=0
    h=len(list1)-1
    while l<=h:
        mid=(l+h)//2
        if (list1[mid]==key):
            return mid
        elif (list1[mid]<key):
            l=mid+1
            
        else:
            h=mid-1
    return -1
    
list1=[4,34,6,8,2,11,100]
list1.sort()
key=int(input("enter a num : "))
print(list1)
reslt=print("Your target is in index: ",binarysearch(key,list1))