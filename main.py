from story1 import start_story_one
from story2 import start_story_two

def main_menu():
    while True:
        print("\n=== STORY SELECT ===")
        print("1. Murder on the Starline Odyssey")
        print("2. The Lost Colony (Story 2)")
        print("3. Quit\n")
        choice = input("Enter 1, 2, or 3: ")

        if choice == "1":
            start_story_one()
            input("\nPress ENTER to return to menu.")

        elif choice == "2":
            start_story_two()
            input("\nPress ENTER to return to menu.")

        elif choice == "3":
            print("Goodbye, astronaut.")
            break

        else:
            print("Invalid choice, try again.")

if __name__ == "__main__":
    main_menu()
