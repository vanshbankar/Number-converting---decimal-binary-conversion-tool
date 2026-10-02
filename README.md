# Number-converting---decimal-binary-conversion-tool
A simple Python CLI tool to convert Decimal ↔ Binary numbers using mathematical logic and input validation.

Binary ↔ Decimal Converter

A simple Python command-line tool made by Vanshkumar Bankar to convert numbers between Decimal and Binary.

Features

The tool provides two conversion options:

1. Decimal → Binary
2. Binary → Decimal
3. Exit

How It Works

Decimal → Binary

The program repeatedly divides the decimal number by "2" and stores the remainders.

The remainders are then reversed to obtain the correct binary number.

Example:

Decimal: 13

13 ÷ 2 → remainder 1
6  ÷ 2 → remainder 0
3  ÷ 2 → remainder 1
1  ÷ 2 → remainder 1

Binary: 1101

Binary → Decimal

The program reads each binary digit and calculates its decimal value using powers of "2".

Example:

Binary: 1101

1 × 2³ = 8
1 × 2² = 4
0 × 2¹ = 0
1 × 2⁰ = 1

Decimal: 13

Input Validation

For Binary → Decimal conversion, the program checks whether the entered value contains only valid binary digits:

0
1

If another digit is entered, the program displays an error message.

Technologies Used

- Python 3
- "input()"
- "while" loops
- "for" loops
- "if / elif / else"
- "try / except"
- String operations
- Integer arithmetic
- Binary conversion logic

How to Run

Make sure Python 3 is installed.

Run:

python binary_decimal_converter.py

Then select an option:

1 → Decimal to Binary
2 → Binary to Decimal

Example

THIS IS TOOL MADE BY VANSHKUMAR BANKAR
WHICH ARE HELPS TO CONVERT
1. DECIMAL TO BINARY
2. BINARY TO DECIMAL
3. EXIT

Enter Do YOU Want 1 or 2: 1

Enter The Number Do You Want to Binary of These: 13

The Binary Of Your number is = 1101

Project Purpose

This project was created to practice Python fundamentals and understand how number-system conversion works using mathematical logic, rather than relying on Python's built-in conversion functions.

Author

Vanshkumar Bankar

GitHub: "Vanshbankar"
