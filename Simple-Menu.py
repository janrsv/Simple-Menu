#!/usr/bin/env python3

def main_menu():
    while True:
        print("\nMain Menu")
        print("1. Option 1")
        print("2. Option 2")
        print("3. Option 3")
        print("4. Option 4")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            handle_choice_1()
        elif choice == '2':
            handle_choice_2()
        elif choice == '3':
            handle_choice_3()
        elif choice == '4':
            handle_choice_4()
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

def handle_choice_1():
    print("You chose option 1.")

def handle_choice_2():
    print("You chose option 2.")

def handle_choice_3():
    print("You chose option 3.")

def handle_choice_4():
    print("You chose option 4.")

if __name__ == "__main__":
    main_menu()
