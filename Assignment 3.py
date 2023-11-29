#Question 1
from random import *
def rolling_dice(sum1):
    d1=randint(1,6)
    d2=randint(1,6)
    sum1=d1+d2
    if (sum1== 2 or sum1== 3 or sum1==12):
        print("You rolled {} + {} = {}".format(d1,d2,sum1))
        print("You lose")
    elif (sum1== 7 or sum1== 11):
        print("You rolled {} + {} = {}".format(d1,d2,sum1))
        print("You Win")
    else:
        print("You rolled {} + {} = {}".format(d1,d2,sum1))
        print("Point is: ",sum1)
        pt=sum1
        while (True):
            d3=randint(1,6)
            d4=randint(1,6)
            sum2=d3+d4
            if(sum2 == 7):
                print("You rolled {} + {} = {}".format(d3,d4,sum2))
                print("You lose")
                break
            elif (sum2 == pt):
                print("You rolled {} + {} = {}".format(d3,d4,sum2))
                print("You Win")
                break
roll=0
rolling_dice(roll)

#Question 2
def index_of_smallest_element(list1):
    small=[]
    for y in range(list1):
        val=int(input("Enter {} numbers: ".format(list1)))
        small.append(val)
    print("The indx of smallest number: ",small.index(min(small)))
            
index_of_smallest_element(10)

#Question 3
def eliminate_duplicate(n):       
    s=[]
    for i in range(1,n+1):
        values=int(input("Enter {} numbers: ".format(n)))
        s.append(values)
    
    result=set(s)
    list_=list(result)
    print("The distinct numbers are: ",*list_, end=" ")

eliminate_duplicate(10)
