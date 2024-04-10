# main.py

def add_numbers(a, b):
    """Add two numbers together."""
    return a + b

def main():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    result = add_numbers(num1, num2)
    print("The result is:", result)

if __name__ == "__main__":
    main()
print("hii")