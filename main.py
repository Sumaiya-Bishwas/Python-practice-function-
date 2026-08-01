# ==============================
# Python Functions Example
# ==============================

# Function to display a welcome message
def welcome(name):
    print(f"\nHello, {name}! Welcome to the Function Demo.\n")


# Function to calculate factorial using recursion
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


# Function to check if a number is prime
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True


# Function to calculate average
def average(numbers):
    return sum(numbers) / len(numbers)


# Main function
def main():
    name = input("Enter your name: ")
    welcome(name)

    number = int(input("Enter a number: "))

    print(f"\nFactorial of {number} = {factorial(number)}")

    if is_prime(number):
        print(f"{number} is a Prime Number.")
    else:
        print(f"{number} is NOT a Prime Number.")

    values = list(map(int, input("\nEnter numbers separated by spaces: ").split()))

    print(f"Average = {average(values):.2f}")


# Program starts here
if __name__ == "__main__":
    main()