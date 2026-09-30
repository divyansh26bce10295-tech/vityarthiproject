# Interest Calculator

## Project Description

This project is a command-line based Interest Calculator developed using Python and Object-Oriented Programming concepts.

The program allows the user to calculate:

- Simple Interest
- Compound Interest

It demonstrates inheritance, constructors, method overriding, and the `super()` function.

## Features

- Accepts account number from the user.
- Accepts principal amount from the user.
- Calculates Simple Interest.
- Calculates Compound Interest.
- Provides a menu-driven command-line interface.
- Allows the user to exit the program.

## Technologies Used

- Python 3
- Object-Oriented Programming

## Project Structure

```text
interest-calculator/
├── main.py
└── README.md
```

## Requirements

Python 3 must be installed on your system.

No external Python libraries are required.

## How to Run

### Step 1: Check Python Installation

Open a terminal and run:

```bash
python --version
```

On some systems, use:

```bash
python3 --version
```

### Step 2: Open the Project Directory

```bash
cd interest-calculator
```

### Step 3: Run the Program

On Windows:

```bash
python main.py
```

On macOS/Linux:

```bash
python3 main.py
```

## How the Program Works

The program first asks the user to enter:

1. Account Number
2. Principal Amount

It then displays a menu:

```text
Main Menu
Press 1 to check Simple Interest
Press 2 to check Compound Interest
Press 3 to Exit
```

### Simple Interest Formula

```text
SI = (Principal × Rate × Time) / 100
```

### Compound Interest Formula

```text
CI = Principal × ((1 + Rate / 100) ^ Time) - Principal
```

## Object-Oriented Concepts Used

### Inheritance

`Simple_Interest` and `Compound_Interest` inherit from the `Account` class.

### Constructor

The classes use `__init__()` to initialize account and interest-related information.

### `super()`

The `super()` function is used to call the constructor and `display()` method of the parent class.

### Method Overriding

Both `Simple_Interest` and `Compound_Interest` provide their own implementation of the `display()` method.

## Example

```text
Enter Account Number: 101
Enter Principal Amount: 10000

Main Menu
Press 1 to check Simple Interest
Press 2 to check Compound Interest
Press 3 to Exit

Please Enter Your Choice: 1
Rate: 5
Time: 2

The Account Number is 101
The Principal Amount is Rs. 10000.0
The Rate of Interest is 5.0 and Time is 2.0
Simple Interest: 1000.0
```

## Author

YOUR NAME
