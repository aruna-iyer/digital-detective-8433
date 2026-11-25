# Mission 5 — Numbers and data

## 1. Task / objective

Convert numbers between decimal, binary, and hexadecimal. Check conversions using Python, create a number converter, and learn how computers represent text.

## 2. Work completed

### Manual number conversions

**Decimal 13 to binary**

Divide by 2 and record each remainder:

- 13 ÷ 2 = 6 remainder 1
- 6 ÷ 2 = 3 remainder 0
- 3 ÷ 2 = 1 remainder 1
- 1 ÷ 2 = 0 remainder 1

Read the remainders from bottom to top: **13 in decimal = 1101 in binary**.

**Decimal 25 to binary**

- 25 ÷ 2 = 12 remainder 1
- 12 ÷ 2 = 6 remainder 0
- 6 ÷ 2 = 3 remainder 0
- 3 ÷ 2 = 1 remainder 1
- 1 ÷ 2 = 0 remainder 1

Read the remainders from bottom to top: **25 in decimal = 11001 in binary**.

**Binary 1010 to decimal**

- 1 × 2³ + 0 × 2² + 1 × 2¹ + 0 × 2⁰
- 8 + 0 + 2 + 0 = **10**

**Binary 1101 to decimal**

- 1 × 2³ + 1 × 2² + 0 × 2¹ + 1 × 2⁰
- 8 + 4 + 0 + 1 = **13**

**Hexadecimal A to decimal**

- A represents 10 in hexadecimal.
- **A in hexadecimal = 10 in decimal**

**Hexadecimal 1F to decimal**

- 1 × 16¹ + F × 16⁰
- F represents 15, so 16 + 15 = **31**

**Binary 1111 to hexadecimal**

- The four binary digits 1111 have the decimal value 15.
- 15 is represented by **F in hexadecimal**.

### Python verification

I used Python’s built-in conversion functions to check the answers:

| Expression | Result |
|---|---|
| `bin(13)` | `0b1101` |
| `bin(25)` | `0b11001` |
| `int("1010", 2)` | `10` |
| `int("1101", 2)` | `13` |
| `hex(13)` | `0xd` |
| `hex(25)` | `0x19` |
| `int("A", 16)` | `10` |
| `int("1F", 16)` | `31` |

The results match my manual calculations. Python adds `0b` to binary results and `0x` to hexadecimal results to show their base.

### Number converter tests

| Input | Binary output | Hexadecimal output |
|---:|---:|---:|
| 13 | 1101 | D |
| 25 | 11001 | 19 |
| 42 | 101010 | 2A |

The program asks for a decimal number and converts it to an integer. The `bin()` function converts the integer to binary, and `hex()` converts it to hexadecimal. The program removes the `0b` or `0x` prefix from the result. The `upper()` function displays hexadecimal letters in uppercase.

### Text encoding

- ASCII code for uppercase `A`: **65**
- ASCII code for lowercase `a`: **97**
- Example of a character outside basic ASCII: **₹**

A computer needs an encoding standard to represent text as numbers that it can store and process. ASCII represents a basic set of characters, while UTF-8 can represent a much wider range of characters.

## 3. Commands / tools used

- `python3` — opened Python to check number conversions.
- `python3 mission-05-numbers-data/number_converter.py` — ran the number converter.
- `bin()` — converted an integer to binary.
- `hex()` — converted an integer to hexadecimal.
- `int()` — converted text representing a number into an integer using a specified base.
- `input()` — asked the user to enter a number.
-  Python character check — checked the number codes for `A` and `a`.
- VS Code — created and edited the Python program and README.

## 4. My understanding

Binary uses base 2, decimal uses base 10, and hexadecimal uses base 16. Python’s built-in functions can convert numbers between these forms. Computers use character encodings to represent text as data.

## 5. Difficulties faced

No major difficulties.

## 6. How I resolved them

Not applicable.

## 7. Evidence / files

- `mission-05-numbers-data/README.md`
- `mission-05-numbers-data/number_converter.py`

## 8. Commit details

- Commit message: `Build number converter and practise data representation`
- Pushed to GitHub