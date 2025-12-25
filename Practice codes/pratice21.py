# Example-1 this for counting the number of vowels in the string
"""
s=input("Enter the string:")
s5=s.lower()
a=s5.count("a")
b=s5.count("e")
c=s5.count("i")
d=s5.count("o")
e=s5.count("u")
print(f"Number of a:{a+b+c+d+e}")
"""
# Example-2 it is find the subject total marks and average and the grade

"""
x1,y1=input("Enter the subject and the marks:").split(",")
x2,y2=input("Enter the subject and the marks:").split(",")
x3,y3=input("Enter the subject and the marks:").split(",")
x1,y1=str(x1),int(y1)
x2,y2=str(x2),int(y2)
x3,y3=str(x3),int(y3)

total_mark=y1+y2+y3

average=total_mark/3

if total_mark>=300:
    print("Grade A")
elif total_mark>=200:
    print("Grade B")
else:
    print("Grade C")
print(f"{total_mark+average}")
"""
# Example-3 This is about the palindrome\
"""
string="radar"
a=(string[::-1])
print(a)
"""
#in another method
"""
s=input("Enter the string:")
reverse=(s[::-1])
if s== reverse:
    print("The string is palindrome")
else:
    print("It is not a palindrome")
"""
# Example-4 this is to find the largest number among three numbers
"""
a=int(input("Enter the first number:"))
b=int(input("Enter the second number:"))
c=int(input("Enter the third number:"))
if a>=b and a>=c:
    print(a)
elif b>=a and b>c:
    print(b)
elif c>a and c>b:
    print(c)
else:
    print("No greater number")
"""
# Example-5 this is about to find the leap year
"""
a=int(input("Enter the year:"))
if a%100==0 and a%400:
    print("It is a leap year")
else:
    print("It is not a leap year")
"""
# Example another format
"""
a=int(input("Enter the year:"))
if a%100==0 and a%400==0:
    leap=True
elif a%4==0:
    print("Leap year")
else:
    print("IT is not a leap year")
"""
# Example-6
a=int(input("Enter the temperature:"))
k=a+273
c=k-273
f=(c*9/5)+32
print(f"Temperature of fahrenhit:",{f})
print(f"Temperature of kelvin:",{k})
print(f"Temperature in celeius:",{c})


    
