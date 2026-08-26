def show_menu():
    print("\nMain Menu")
    print("1. Say Hello")
    print("2. Add Numbers")
    print("3. Quit")

def say_hello():
    name = input("Enter your name: ")
    print(f"Hello, {name}!")

def add_numbers():
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum:", a + b)

def main():
    while True:
        show_menu()
        choice = input("Choose an option: ")

        if choice == "1":
            say_hello()
        elif choice == "2":
            add_numbers()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid choice")

if __name__ == "__main__":
    main()
