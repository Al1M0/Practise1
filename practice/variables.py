#Exercises

# ex 1
x = 5 # basic int type automatic variable declaration

# ex 2

# my-var = 7 <-- incorrect declaration
myTemporalVar = 7 # < -- Camel case
MyTemporalVar = 7 # < -- Pascal case
my_temporal_var = 7 # < -- Snake case

# ex 3: One value for multiple variables
a = b = c = 7
print(a, b, c, sep = " ")

# Declaring multiple variables in one row
a, b, c = 7, 9, 18 # <-- a corresponds to the first value 7, b to the second 9 and so on
print(a, b, c, sep = " ")


# ex 4
a = "Hello"
b = "Jordan"
print(a + b) # < -- without spaces they will combine and slip. To fix we either put space to one of them, or use sep parameter

print(a, b, sep = " ")
print(a, b.replace("Jordan", " Jordan"))

# ex 5: Global and local variables

x = "Taylor"

def praise_alex():
    x = "Alex" # < -- now its local
    print(x, " is great!")
praise_alex()
print(x, " is great!") # expected Taylor is great, because x = Alex is inside a function

x = "Casey"

def praise_riley():
    global x
    x = "Riley" # Now Casey has been changed to Riley because x is now global
    print(x, "is great")
praise_riley()
print(x, "is great")
