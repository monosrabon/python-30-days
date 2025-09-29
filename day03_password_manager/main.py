from generator import generate_password
from checker import check_strength

def main():
    while True:
        print("\n==== PASSWORD MANAGER ====")
        print("1. Generate Password")
        print("2. Check Password Strength")
        print("3. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            try:
                length = int(input("Enter password length: "))
                use_upper = input("Include uppercase? (y/n): ").lower() == "y"
                use_lower = input("Include lowercase? (y/n): ").lower() == "y"
                use_digits = input("Include digits? (y/n): ").lower() == "y"
                use_symbols = input("Include symbols? (y/n): ").lower() == "y"

                password = generate_password(length, use_upper, use_lower, use_digits, use_symbols)
                print(f"\n🔑 Generated Password: {password}\n")

            except ValueError:
                print("⚠️ Please enter a valid number for length.")

        elif choice == "2":
            pwd = input("Enter password to check: ").strip()
            strength = check_strength(pwd)
            print(f"\n🔍 Password Strength: {strength}\n")

        elif choice == "3":
            print("👋 Exiting Password Manager. Goodbye!")
            break

        else:
            print("⚠️ Invalid choice. Try again!")

if __name__ == "__main__":
    main()
