decimal_number = int(input("Enter a positive decimal number: "))

binary_number = bin(decimal_number)[2:]
hexadecimal_number = hex(decimal_number)[2:].upper()

print("Binary:", binary_number)
print("Hexadecimal:", hexadecimal_number)