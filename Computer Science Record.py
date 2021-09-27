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
x=eval(input("Enter a tuple"))
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
    elif ch==3:
        val = Peek(Q)
        if val=="Underflow":
            print("Queue Empty")
        else:
            print("Front Item:",val)
    elif ch==4:
        Show(Q)
    elif ch==0:
        print("Bye")
        break
                                

#9
#TO IMPLEMENT PYTHON STRING FUNCTIONS
c=str(input("Enter sentence :"))
a=input("enter the spacing :")
print("The string entered is a word :",c.isalpha())
print("The string entered in lower case :",c.lower())
print("The string entered is in lower case :",c.islower())
print("The string entered in lower case :",c.upper())
print("The string entered is in lower case :",c.isupper())
print("The string entered after removing the space from left side :",c.lstrip())
print("The string entered after removing the space from right side :",c.rstrip())
print("The string entered contains whitespace :",c.isspace())
print("The string entered is titlecased :",c.istitle())
print("The string entered after joining with ",a,":",a.join(c))
print("The string entered after swaping case :",c.swapcase())


#10
#TO READ AND DISPLAY FILE CONTENT LINE BY LINE WITH EACH WORD SEPARATED BY #
a=open(r"C:\Users\Jammy\Documents\Abhishek\Python\TEXT.txt,","r")
lines=a.readlines()
for line in lines:
    x=line.split()
    for y in x:
        print(y+"#",end="")
    print("")

    
#11
#TO REMOVE ALL THE LINES THAT CONTAIN THE CHARACTER 'A' IN A FILE & WRITE IT TO ANOTHER FILE
file=open(r"C:\Users\Jammy\Documents\Abishek\Python\TEXT1.txt","r")
lines=file.readlines()
file.close()
file=open(r"C:\Users\Jammy\Documents\Abishek\Python\TEXT1.txt","w")
file=open(r"C:\Users\Jammy\Documents\Abishek\Python\MODTEXT1.txt","w")
for line in lines:
	if 'a' in line :
		file1.write(line)
	else:
		file.write(line)
print("Lines that contain a character are removed from TEXT1")
print("Lines that contain a character are added in MODTEXT1")
file.close()
file1.close()


#12
#TO READ CHARACTERS FROM KEYBOARD ONE BY ONE ALL LOWER CASE LETTERS STORED INSIDE A FILE "LOWER",
#ALL UPPERCASE LETTERS STORED INSIDE A FILE "UPPER",& ALL OTHER CHARACTERS STORED INSIDE "OTHERS"
f1=open(r"C:\Users\Jammy\Documents\Abhishek\Python\LOWER.txt","w")
f2=open(r"C:\Users\Jammy\Documents\Abhishek\Python\UPPER.txt","w")
f3=open(r"C:\Users\Jammy\Documents\Abhishek\Python\OTHERS.txt","w")
print('Input "~" to stop execution.')
while True:
	c=input("Enter a single character :")
	if c=="~":
		break
	elif c.islower():
		f1.write(c)
	elif c.isupper():
		f2.write(c)
	else:
		f3.write(c)
f1.close()
f2.close()
f3.close()


#13
#CREATE A BINARY FILE WITH NAME & ROLL NUMBER. SEARCH FOR A GIVEN ROLL NUMBER AND DISPLAY NAME, IF NOT FOUND DISPLAY
#APPROPRIATE MESSAGE
import pickle
sdata=[]
slist=[]
totals=int(input("Enter number of students :"))
for i in range(totals):
	sdata["Roll no."]=int(input("Enter roll no. :"))
	sdata["Name"]=input("Enter name :")
	slist.append(sdata)
	sdata=()
a=open(r"C:Users\Jammy\Documents\Abhishek\Python\TEXT2.dat","wb")
pickle.dump(slist,a)
a.close()

x=open(r"C:Users\Jammy\Documents\Abhishek\Python\TEXT2.dat","rb")
slist=pickle.load(x)
b=int(input("Enter the roll number of student to be searched :"))
y=False
for TEXT2 in slist:
	if (TEXT2["Roll no."]==b):
		y=True
		print(TEXT2["Name"],"Found in file")
if (y==False):
	print("Data of student not found.")
	

#14
#TO CREATE A BINARY FILE WITH ROLL NUMBER, NAME & MARKS, INPUT A ROLL NUMBER & UPDATE THE MARKS.
import pickle

sdata={}
totals=int(input("Enter number of students :"))
a=open(r"C:\Users\Jammy\Documents\Abhishek\Python\TEXT3.dat","wb")
for i in range(totals):
	sdata["Roll no"]=int(input("Enter roll no. :"))
	sdata["Name"]=input("Enter name :")
	sdata["Marks"]=float(input("Enter marks :"))
	pickle.dump(sdata,a)
	sdata={}
a.close()

#UPDATING MARKS

found=False
rollno=int(input("Enter roll number :"))
a=open(r"C:\Users\Jammy\Documents\Abhishek\Python\TEXT3.dat","rb+")
try:
	while True:
		pos=a.tell()
		sdata=pickle.load(a)
		if (sdata["Roll no"]==rollno):
			sdata["Marks"]=float(input("Enter new marks :"))
			
			a.seek(pos)
			pickle.dump(sdata,a)
			found=True
except EOFError:
	if found==False:
		print("Roll number not found.")
	else:
		print("Students marks updated successfully.")
	a.close()
	
	
