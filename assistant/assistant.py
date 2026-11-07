# First version Day: 05-07-2026
# Last worked on 11-07-2026

from modules import notes
import shutil
width = shutil.get_terminal_size().columns

def show_welcome():
    
    print("=" * width)
    print("PERSONAL AI ASSISTANT".center(width))
    print("=" * width)
    print()

def show_menu(name):
        print(f"\nWhat do you want me to do {name}?")
        print("- Notes")
        print("- Help")
        print("- Exit")
        

def run_assistant():
    show_welcome()

    name = input("\nWhat should I call you ? ")

    while True:
        show_menu(name)
        command = (input("\n > ")).lower()

        
        if command != "exit":
            process_command(command)

        else:
            show_goodbye()
            break

def process_command(command):
    print(f"\nSure, processing your command <{command}>")

    if command == "help":
        show_help()

    elif command == "notes":
        notes.run_notes_manager()
    else:
        print(f"\nUnknown command")

def show_help():
    print("\nAVAILABLE COMMANDS: \n")
    print("- Notes")
    print("- Help")
    print("- Exit")

def show_goodbye():
    print("\nBye")