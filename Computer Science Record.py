#1
#TO LINEAR SEARCH AN ELEMENT IN A LIST AND DISPLAY THE FREQUENCY AND LOCATION
def fun(l,x):
    count=0
	for i in range(0,len(l)):
    	if l[i]==x:
        	print("Found location :",i)
            count+=1
			print("Frequency of element :",count)
a=eval(input("Enter a list :"))
b=eval(input("Element to be searched :"))
fun(a,b)


#2
#2
#TO BINARY SEARCH AN ELEMENT IN A LIST AND DISPLAY THE FREQUENCY AND LOCATION
def fun(l,a):
	count=0
    low=0
    high=len(l)-1
    while low<=high:
    	mid=int((low+high)/2)
        if a==l[mid]:
        	count+=1
            return("Element found!,index :",mid,"Frequency :",count)
        elif a<l[mid]:
        	high=mid-1
        else:
        	low=mid+1
x=eval(input("Enter a list :"))
y=eval(input("Enter the element to search :"))
print(fun(x,y))


#3
#TO PASS LIST & DOUBLE THE ODD VALUES AND HALF EVEN VALUES & DISPLAY THE CHANGED LIST
def f(l):
    l2=[]
    for i in range(0,len(l)):
        if l[i]%2==0:
            e=l[i]/2
            l2.append(e)
        else:
            e=l[i]*2
            l2.append(e)
    print(l2)
a=eval(input("Enter a list :"))
f(a)


#4
#TO INPUT N NUMBERS IN TUPLE & COUNT HOW MANY EVEN & ODD NUMBERS ARE ENTERED
def fun(l):
	e=0
    o=0
    for i in range(0,len(l)):
    	if l[i]%2==0:
        	e+=1
        else:
        	o+=1
        print("Number of even numbers :",e,"Number of odd numbers :",o)
x=eval(input("Enter a tuple :"))
fun(x)


#5
#TO UPDATE THE KEY AND VALUE OF EXISTING DICT ENTERED BY USER
def fun(d,k):
	value2=eval(input("Enter the value :"))
    d[k]=value2
    print("Updated dictionary :",d)
x=int(input("Number of pairs in dictionary :"))
dic={}
for i in range(x):
	key=eval(input("Enter the key :"))
    value=eval(input("Enter the value :"))
    dic[key]=value
print("Original dictionary :",dic)
a=(eval(input("Enter the key whose value you want to change :")))
fun(dic,a)


#6
#TO COUNT HOW MANY VOWELS PRESENT IN THE STRING
def fun(l):
	count=0
    for i in range(0,len(l)):
    	if l[i]=="a" or l[i]=="A" :
        	count+=1
        if l[i]=="e" or l[i]=="E" :
        	count+=1
        if l[i]=="i" or l[i]=="I" :
            count+=1
        if l[i]=="o" or l[i]=="O" :
            count+=1
        if l[i]=="u" or l[i]=="U" :
            count+=1
 print("Number of vowels :",count)
a=eval(input("Enter a string :"))
fun(a)


#7
#TO GENERATE RANDOM NUMBERS BETWEEN 1 AND 6 USING USER DEFINED FUNCTION
def fun():
	import random
    r=random.randint(1,6)
    print("Random number generated between 1 to 6 :",r)
fun()


#8
def isEmpty(Q):
	if len(Q)==0:
    	return True
    else:
        return False

def Enqueue(Q,item):
	Q.append(item)
    if len(Q)==1:
    	front=rear=0
    else:
    	rear=len(Q)
def Dequeue(Q):
	if isEmpty(Q):
    	return "Underflow"
    else:
    	val = Q.pop(0)
    if len(Q)==0:
    	front=rear=None
        return val
def Peek(Q):
	if isEmpty(Q):
    	return "Underflow"
    else:
    	front=0
        return Q[front]
def Show(Q):
   	if isEmpty(Q):
       	print("Sorry No items in Queue ")
    else:
        t = len(Q)-1
        print("(Front)",end='')
        front = 0
        i=front
        rear = len(Q)-1
        while(i<=rear):
	   	    print(Q[i],"==>",end='')
            i+=1
        print()
Q=[ ] #Queue
front=rear=None
while True:
	print("**** QUEUE DEMONSTRATION ******")
    print("1. ENQUEUE ")
    print("2. DEQUEUE")
    print("3. PEEK")
    print("4. SHOW QUEUE ")
    print("0. EXIT")
    ch = int(input("Enter your choice :"))
    if ch==1:
    	val = int(input("Enter Item to Insert :"))
        Enqueue(Q,val)
    elif ch==2:
        val = Dequeue(Q)
        if val=="Underflow":
    	    print("Queue is Empty")
        else:
            print("\nDeleted Item was :",val)
                                
