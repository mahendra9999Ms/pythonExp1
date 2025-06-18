Python 3.7.9 (tags/v3.7.9:13c94747c7, Aug 17 2020, 18:58:18) [MSC v.1900 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> a=eval(input("enter first value:"))
b=eval(input("enter second value:"))
print("before swaping a,b:",a,b)
a,b=b,a
print("after swaping a,b:",a,b)
print("-----------------------")
print("before swaping a,b:",a,b)
temp=a
a=b
b=temp
print("after swaping a,b:",a,b)
print("-----------------------")
print("before swaping a,b:",a,b)
a=a+b
b=a-b
a=a-b
print("after swaping a,b:",a,b)
print("-----------------------")
print("before swaping a,b:",a,b)
a=a*b
b=a//b
a=a//b
print("after swaping a,b:",a,b)