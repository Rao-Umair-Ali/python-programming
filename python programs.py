
#---------------how to print any thing-------------
#print("hello world")

#---------------how to assign value ---------------
#a=3
#b=4

#---------------how to convert assign value into integer and applu mathematical operation----------------

#a=input()
#c=float(a)
#b=input()
#d=float(b)
#print(c+d)
#print(c-d)
#print(c*d)
#print(c/d)

#---------------How to show some thing when you want input

#a=input("enter 1st value")
#c=input("enter 2nd value")


#----------------2nd way to convert string into integer------------

#a=int(input())
#b=int(input())

#---------------percentage calculator-----------------

#obtained_marks = int(input("Obtained marks"))
#Total_marks = int(input("Total marks"))
#percentage = (obtained_marks/Total_marks)*100
#print("your percentage :" , percentage ,"%")


#--------------discount percentage -------------------------

#disprice=int(input("New price :"))
#oldprice=int(input("old price :"))
#discountedamount=(oldprice-disprice)
#print("discounted amount :",discountedamount)
#discountpercentage=(disprice/oldprice)*100
#print("discountpercentage : ",discountpercentage"%")


#-------------all mathematical operator----------
#a=5
#b=6
#c=7
#d=8
#e=a*b+c-d/a+(c**2)
#print(e)

#-------------assignment number 3 ---------------
##
##discountsprice=int(input("disprice"))
##discountpercent=int(input("d.p"))
##oriinal=(discountsprice/discountpercent)*100
##print(oriinal)

##------------------Assignment no 1-----------------
##obtained_marks=int(input("Enter Obtained marks"))
##total_marks=int(input("Enter Total marks"))
##percentage =(obtained_marks/total_marks)*100
##print(percentage)
##
##------------------Assignment no 2-----------------
##r=int(input("give me a radius "))
##pi=3.141592653589793238
##circumferenceofcircle=2*pi*r
##print("circumference of circle = ",circumferenceofcircle)
##A=pi*(r**2)
##print("Area of circle = ",A)
##
##------------------Assignment no 3-----------------
##original_price=int(input("original_price"))
##discounted_percentage=int(float(input("discounted_percentage")))
##discounted_price=(discounted_percentage/100)*original_price
##print("discounted price = " , discounted_price)
##
##------------------Assignment no 4-----------------
##discounted_price=int(input("discounted_price"))
##discounted_percentage=int(float(input("discounted_percentage")))
##original_price=(discounted_price/discounted_percentage)*100
##print(original_price)
##
##------------------Assignment no 5-----------------
##volt=int(input("give me volt"))
##ampere=int(input("give me ampere "))
##p=volt*ampere
##print(p)
##------------------Assignment no 6-----------------
##a=int(input("side a"))
##b=int(input("side b"))
##h=int(input("perpendicular distance "))
##k=h*((a+b)/2)
##print("Area of trapezoid ",k)
##
##------------------Assignment no 7-----------------
##a=int(input("give me a number "))
##if(a%2==0):
##    print("even")
##else:
##    print("odd")
##
##------------------Assignment no 8-----------------
##d=int(input("side a"))
##a=float(d)
##e=int(input("side b"))
##b=float(e)
##f=int(input("side c"))
##c=float(f)
##s=(a+b+c)/2
##print("semiperimeter",s)
##first=(s-a)
##second=(s-b)
##third=(s-c)
##product=first*second*third
##Areaoftriangle=product*s
##print("Area of triangle",Areaoftriangle)
##-----------------Assignment no 9------------------
##x=int(input())
##y=int(input())
##if (x<=10 and x>=-10 and y<=10 and y>=-10):
##    print("point on line")
##else:
##    print("point not line")
####-----------------Assignment no 10------------------
##a=int(input())
##b=int(input())
##i=2
##while True:
##    r1=a%i
##    r2=b%i
##    if(r1==0):
##        if(r2==0):
##            print(i)
##    i+=1
##  
####-----------------Assignment no 11------------------
##a=int(input("enter first number"))
##b=int(input("enter second number "))
##i=a
##while i>=a and i<=b :
##    if i%2==0:
##        print(i)
##    i+=1
##    
#write a program and takes 2 positive integer number from the user and prints all the common divisors.
##User_input1 = int(input("Enter number: "))
##User_input2 = int(input("Enter number: "))
##common_divisor = []
##for i in range(1,User_input1 + 1) and range(1,User_input2 + 1):
##        if User_input1 % i == 0 and User_input2 % i == 0:
##            common_divisor == i
##            common_divisor.append(i)
##            print(common_divisor)
####-----------------Assignment no 12------------------
##i=2
##a=True
##while i<n:
##    if n%i==0:
##        a=False
##        break
##    i+=1
##if a==False:
##    print("not prime ")
##else:
##    print("prime")
    
####Write a python program that keeps taking numbers
####from the user until presses enter-key without typing a number;
####in such case, your program should print
####sum of positive number , count of the negative number, zeros are to be ignored.
####The program should print count of all input values as well
######------------------Code of object 2-----------------------------------------------
##count_negative=0
##count_all=0
##sum_positive=0
##while True :
##    s=input("give me any  integer number(press enter for final result )")
##    if s=='' :
##        break
##    n=int(s)
##    if n!=0:
##        count_all+=1
##    if n>0:
##        sum_positive+=n 
##    if n<0:
##        count_negative+=1
##print("sum of all positive number",sum_positive)
##print("count of all negative number ",count_negative)
##print("Count of all input number",count_all)
#### --------------------Object 1---------------------------------------------------
##Consider the following scenario Write a python program that keeps taking input positive
##numbers from the user until a negative number is entered
##When a negative number is encountered your program should print
##sum and count of the positive numbers entered by the user.
#### -------------------- code of Object 1---------------------------------------------------

##sum = 0
##count = 0
##while True:
##    a=int(input("Give me a number"))
##    if a >= 0:
##        sum += a
##        count += 1
##    else:
##        print(sum)
##        print(count)
##        break
##
## --------------------Object 2---------------------------------------------------
##Write a python program that keeps taking numbers
##from the user until presses enter-key without typing a number;
##in such case, your program should print
##sum of positive number , count of the negative number, zeros are to be ignored.
##The program should print count of all input values as well
####------------------Code of object 2-----------------------------------------------
##count_negative=0
##count_all=0
##sum_positive=0
##count_zero=0
##while True :
##    s=input("give me any  integer number(press enter for final result )")
##    if s=='' :
##        break
##    n=int(s)
##    if n!=0:
##        count_all+=1
##    if n>0:
##        sum_positive+=n 
##    if n<0:
##        count_negative+=1
##print("sum of all positive number",sum_positive)
##print("count of all negative number ",count_negative)
##print("Count of all input number",count_all)
##--------------------------------------------------------------------------------------
##count_negative=0
##count_all=0
##sum_positive=0
##count_zero=0
##while True :
##    s=input("give me any  integer number(press enter for final result )")
##    if s=='' :
##        break
##    n=int(s)
##    if n!=0:
##        count_all+=1
##    if n>0:
##        sum_positive+=n 
##    if n<0:
##        count_negative+=1
##    if n==0:
##        count_zero+=1
##print("sum of all positive number",sum_positive)
##print("count of all negative number ",count_negative)
##print("Count of all zero number",count_zero)
##print("Count of all input number",count_all)
##        

