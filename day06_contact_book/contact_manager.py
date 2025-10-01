def add_contact(contacts):
    name = input("Enter Name: ").strip()
    phone = input("Enter Phone: ").strip()
    email = input("Enter Email: ").strip()
    address = input("Enter Address: ").strip()
    
    contacts[name] = {
        "Phone": phone,
        "Email": email,
        "Address": address
    }
    print(f"\n✅ Contact '{name}' added successfully!\n")

def view_contacts(contacts):
    if not contacts:
        print("\n📭 No contacts found.\n")
        return
    print("\n📒 All Contacts:")
    for name, details in contacts.items():
        print(f"\nName: {name}")
        for key, value in details.items():
            print(f"  {key}: {value}")
    print()

def search_contact(contacts):
    name = input("Enter Name to Search: ").strip()
    if name in contacts:
        print(f"\n🔍 Found Contact: {name}")
        for key, value in contacts[name].items():
            print(f"  {key}: {value}")
    else:
        print("\n❌ Contact not found.\n")

def update_contact(contacts):
    name = input("Enter Name to Update: ").strip()
    if name in contacts:
        print("\nLeave blank if you don't want to change a field.")
        phone = input("Enter New Phone: ").strip()
        email = input("Enter New Email: ").strip()
        address = input("Enter New Address: ").strip()

        if phone:
            contacts[name]["Phone"] = phone
        if email:
            contacts[name]["Email"] = email
        if address:
            contacts[name]["Address"] = address
        
        print(f"\n✏️ Contact '{name}' updated successfully!\n")
    else:
        print("\n❌ Contact not found.\n")

def delete_contact(contacts):
    name = input("Enter Name to Delete: ").strip()
    if name in contacts:
        del contacts[name]
        print(f"\n🗑️ Contact '{name}' deleted successfully!\n")
    else:
        print("\n❌ Contact not found.\n")
