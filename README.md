# 🧰 Moduler_&_Packager  - Multi-Utility Toolkit

A Python-based menu-driven console application developed to demonstrate custom module creation, package structure, file handling, and Python standard library utilities.

---

## 👩‍💻 Author

**Drashti Vadukul**

College Student | Learning Python, Web Development & Software Engineering

---

## 📌 Project Overview

The **Multi-Utility Toolkit** is a modular Python application that combines multiple practical utilities into a single menu-driven console interface.

It allows users to perform various operations, including date and time calculations, mathematical computations, random data generation, UUID generation, file management, and dynamic module exploration.

The primary purpose of this project is to strengthen practical knowledge of Python programming, custom module creation, package organization, file handling, exception handling, and built-in standard libraries.

---

## 🎯 Project Objectives

* Understand custom module creation and Python package organization.
* Develop an interactive menu-driven console application.
* Perform file operations such as creating, reading, writing, and appending.
* Work with date and time calculations and formatting.
* Implement mathematical formulas and geometric calculations.
* Generate random numbers, lists, passwords, and OTPs.
* Generate unique identifiers using UUID version 4.
* Explore Python modules dynamically using `importlib` and `dir()`.
* Practice control flow, user input, and exception handling.

---

## ✨ Features

### 1. ⏰ Date and Time Operations

Uses Python's `datetime` and `time` modules.

* Display the current date and time.
* Calculate the difference between two dates.
* Format dates using `strftime()`.
* Display month and day names.
* Run a stopwatch to measure elapsed time.
* Run a countdown timer in the terminal.

### 2. 📐 Mathematical Operations

Uses Python's `math` module to perform mathematical calculations.

* **Factorial:** Calculate the factorial of a number.

* **Compound Interest:** Calculate compound growth using the formula:

  $$
  A = P\left(1+\frac{r}{100}\right)^n
  $$

* **Trigonometry:** Calculate sine, cosine, and tangent using angles in degrees.

* **Geometric Areas:** Calculate the areas of different shapes.

| Shape     | Formula           |
| --------- | ----------------- |
| Circle    | π × radius²       |
| Square    | side²             |
| Rectangle | length × width    |
| Triangle  | ½ × base × height |

### 3. 🎲 Random Data Generation

Uses Python's `random` and `string` modules.

* Generate a random integer between 1 and 100.
* Generate a list of random numbers using a custom size and range.
* Generate passwords using letters, digits, and special characters.
* Generate a six-digit numeric OTP.

### 4. 🔑 Unique Identifier Generation

Uses Python's `uuid` module.

* Generate UUID version 4 identifiers.
* Create unique-looking identifiers for testing and demonstration purposes.

### 5. 📁 File Operations

Provides basic text file management using Python's built-in file handling.

* **Create File:** Create an empty text file.
* **Write File:** Write new content or overwrite existing content.
* **Read File:** Read and display the file's contents.
* **Append File:** Add new content without overwriting existing data.

| File Mode | Purpose                    |
| --------- | -------------------------- |
| `w`       | Write or overwrite content |
| `r`       | Read existing content      |
| `a`       | Append content             |

### 6. 🔍 Dynamic Module Exploration

Uses Python's `importlib` and `dir()` functions.

* Accept a module name from the user.
* Import valid modules dynamically.
* Display available attributes, functions, and other names.
* Handle missing modules using exception handling.

**Examples:** `math`, `os`, `sys`, and `datetime`.

> Note: The attributes returned by `dir()` depend on the selected module.

---

## 🏗️ Project Structure

```text
Project_7/
│
├── Module/
│   ├── __pycache__/
│   ├── __init__.py
│   ├── File_Operations.py
│   └── Operations.py
│
├── Main.py
├── Output.png
└── README.md
```

### File Description

| File / Folder               | Description                                                                                  |
| --------------------------- | -------------------------------------------------------------------------------------------- |
| `Main.py`                   | Entry point of the application; displays the main menu and handles user choices.             |
| `Module/`                   | Contains the custom Python package and utility modules.                                      |
| `Module/__init__.py`        | Initializes the package.                                                                     |
| `Module/Operations.py`      | Implements date and time, mathematical, random data, UUID, and module exploration utilities. |
| `Module/File_Operations.py` | Implements text file creation, reading, writing, and appending.                              |
| `Output.png`                | Screenshot of the program's execution.                                                       |
| `README.md`                 | Project documentation.                                                                       |

---

## 🔄 Program Flow

```text
          ┌──────────────────────┐
          │      Start Main      │
          └──────────┬───────────┘
                     │
                     ▼
          ┌──────────────────────┐
          │  Display Main Menu   │
          └──────────┬───────────┘
                     │
                     ▼
          ┌──────────────────────┐
          │   Get User Choice    │
          └──────────┬───────────┘
                     │
          ┌──────────┴───────────┐
          │                      │
          ▼                      ▼
  ┌──────────────────┐   ┌──────────────────┐
  │ Choices 1 to 6   │   │    Choice 7      │
  └────────┬─────────┘   └────────┬─────────┘
           │                      │
           ▼                      ▼
  ┌──────────────────┐   ┌──────────────────┐
  │ Open Selected    │   │   Exit Program   │
  │ Utility / Menu   │   └────────┬─────────┘
  └────────┬─────────┘            │
           │                      ▼
           ▼                     Stop
  ┌──────────────────┐
  │ Perform Selected │
  │    Operation     │
  └────────┬─────────┘
           │
           ▼
  ┌──────────────────┐
  │ Return to Main   │
  │       Menu       │
  └──────────────────┘
```

---

## 🖥️ Application Output

The following screenshot demonstrates the application's execution.

![Multi-Utility Toolkit Output](Output.png)

---


## ⚙️ Technologies Used

* **Programming Language:** Python
* **Development Environment:** Visual Studio Code
* **Python Libraries:** `datetime`, `time`, `math`, `random`, `string`, `uuid`, `importlib`
* **Interface:** Command-Line Interface (CLI)
* **Version Control:** Git and GitHub

---
---

## 🚀 Learning Outcomes

Through this project, I practiced:

* Developing a modular Python application.
* Organizing code into reusable modules.
* Using Python's standard library for practical tasks.
* Managing text files through file input/output operations.
* Implementing nested menus and interactive program flow.
* Exploring modules dynamically and handling common errors.
* Improving code organization and problem-solving skills.

---

## 📌 Conclusion

The **Multi-Utility Toolkit** brings together several useful Python utilities in one modular console application. It demonstrates practical implementation of Python modules, package organization, mathematical operations, random data generation, UUID creation, file handling, and dynamic module exploration.

This project represents my practical learning journey in Python programming and software development.
