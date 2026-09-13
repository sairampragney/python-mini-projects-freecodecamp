# Build a Budget App

A Python-based budget management program that uses **Object-Oriented Programming (OOP)** to track deposits, withdrawals, transfers, balances, and spending across different budget categories.

The project also generates a **spending chart** that visually compares how much of the total spending belongs to each category.

This project was completed as part of my **FreeCodeCamp Python learning journey**.

---

## 📌 About the Project

The Budget App simulates a simple personal budgeting system.

Users can create different spending categories such as:

- Food
- Clothing
- Auto
- Entertainment
- Utilities

Each category has its own **ledger**, which stores transactions such as deposits and withdrawals.

The program can also transfer money between categories and generate a percentage-based spending chart.

---

## 🎯 Main Features

The program can:

- Create budget categories
- Add money using deposits
- Withdraw money from a category
- Check whether enough funds are available
- Transfer money between categories
- Calculate the current balance
- Display a formatted category ledger
- Calculate spending percentages
- Generate a vertical spending chart

---

# 🏗️ How the Program Works

The project mainly consists of:

```text
Category
   │
   ├── Name
   ├── Ledger
   ├── Deposit
   ├── Withdraw
   ├── Transfer
   ├── Balance
   └── Check Funds

create_spend_chart()
   │
   └── Creates a spending percentage chart
