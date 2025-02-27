def calculator():
    """Simple calculator for basic arithmetic operations."""
    try:
        x = float(input("Enter 1st number: "))
        op = input("Select the operator (+, -, *, /): ")
        y = float(input("Enter 2nd number: "))

        if op == "+":
            result = x + y
        elif op == "-":
            result = x - y
        elif op == "*":
            result = x * y
        elif op == "/":
            result = x / y if y!=0 else "Error: Cannot divide by zero."
        else:
            result = "Invalid operator! Please select from (+, -, , /)."
        print(f"Result: {result}")

    except ValueError:
        print("Invalid input! Please enter numeric values")

def reverse():
    """Reverses the user-inputted string."""
    wrt = input("Enter a string: ")
    print(f"Reversed string: {wrt[::-1]}")

def welcome():
    """Greets the user with a welcome message."""
    while True:
        name = input("Enter your full name: ").strip()
        if name == "":
            print("You didn't enter your name. Please try again.\n")
        else:
            print(f"Hello {name}! Welcome to the program. Glad to have you here!")
            break

def count_vowels():
    """Counts the number of vowels in a given string."""
    text = input("Enter a string: ")

    vowels = "aeiouAEIOU"
    count = 0

    for char in text:
        if char in vowels:
            count += 1
    print(f"Total number of vowels: {count}")


def age_group():

    """Determines the user's age category"""
    while True:
        try:
            age = int(input("Enter your age: "))

            if age <= 0:
                print("Invalid age! Please enter a positive number.")
            elif age > 100:
                print("You are a senior citizen (100+ years).")
            elif age > 64:
                print("You are a senior citizen.")
            elif age > 19:
                print("You are an adult.")
            else:
                print("You are a minor.")
            break
        except ValueError:
            print("Invalid input! Age must be a number")

#Now I will create a program then user can select what they to do?
def main():
    """Main menu for the program"""
    while True:
        print("\nSelect an option:")
        print("1. Calculator")
        print("2. Reverse a String")
        print("3. Welcome Message")
        print("4. Count Vowels")
        print("5. Determine Age Group")
        print("0. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            calculator()
        elif choice == "2":
            reverse()
        elif choice == "3":
            welcome()
        elif choice == "4":
            count_vowels()
        elif choice == "5":
            age_group()
        elif choice == "0":
            print("Thank you for using the program! Goodbye.")
            break
        else:
            print("Invalid choice! Please try again.")
main()

