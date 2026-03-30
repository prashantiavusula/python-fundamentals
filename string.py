A string is a sequence of characters (text) enclosed in quotes.
a = "Hello"
b = 'World'

🔹 Operations on Strings
1.Concatenation (Joining)
Combine two strings using +
a = "Hello"
b = "World"
print(a + " " + b)   # Hello World

2 Repetition
Repeat a string using*
a = "Hi "
print(a * 3)   # Hi Hi Hi 

3.Indexing (Access characters)
Access characters using position
a = "Python"
print(a[0])   # P
print(a[2])   # t

4.Length of String
a = "Hello"
print(len(a))   # 5

5.Membership Operators
a = "apple"
print('a' in a)        # True
print('z' not in a)    # True

6.Slicing (Get part of string)
a = "Python"
print(a[0:3])   # Pyt
print(a[2:])    # thon
print(a[:4])    # Pyth

7. String Methods (Very Important)
a = "hello world"
print(a.upper())      # HELLO WORLD
print(a.lower())      # hello world
print(a.title())      # Hello World
print(a.capitalize()) # Hello world

8. Replace
a = "hello"
print(a.replace("h", "y"))   # yello

9. Split
a = "apple banana mango"
print(a.split())   # ['apple', 'banana', 'mango']

10. Strip (Remove spaces)
a = "  hello  "
print(a.strip())   # hello

11. Find
a = "python"
print(a.find("t"))   # 2









