## 🔹 What is a Tuple in Python?

A **tuple** is a collection of items, just like a list, but:

👉 **Tuple is immutable** (cannot be changed after creation)

---

## 🔹 Syntax

```python
my_tuple = (10, 20, 30)
```

---

## 🔹 Key Features

* Ordered ✅
* Immutable ❌ (cannot add/remove/update)
* Allows duplicates ✅
* Faster than lists ⚡

---

## 🔹 Different Types of Tuple

```python
t1 = (1, 2, 3)
t2 = ("a", "b", "c")
t3 = (10, "hello", 3.5)
```

---

## 🔹 Accessing Elements

```python
t = (10, 20, 30, 40)

print(t[0])   # 10
print(t[-1])  # 40
```

---

## 🔹 Tuple Cannot Be Changed ❗

```python
t = (10, 20, 30)
t[0] = 100   # ❌ Error
```

---

## 🔹 Looping in Tuple

```python
for i in t:
    print(i)
```

---

## 🔹 Tuple Functions

```python
t = (10, 20, 30, 10)

len(t)        # length
t.count(10)   # count occurrences
t.index(20)   # find index
```

---

## 🔹 Tuple Packing & Unpacking

### Packing

```python
t = 1, 2, 3   # automatically tuple
```

### Unpacking

```python
a, b, c = t
print(a)  # 1
```

---

## 🔹 Single Element Tuple ⚠️

```python
t = (5,)   # correct
```

👉 Without comma, it is not a tuple

---

## 🔹 Tuple vs List

| Feature | List   | Tuple  |
| ------- | ------ | ------ |
| Mutable | Yes    | No     |
| Syntax  | `[ ]`  | `( )`  |
| Speed   | Slower | Faster |

---

## 🔹 When to Use Tuple?

* When data should **not change**
* Example: coordinates, fixed values

```python
point = (10, 20)
```

---

## 🔹 Simple Example

```python
student = ("Prashanti", 20, "IT")

print(student[0])  # Name
```

---

If you want next:
👉 **Dictionary (very important in Python & DSA)**
👉 Practice questions on tuple

Just tell me 👍
