# 🎵 Musical Instrument Inventory

## 📌 Problem

Musical instruments have different names and belong to different instrument families, such as **woodwind** and **brass**.

The goal of this project is to create a simple Python program that stores information about musical instruments and provides basic functionality for each instrument.

Instead of creating separate variables and functions for every instrument, the program uses **Object-Oriented Programming (OOP)** to create reusable instrument objects.

---

## 💡 Solution

The program defines a `MusicalInstrument` class with:

- `name` — stores the instrument's name
- `instrument_type` — stores its instrument family
- `play()` — displays a message about playing the instrument
- `get_fact()` — returns information about the instrument's family

Two objects are then created:

- **Oboe** → Woodwind
- **Trumpet** → Brass

Each object can use the methods defined in the class.

---

## 🧠 Concepts Practiced

- Classes
- Objects
- Constructors (`__init__`)
- Instance attributes
- Instance methods
- `self`
- f-strings
- Object-Oriented Programming

---

## ▶️ Example Output

```text
The Oboe is fun to play!
The Oboe is part of the woodwind family of instruments.
The Trumpet is fun to play!
The Trumpet is part of the brass family of instruments.
