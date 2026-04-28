# 🐍 Python Notes

---

## 1. Data Types (with Examples)

Data types define the kind of value a variable can store.

### Integer (int)
Stores whole numbers.

```python
a = 10
print(a)
````

---

### Float (float)

Stores decimal numbers.

```python
b = 3.14
print(b)
```

---

### String (str)

Stores text inside quotes.

```python
name = "Aditya"
print(name)
```

---

### Boolean (bool)

Stores True or False values.

```python
is_valid = True
print(is_valid)
```

---

### List

Stores multiple values (mutable).

```python
numbers = [1, 2, 3, 4]
print(numbers)
print(numbers[0])   # Access first element
```

---

### Tuple

Stores multiple values (immutable).

```python
t = (1, 2, 3)
print(t)
```

---

### Dictionary

Stores key-value pairs.

```python
student = {
    "name": "Aditya",
    "age": 20
}

print(student["name"])
```

---

## 2. Loops (with Examples)

Loops are used to execute a block of code multiple times.

---

### for loop

Used when number of iterations is known.

```python
for i in range(5):
    print(i)
```

Output:
0 1 2 3 4

---

### while loop

Used when execution depends on a condition.

```python
x = 0
while x < 5:
    print(x)
    x += 1
```

---

### Loop Control Statements

#### break → Stops the loop completely

```python
for i in range(5):
    if i == 3:
        break
    print(i)
```

---

#### continue → Skips current iteration

```python
for i in range(5):
    if i == 3:
        continue
    print(i)
```

---

## 3. Functions (with Examples)

Functions are reusable blocks of code.

---

### Basic Function

```python
def greet():
    print("Hello")

greet()
```

---

### Function with Parameters

```python
def add(a, b):
    return a + b

result = add(2, 3)
print(result)
```

---

### Function with Default Parameters

```python
def greet(name="User"):
    print("Hello", name)

greet()
greet("Aditya")
```

---

### Function Returning Multiple Values

```python
def operations(a, b):
    return a + b, a - b

sum_val, diff_val = operations(5, 3)
print(sum_val, diff_val)
```

---

## 4. File Handling (with Examples)

File handling is used to read from and write to files.

---

### File Modes

* `"r"` → Read
* `"w"` → Write (overwrites file)
* `"a"` → Append

---

### Writing to a File

```python
f = open("file.txt", "w")
f.write("Hello World")
f.close()
```

---

### Reading from a File

```python
f = open("file.txt", "r")
data = f.read()
print(data)
f.close()
```

---

### Appending to a File

```python
f = open("file.txt", "a")
f.write("\nNew Line Added")
f.close()
```

---

### Best Practice (with statement)

```python
with open("file.txt", "r") as f:
    data = f.read()
    print(data)
