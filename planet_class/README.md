# 🪐 Planet Class

## 📌 Problem

The goal of this project is to create a Python program that represents planets using **Object-Oriented Programming (OOP)**.

Each planet should have:
- A name
- A planet type
- A star that it orbits

The program should also validate the provided information and provide methods to display planet details and describe its orbit.

---

## 💡 Solution

A `Planet` class is created to represent each planet.

The class contains:

- `name` — stores the planet's name
- `planet_type` — stores the type of planet
- `star` — stores the star the planet orbits
- `orbit()` — returns a message describing the planet's orbit
- `__str__()` — provides a readable representation of the planet

The program also uses **type checking** and **value validation**:

- Raises `TypeError` if the name, planet type, or star is not a string.
- Raises `ValueError` if any of these values are empty.

Three planet objects are created:

- **Earth** → Terrestrial → Sun
- **Jupiter** → Gas Giant → Sun
- **Proxima Centauri b** → Super Earth → Proxima Centauri

---

## 🧠 Concepts Practiced

- Classes
- Objects
- Constructors (`__init__`)
- Instance attributes
- Instance methods
- `self`
- `__str__()`
- Type checking with `isinstance()`
- `TypeError`
- `ValueError`
- f-strings
- Object-Oriented Programming

---

## ▶️ Example Output

```text
Planet: Earth | Type: Terrestrial | Star: Sun
Planet: Jupiter | Type: Gas Giant | Star: Sun
Planet: Proxima Centauri b | Type: Super Earth | Star: Proxima Centauri
Earth is orbiting around Sun...
Jupiter is orbiting around Sun...
Proxima Centauri b is orbiting around Proxima Centauri...
