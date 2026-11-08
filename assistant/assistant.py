# First version Day: 5/07/2026
# Last worked on 8/11/2026

from modules import notes
from assistant import display_heading, display_subheading, display_message

def show_welcome():
    
    display_heading("PERSONAL AI ASSISTANT")


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
        command = (input("\n > ")).lower().strip()

        
        if command != "exit":
            process_command(command)

        else:
            show_goodbye()
            break

def process_command(command):

    if command == "help":
        display_message([f"Sure, processing your command <{command}>"])
        show_help()

    elif command == "notes":
        display_message([f"Sure, processing your command <{command}>"])
        notes.run_notes_manager()
    else:
        display_message([f"Unknown command"])

def show_help():
    display_subheading(["AVAILABLE COMMANDS:"])
    print("- Notes")
    print("- Help")
    print("- Exit")

def show_goodbye():
    display_message(["Bye"])