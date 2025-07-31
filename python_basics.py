# ---------------------------
# Python Basics
# ---------------------------

# 1. Variables and Data Types
name = "John"
age = 20
height = 151.5
is_coder = True

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Is a coder?", is_coder)

# 2. Conditional Statements
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 3. Loops
print("Counting from 1 to 5:")
for i in range(1, 6):
    print(i)

# While loop
count = 0
while count < 3:
    print("Count is:", count)
    count += 1

# 4. Functions
def greet(name):
    return "Hello, " + name + "!"

print(greet("Vara"))

# 5. Lists
fruits = ["apple", "banana", "cherry"]
print("Fruits list:", fruits)
fruits.append("orange")
print("After adding orange:", fruits)

# 6. Dictionaries
person = {
    "name": "Vara",
    "age": 28,
    "city": "Auckland"
}
print("Person Info:", person)
print("Name:", person["name"])

# 7. Classes and Objects
class Dog:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return self.name + " says woof!"

my_dog = Dog("Buddy")
print(my_dog.speak())

# 8. Exception Handling
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# 9. File Handling
with open("example.txt", "w") as file:
    file.write("This is a test file.")

with open("example.txt", "r") as file:
    content = file.read()
    print("File Content:", content)

# 10. Importing Modules
import math
print("Square root of 16 is:", math.sqrt(16))
