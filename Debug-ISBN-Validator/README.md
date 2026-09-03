# Debug an ISBN Validator

## Description

An **ISBN (International Standard Book Number)** is a unique identification number assigned to books and other book-related publications. An ISBN can contain either **10 digits (ISBN-10)** or **13 digits (ISBN-13)**.

The last digit of an ISBN is called the **check digit**. It is calculated using the other digits and is used to verify whether the ISBN is valid.

This project is a debugging exercise based on a FreeCodeCamp Python lab. The original program contains several errors that need to be fixed so that it can correctly validate ISBN-10 and ISBN-13 codes.

## What This Project Does

The program:

- Accepts an ISBN and its length from the user.
- Checks whether the input is correctly comma-separated.
- Validates that the length is `10` or `13`.
- Checks whether the ISBN contains invalid characters.
- Verifies that the ISBN has the correct number of characters.
- Calculates the expected check digit.
- Compares the calculated check digit with the provided check digit.
- Displays whether the ISBN is valid or invalid.
- Handles common errors without crashing.

## Concepts Covered

- Functions
- Function Parameters
- String Manipulation
- String Slicing
- Lists
- `enumerate()`
- Conditional Statements
- `try` and `except`
- `IndexError`
- `ValueError`
- Input Validation
- ISBN Check Digit Calculation
- Debugging

## Error Handling

The program handles several possible input errors:

| Input Problem | Message |
|---|---|
| Missing comma | `Enter comma-separated values.` |
| Non-numeric length | `Length must be a number.` |
| Length other than 10 or 13 | `Length should be 10 or 13.` |
| Incorrect ISBN length | `ISBN-10 code should be 10 digits long.` or `ISBN-13 code should be 13 digits long.` |
| Invalid characters | `Invalid character was found.` |
| Incorrect check digit | `Invalid ISBN Code.` |

## Example

### Valid ISBN-10

```text
Enter ISBN and length: 1530051126,10
Valid ISBN Code.
