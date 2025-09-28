from storage import load_contacts, save_contacts
from contact_manager import add_contact, view_contacts, search_contact, update_contact, delete_contact

def main():
    contacts = load_contacts()

    while True:
        print("==== CONTACT BOOK ====")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("\nEnter your choice: ").strip()

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("\n💾 Contacts saved. Exiting program. Goodbye!\n")
            break
        else:
            print("\n⚠️ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
