def display_menu():
    print("Shopping List Manager")
    print("1. Add Item")
    print("2. Remove Item")
    print("3. View List")
    print("4. Exit")

def main():
    shopping_list = []
    while True:
        display_menu()
        choice = input("Enter your choice: ")

        if choice == "1":
            item = input("Enter the item to add: ")
            shopping_list.append(item)
        elif choice == "2":
            item = input("Enter the item to remove: ").lower()
            if item in shopping_list:
                shopping_list.remove(item)
            else:
                "Item not found in the list."
        elif choice == "3":
            print("Shopping List:")
            if shopping_list == []:
                print("The list is empty.")
            else:
                for item in shopping_list:
                    print(item)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
