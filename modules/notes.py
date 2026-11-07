# First implementation on 7/11/2026
# Last worked on 11-07-2026

import shutil
width = shutil.get_terminal_size().columns

def show_notes_menu():
    print()
    print("=" * width)
    print("Notes Manager".center(width))
    print("=" * width)
    print("\n1. Add Note")
    print("\n2. Show notes functionality coming soon!")
    print("\n3. Return to main menu")


def run_notes_manager():
    show_notes_menu()
    while True:
        try:
            command = int(input("\nEnter the command: "))
            
        except ValueError:
            print("-" * width)
            print("Enter appropriate command")
            print("\nAvailable commands {1, 2, 3}")
            print("-" * width)
            continue

        if command == 1:
            note = add_note()
            show_notes_menu()

        elif command == 3:
            print("\nReturning to main menu")
            break
        else:
            print("-" * width)
            print("Enter appropriate command")
            print("\nAvailable commands {1, 2, 3}")
            print("-" * width)
            show_notes_menu()

def add_note():
    note = input("\nEnter the Note: ").strip()

    while not note:
        note = input("\nEnter the Note: ").strip()

    print("\nNote received successfully!")
    return note