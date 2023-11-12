def add_contacts(contacts):
    name = input("Enter contact name: ")
    if name in contacts:
        print("Contact already added. ")
    else:
        number = input("Enter phone number: ")
        contacts[name] = number
        print("Contact Added!")

def view_contacts(contacts):
    if contacts:
        for name, number in contacts.items():
            print(f"Name: {name}, Phone Number: {number}")
    else:
        print("No contacts to view! ")

def edit_contacts(contacts):
    name = input("Enter name of contact to edit: ")
    if name in contacts:
        newNumber = input("Enter the new number: ")
        contacts[name] = newNumber 
        print("Contact updated.")
    else:
        print("Contact not found.")

def delete_contacts(contacts):
    name = input("Enter name of contact to delete: ")
    if name in contacts:
        del contacts[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")
def main():
    contacts = {}
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            add_contacts(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            edit_contacts(contacts)
        elif choice == "4":
            delete_contacts(contacts)
        elif choice == "5":
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please choose a valid option. ")

if __name__ == "__main__":
    main()



