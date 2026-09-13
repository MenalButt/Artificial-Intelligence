# 1. Hello World

print("Hello, World!")




# 2. Comments

# This is a single line comment
print("This is a comment")



# 3. Input and Output

name = input("Enter your name: ")
print("Hello", name)



# 4. Multiple Statements on a single line

x = 10
y = 20

print("x =", x)
print("y =", y)

print("x =", x); print("y =", y)



# 5. Indentation

number = 10

if number > 5:
    print("Number is greater than 5")
    print("This is inside the if block")

print("This is outside the if block")



# 6. Data Types

integer_value = 25
float_value = 12.5
complex_value = 3 + 4j
boolean_value = True
string_value = "Python"

print("\nData Types:")

print("Integer:", integer_value)
print("Type:", type(integer_value))

print("Float:", float_value)
print("Type:", type(float_value))

print("Complex:", complex_value)
print("Type:", type(complex_value))

print("Boolean:", boolean_value)
print("Type:", type(boolean_value))

print("String:", string_value)
print("Type:", type(string_value))



# 7. Type Casting

num_string = "100"

num_integer = int(num_string)
num_float = float(num_string)
num_stringagain = str(num_integer)

print("\nType Casting:")

print("String to Integer:", num_integer)
print("String to Float:", num_float)
print("Integer to String:", num_stringagain)





# 8. Boolean

value1 = True
value2 = False

print("\nBoolean:")

print("Value 1:", value1)
print("Value 2:", value2)

print("10 > 5:", 10 > 5)
print("10 < 5:", 10 < 5)


# 9. Strings

string1 = "PYTHON TUTORIAL"
string2 = 'Python Programming'

print("\nStrings:")

print(string1)
print(string2)

message1 = "Python's syntax is easy"
message2 = 'He said "Hello"'

print(message1)
print(message2)



# 10. Special Characters

print("\nSpecial Characters:")

print("Hello\nWorld")
print("Name:\tPython")
print("Backslash: \\")
print("Single Quote: \'")
print("Double Quote: \"")


# 11. String Indexing

text = "PYTHON TUTORIAL"

print("\nString Indexing:")

print("First character:", text[0])
print("Second character:", text[1])
print("Third character:", text[2])

print("Last character:", text[-1])
print("Second last character:", text[-2])



# 12. String Slicing

print("\nString Slicing:")

print(text[0:6])
print(text[7:15])
print(text[:6])
print(text[7:])
print(text[-8:])




# 13. Lists

color_list = ["RED", "Blue", "Green", "Black"]

print("\nList:")

print("Complete List:", color_list)

print("First Item:", color_list[0])
print("Second Item:", color_list[1])
print("Last Item:", color_list[-1])




# 14. Empty List

empty_list = []

print("\nEmpty List:")
print(empty_list)




# 15. Mixed List

mixed_list = ["Python", 100, 25.5, True]

print("\nMixed List:")
print(mixed_list)




# 16. List Slicing

print("\nList Slicing:")

print("First Two Items:", color_list[0:2])
print("Middle Items:", color_list[1:3])
print("Last Two Items:", color_list[-2:])
print("All Except Last:", color_list[:-1])




# 17. Comparison Operators

a = 20
b = 10

print("\nComparison Operators:")

print("a == b:", a == b)
print("a != b:", a != b)
print("a < b:", a < b)
print("a <= b:", a <= b)
print("a > b:", a > b)
print("a >= b:", a >= b)




# 18. Conditional Statements

if b > a:
    print("b is greater than a")
else:
    print("b is not greater than a")











