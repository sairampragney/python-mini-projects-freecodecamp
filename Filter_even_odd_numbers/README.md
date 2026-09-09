# Filter Even and Odd Numbers

A simple Python program that uses the built-in `filter()` function and `lambda` expressions to separate a list of numbers into **even** and **odd** numbers.

---

## 📌 About

This project is part of my **Python learning journey**.

The program starts with a list of numbers stored as strings and processes each number to determine whether it is even or odd.

It creates two separate lists:

- **Even numbers:** Numbers divisible by 2
- **Odd numbers:** Numbers that leave a remainder of 1 when divided by 2

This program demonstrates the use of:

- Lists
- `filter()`
- Lambda functions
- `int()` type conversion
- Modulo operator `%`
- Boolean conditions
- `list()` conversion

---

## 💻 Complete Code

```python
numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

even_numbers = list(filter(lambda x: int(x) % 2 == 0, numbers))
print(even_numbers)

odd_numbers = list(filter(lambda x: int(x) % 2 == 1, numbers))
print(odd_numbers)
