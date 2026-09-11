# Email Simulator

A Python-based email simulation program that models a simple email system using **Object-Oriented Programming (OOP)**.

This project simulates how users can send emails to each other, receive emails in an inbox, view their messages, mark emails as read, and delete emails.

This project was completed as part of the **FreeCodeCamp Python course**:

[Build an Email Simulator](https://www.freecodecamp.org/learn/python-v9/#workshop-email-simulator)

---

## 📌 About the Project

The **Email Simulator** is a console-based Python program that recreates the basic behavior of an email system.

Instead of connecting to a real email server, the program keeps everything inside Python objects.

The simulation contains three main classes:

- `Email`
- `User`
- `Inbox`

These classes work together to create a simple email workflow.

A user can:

1. Send an email to another user.
2. Receive the email in their inbox.
3. View their inbox.
4. Open and read an email.
5. Automatically mark the email as read.
6. Delete an email from the inbox.

---

# 🧠 What This Project Actually Represents

This project is essentially a **small model of how an email application could work**.

There are different objects in the system, and each object has its own data and responsibilities.

For example:

```text
User
 │
 ├── Name
 │
 └── Inbox
      │
      ├── Email
      ├── Email
      └── Email
