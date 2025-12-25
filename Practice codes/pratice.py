#Example-1
"""
name=str(input("Enter the name:"))
print("Hello",name,sep=",",end="!")
"""

#Example-2
"""
value=int(input("Enter the value:"))
print("You entered:",value,sep="")
"""
#Example-3
"""
num=float(input("Enter the value of the pi:"))
print("Value of pi:",num,sep="")
"""
#Example-4
"""
x=int(input("Enter the value:"))
y=int(input("Enter the values:"))
z=int(input("Enter the values:"))
sum=x+y+z
print("Sum of Inputs:",sum,sep="")
"""
#Exampl-4
"""
#another method for example-4
a=input()
x,y,z=a.split(" ")
sum=int(x)+int(y)+int(z)
print(sum)
"""



#Example-5
"""
inp=input("Enter the name and the age values:")
name,age=inp.split(",")
print("Name:",name,"Age:",age,sep=" ")
"""
# Example-6
"""
x=int(input("Enter the value:"))
print("Countdown:5 4 3 2 1 ",end="Blast Off!")
"""

#Example-7
"""
x=int(input("Enter the values:"))
y=int(input("Enter the values:"))
print("Addition:",x+y)
print("subtraction:",x-y)
print("multiplication:",x*y)
print("division:",x/y)
"""
 #or
""""
x,y=input("Enter the values of a and b").split(",")
a=int(x)
b=int(y)
print("Addition:",a+b,"subtraction:",a-b,"multiplication:",a*b,"Division:",a/b)
"""

#Example-8
"""
x,y=input("Enter the values of a and b").split(",")
a=int(x)
b=int(y)
print(a>b,a<b,a==b,a!=b,sep=",")
"""
#Example-9
"""
x,y=input("Enter the x and y values:").split(",")
a=str(x)
b=str(y)
print("True and False:",a,"True or False:",a,"not True:",b,sep=",")
"""
#Example-10
"""
a=str(input("Enter the input a:"))
b=str(input("Enter the input b:"))
c=str(input("Enter the input c:"))
d=str(input("Enter the input d:"))
print("You entered:",a)
"""

#OR
"""
a,b,c,d=input("Enter the input of this:").split(",")
e=str(a)
f=str(b)
g=str(c)
h=str(d)
print("You entered:",e)
"""
#Example-11
"""
Name,Age=input("Enter the name and age:").split(",")
print("Name:",Name,"Age:",Age)
"""
#or with the help of F string
"""
x,y=input("Enter the name and the age:").split(",")
print(f"Name:{x},Age:{y} years")
"""

#Example-12
"""
num1=int(input("Enter the value of num1:"))
num2=int(input("Enter the value of num2:"))
print(f"sum:{num1+num2}")
"""
#Example-13
"""
radius=int(input("Enter the radius:"))
area=3.14*radius*radius
print(f"Area of the circle:{area}")
"""

#Example=14 pending

#Example-15: With temporary variable..
"""
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
temp=a
a=b
b=temp
print(f"After swapping of a:{a}")
print(f"After swapping of b:{b}")
""" 

#or 
#input a=10,b=20
#output-a=20,b=10
"""
a=int(input("Enter the value of a:"))
b=int(input("Enter the value of b:"))
b=a+b
a=b-a
b=b-a
print(f"After swapping of a:{a}")
print(f"After swapping of b:{b}")
"""

#Example-16
"""
temp_celsius=int(input("Enter the value of temp:"))
f=temp_celsius*(9/5)+32
k=273+temp_celsius
print("Temperature of Fahrenhit:",f)
print("Temperature in kelvin:",k)
"""

#Example-17
Amount_in_usd=int(input("Enter the value:"))
Exchange=float(input("enter"))
result=Amount_in_usd*Exchange
print(result)














