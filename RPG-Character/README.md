# RPG Character

## Description

A beginner-friendly Python project that creates and validates a character for an RPG adventure. The program validates the character name and stats, then generates a character profile with visual stat bars.

## Concepts Covered

- Functions
- Function Parameters
- Input Validation
- `isinstance()`
- Conditional Statements
- String Methods and Slicing
- String Formatting
- String Multiplication
- Unicode Characters

## Files

- `rpg_character.py` – Main Python program

## Example

```python
create_character('ren', 4, 2, 1)
```

### Sample Output

```text
ren
STR ●●●●○○○○○○
INT ●●○○○○○○○○
CHA ●○○○○○○○○○
```

## Validation Rules

The program checks that:

- The character name is a string.
- The character has a name.
- The name is no longer than 10 characters.
- The name contains no spaces.
- All stats are integers.
- Each stat is between 1 and 4.
- The total of all three stats is exactly 7.

## Learning Outcome

This project helped me practice functions, input validation, conditional logic, string manipulation, and generating formatted output in Python.
