class Contact:
    def __init__(self, name, phone_number, email):
        self.name = name
        self.phone_number = phone_number
        self.email = email

class AddressBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact '{contact.name}' added successfully.")

    def search_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                found_contacts.append(contact)
        if found_contacts:
            print(f"Found {len(found_contacts)} contact(s):")
            for contact in found_contacts:
                print_contact(contact)
        else:
            print("No matching contacts found.")

    def edit_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                found_contacts.append(contact)
        if found_contacts:
            print(f"Found {len(found_contacts)} contact(s).")
            print("Select a contact to edit:")
            for index, contact in enumerate(found_contacts):
                print(f"{index + 1}. {contact.name}")
            choice = int(input("Enter the contact number: ")) - 1
            if 0 <= choice < len(found_contacts):
                contact = found_contacts[choice]
                print("Enter new details for the contact:")
                contact.name = input("Name: ")
                contact.phone_number = input("Phone Number: ")
                contact.email = input("Email: ")
                print(f"Contact '{contact.name}' updated successfully.")
            else:
                print("Invalid contact number.")
        else:
            print("No matching contacts found.")

    def delete_contact(self, name):
        found_contacts = []
        for contact in self.contacts:
            if name.lower() in contact.name.lower():
                found_contacts.append(contact)
        if found_contacts:
            print(f"Found {len(found_contacts)} contact(s).")
            print("Select a contact to delete:")
            for index, contact in enumerate(found_contacts):
                print(f"{index + 1}. {contact.name}")
            choice = int(input("Enter the contact number: ")) - 1
            if 0 <= choice < len(found_contacts):
                contact = found_contacts[choice]
                self.contacts.remove(contact)
                print(f"Contact '{contact.name}' deleted successfully.")
            else:
                print("Invalid contact number.")
        else:
            print("No matching contacts found.")

    def display_contacts(self):
        if self.contacts:
            print("Address Book:")
            for contact in self.contacts:
                print_contact(contact)
        else:
            print("Address Book is empty.")

def print_contact(contact):
    print(f"Name: {contact.name}")
    print(f"Phone Number: {contact.phone_number}")
    print(f"Email: {contact.email}")
    print()

def main():
    address_book = AddressBook()

    while True:
        print("Address Book Menu:")
        print("1. Add Contact")
        print("2. Search Contact")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Display Contacts")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            print("Enter contact details:")
            name = input("Name: ")
            phone_number = input("Phone Number: ")
            email = input("Email: ")
            contact = Contact(name, phone_number, email)
            address_book.add_contact(contact)
        elif choice == "2":
            name = input("Enter name to search: ")
            address_book.search_contact(name)
        elif choice == "3":
            name = input("Enter name to edit: ")
            address_book.edit_contact(name)
        elif choice == "4":
            name = input("Enter name to delete: ")
            address_book.delete_contact(name)
        elif choice == "5":
            address_book.display_contacts()
        elif choice == "6":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