#15
#Input Data
import csv
with open(r'C:\Users\Jammy\Documents\Abhishek\Python\employee.txt','a') as csvfile:
	mywriter = csv.writer(csvfile,delimiter=',')
	ans='y'
	while ans.lower()=='y':
		eno=int(input("Enter Employee ID :"))
		name=input("Enter Employee Name :")
		mobno=int(input("Enter Employee Mobile No :"))
		mywriter.writerow([eno,name,mobno])
		ans=input("Do You Want To Enter More Data? (y/n):")
ans='y'

#Search Empid And Display The Records

with open(r'C:\Users\Jammy\Documents\Abhishek\Python\employee.txt','r') as csvfile:
	myreader = csv.reader(csvfile,delimiter=',')
	ans='y'
	while ans.lower()=='y':
		found=False
		e = int(input("Enter Employee ID to search :"))
		for row in myreader:
			if len(row)!=0:
				if int(row[0])==e:
					print("Name :",row[1])
					print("Mobile no. :",row[2])
					found=True
					break
				if not found:
					print("Employee ID not found.")
		ans = input("Do You Want To Search More? (y/n):")
ans='y'

with open(r'C:\Users\Jammy\Documents\Abhishek\Python\employee.txt','a') as csvfile:
	x=csv.writer(csvfile)
	x.writerow([eno,name,mobno])
	
	
#16
#Write a programme to create Lpush() and Lpop() function to do push and pop operation
#on a stack using a list e.g. take a student information and push and pop the details
def isEmpty(S):
	if len(S)==0:
		return True
	else:
		return False
def Push(S,item):
	S.append(item)
	top=len(S)-1
def Pop(S):
	if isEmpty(S):
		return "UNDERFLOW"
	else:
		val=S.pop()
	return val
#main function begins here
S=[]
top=None
while True:
	print("***STACK DEMONSTRATION***")
	print("1. PUSH")
	print("2. POP")
	print("0. EXIT")
	ch=int(input("Enter your choice :"))
	if ch==1:
		val=int(input("Enter the item of Push :"))
		Push(S,val)
	elif ch==2:
		val=Pop(S)
		if val=="UNDERFLOW":
			print("STACK IS EMPTY")
		else:
			print("Deleted Item was:", val)
	elif ch==0:
		print("THANK YOU")
		break
		
		
#17
use studentdb;
create table student
(roll int not null,
studentname varchar(30) not null,
class char(5) not null,
section char(1) not null,
classstream char(20) not null);
desc student;
insert into student values
(1,"Akhil", "XII", "A", "Science"),
(2, "Satya", "XII", "C", "Science"),
(3, "Antony", "XII", "D", "Commerce"),
(4, "Vishal", "XII", "E", "Humanities"),
(5, "Deepak", "XII", "A", "Science"),
(6, "Brij", "XII", "B", "Science");
select * from student;
alter table student
add(Substream char(20) not null),
(Percentage float not null);
desc student;
update student set Substream = "Computer Science" where roll = 1;
update student set Substream = "Biology" where roll = 2;
update student set Substream = "Maths" where roll = 3;
update student set Substream = "NA" where roll = 4;
update student set Substream = "Computer Science" where roll = 5;
update student set Substream = "Computer Science" where roll = 6;
select * from student;
update student set Percentage = 81 where roll = 1;
update student set Percentage = 69 where roll = 2;
update student set Percentage = 92 where roll = 3;
update student set Percentage = 55 where roll = 4;
update student set Percentage = 85 where roll = 5;
update student set Percentage = 72 where roll = 6;
alter table student add(Adhaar_card biginit not null);
desc student;
alter table student
drop coloumn Adhaar_card;
desc student;
select studentname,section from student order by Percentage;
select avg(Percentage) from student;
select count(*) from student;
select min(Percentage) from student;
select max(Percentage) from student;
select sum(Percentage)/count(*) from student where Substream = "Computer Science"
delete from student where classstream = "Science";
select * from student;


#18
#program to Integrate SQL with Python by importing the MYSQL module record of employee and display the record.

import mysql.connector as pysql
conn=pysql.connect(host="localhost", user = "root", passwd = "q2w3e4r5t6y7", database = "empdb")
cur=conn.cursor()
cur.execute("select * from employee")
for x in cur:
	print(x)
	
	
#19
import mysql.connector as pysql
conn=pysql.connect(host = "localhost", user = "root", passwd = "q2w3e4r5t6y7", database = "empdb")
cur=conn.cursor()
ans='y'
while ans.lower()=='y':
	empno=int(input("enter the emp_no to search:"))
	query='select * from employee where emp_no=()'.format(empno)
	cur.execute(query)
	result=cur.fetchall()
	if cur.rowcount==0:
		print("sorry not found")
	else:
		print("%10s"%"Emp_no","%20s"%"emp_name","%15s"%"dept","%10s"%"hire_data","%10"%"hire_data","%10s"%"salary")
		for row in result:
			print("%10s"%row[0],"%20s"%row[1],"%15s"%row[3],"%10s"%row[4])
	ans=input("seaarch one more? [y/n]:")
	
	
#20
import mysql.connector as pysql
conn=pysql.connect(host = "localhost", user = "root", passwd = "q2w3e4r5t6y7", database = "studentdb")
cur=conn.cursor()

roll=int(input("Enter roll number:"))
perc=int(input("Enter new percentage:"))

print("Before updating record:")
query1 = 'select * from student where roll=()'.format(roll)
cur.execute(query1)
record = cur.fetchone()
print(record)

query2='update student set Percentage = () where roll=()'.format(perc,roll)
cur.execute(query2)
conn.commit()
record = cur.fetchone()

print("After updating record:")
query3 = 'select * from student where roll=()'.format(roll)
cur.execute(query3)
record = cur.fetchone()
print(record)
