
a=5 #variable a is assigned the value 5
b=2 # variable b is assigned the value 2
sum = a + b
diff = a-b
multi = a*b
division = a/b
mod = a%b
print("The sum of " + str(a) + " and " + str(b) + " is " + str(sum))
print("The difference of " + str(a) + " and " + str(b) + " is " + str(diff))
print("The product of " + str(a) + " and " + str(b) + " is " + str(multi))
print("The quotient of " + str(a) + " and " + str(b) + " is " + str(division))
print("The remainder of " + str(a) + " and " + str(b) + " is " + str(mod))

a=10
b=2

print(a+b)
print(a-b)
print(a*b)
print(a/b)
print(a%b)
print(a**b) #exponentiation


#relational operators
a=10
b=20
print(a==b) #equal to
print(a!=b) #not equal to
print(a>b) #greater than
print(a<b) #less than
print(a>=b) #greater than or equal to
print(a<=b) #less than or equal to

#assignment operators
num =10
num *=5
print ("The number is:", str(num))

#logical operators
a=1
b=2
print (not False)
print (a>b)

#logical operators
val1 = True
val2 = False
print("AND Operator:" , (val1 and val2)) #logical AND
print("OR Operator:" , (val1 or val2)) #logical OR
print("NOT Operator:", (not val1)) #logical NOT

#type conversion
x = 5
y = 2.25

sum = x + y
print("Sum of x and y is:", sum)

#type casting

x=int("5")
y=2.25
print(type(x))
print(type(y))

#inputs in python
name = input("Enter your name: ")
age = input("Enter your age: ")
marks = float(input("Enter your marks: "))
print("Hello", name, "your age is", age, "and your marks are", marks)
print(type(marks))