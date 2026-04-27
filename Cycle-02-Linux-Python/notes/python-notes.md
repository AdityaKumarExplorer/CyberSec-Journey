# Python Notes

## Data Types
- int → 10
- float → 3.14
- string → "hello"
- list → [1,2,3]

## Loops

### for loop
for i in range(5):
    print(i)

### while loop
x = 0
while x < 5:
    print(x)
    x += 1

## Functions

def add(a, b):
    return a + b

print(add(2,3))

## File Handling

# Write
f = open("file.txt", "w")
f.write("Hello")
f.close()

# Read
f = open("file.txt", "r")
print(f.read())
f.close()
