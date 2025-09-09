import os
from datetime import datetime

NOTES_FILE = "notes.txt"

def add_note():
    note = input("Enter your note: ").strip()
    if note:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        with open(NOTES_FILE, "a", encoding="utf-8") as f:
            f.write(f"[{timestamp}] {note}\n")
        print("Note saved!")
    else:
        print("Empty note not saved.")

def view_notes():
    if not os.path.exists(NOTES_FILE):
        print("No notes found.")
        return
    print("\nYour notes:")
    with open(NOTES_FILE, "r", encoding="utf-8") as f:
        for line in f:
            print(line.strip())
    print()

def main():
    print("Simple Note-Taking App")
    print("----------------------")
    while True:
        print("\nOptions:")
        print("1. Add a note")
        print("2. View notes")
        print("3. Quit")
        choice = input("Choose an option (1-3): ").strip()
        if choice == "1":
            add_note()
        elif choice == "2":
            view_notes()
        elif choice == "3":
            print("Goodbye!")
            break
        else:
            print("Invalid option, please try again.")

if __name__ == "__main__":
    main()
