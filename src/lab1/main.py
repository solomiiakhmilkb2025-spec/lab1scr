from lib import greet, add_numbers, multiply_numbers, power

def main():
    print(greet("Соломія"))
    print("5 + 3 =", add_numbers(5, 3))
    print("5 * 3 =", multiply_numbers(5, 3))
    print("2 ^ 3 =", power(2, 3))

if __name__ == "__main__":
    main()
    