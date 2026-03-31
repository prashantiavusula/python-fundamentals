List in Python
A list in Python is a collection (data structure) used to store multiple values in a single variable.

Key Features
Ordered (items have a fixed position)
Mutable (you can change values)
Allows duplicates
Can store different data types

syntax
my_list = [item1, item2, item3]

Example
numbers = [1, 2, 3, 4]
names = ["ram", "sita", "john"]
mixed = [1, "hello", 3.5]

📌 Common Operations
1. Add elements
numbers.append(5)        # adds at end
numbers.insert(1, 10)    # adds at index 1

2. Remove elements
numbers.remove(2)   # removes value
numbers.pop()       # removes last
numbers.pop(1)      # removes index 1

3. Update element
numbers[0] = 100

4.Length
len(numbers)

5. Loop through listfor i in numbers:
    print(i)

6.Slicing
nums = [1, 2, 3, 4, 5]
print(nums[1:4])   # [2, 3, 4]

Real-life Example

A list can store:

Student marks
Names
Items in shopping cart



