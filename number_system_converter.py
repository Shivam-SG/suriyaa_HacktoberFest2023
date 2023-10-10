def decimal_to_binary(decimal_num):
    return bin(decimal_num).replace("0b", "")

def decimal_to_hexadecimal(decimal_num):
    return hex(decimal_num).replace("0x", "")

def binary_to_decimal(binary_num):
    return int(binary_num, 2)

def binary_to_hexadecimal(binary_num):
    decimal_num = binary_to_decimal(binary_num)
    return decimal_to_hexadecimal(decimal_num)

def hexadecimal_to_decimal(hexadecimal_num):
    return int(hexadecimal_num, 16)

def hexadecimal_to_binary(hexadecimal_num):
    decimal_num = hexadecimal_to_decimal(hexadecimal_num)
    return decimal_to_binary(decimal_num)

def main():
    print("Number System Converter")

    while True:
        print("\nOptions:")
        print("1. Decimal to Binary")
        print("2. Decimal to Hexadecimal")
        print("3. Binary to Decimal")
        print("4. Binary to Hexadecimal")
        print("5. Hexadecimal to Decimal")
        print("6. Hexadecimal to Binary")
        print("7. Quit")

        choice = input("Enter your choice (1/2/3/4/5/6/7): ")

        if choice == "1":
            decimal_num = int(input("Enter a decimal number: "))
            print(f"Binary: {decimal_to_binary(decimal_num)}")
        elif choice == "2":
            decimal_num = int(input("Enter a decimal number: "))
            print(f"Hexadecimal: {decimal_to_hexadecimal(decimal_num)}")
        elif choice == "3":
            binary_num = input("Enter a binary number: ")
            print(f"Decimal: {binary_to_decimal(binary_num)}")
        elif choice == "4":
            binary_num = input("Enter a binary number: ")
            print(f"Hexadecimal: {binary_to_hexadecimal(binary_num)}")
        elif choice == "5":
            hexadecimal_num = input("Enter a hexadecimal number: ")
            print(f"Decimal: {hexadecimal_to_decimal(hexadecimal_num)}")
        elif choice == "6":
            hexadecimal_num = input("Enter a hexadecimal number: ")
            print(f"Binary: {hexadecimal_to_binary(hexadecimal_num)}")
        elif choice == "7":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please select a valid option.")

if __name__ == "__main__":
    main()
