# ex 1: Determining the type of a variable
x = 7
print(type(x)) # class <'int'>


# ex 2: Which data type is expected?
x = "Moriko"
print(type(x))

# answer: class <'str'>

# ex 3: Set manual data type (if supported)
x = str(7)
y = "Moriko"
print(x, y)

# note: in some cases str cannot be re declared as an integer:
x = "122f"
try:
    y = int(x)
except ValueError:
    print("You cant declare integer as string! Check if the string has any non-digit character")

# ex 4, which type is it?
a = ["apple", "banana", "orange"]
print(type(a)) # class <'list'>

# ex 5, declare type instantly in inputting:
a = int(input("Input a value: "))
print(a, type(a))