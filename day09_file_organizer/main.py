# Entry point
from organizer import organize_files

def main():
    print("=== File Organizer ===")
    folder = input("Enter the path of the folder to organize: ").strip()
    organize_files(folder)
    print("\n🎉 Files organized successfully!")

if __name__ == "__main__":
    main()