# First implementation on 7/11/2026
# Last worked on 8/11/2026

from pathlib import Path
from datetime import datetime
import json

from assistant.terminal_ui import display_heading, display_subheading, display_message

MODULES_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = MODULES_DIR.parent
MEMORY_DIR = PROJECT_ROOT / "memory"
NOTES_FILE = MEMORY_DIR / "notes.json"


def initialize_storage():
    MEMORY_DIR.mkdir(parents=True, exist_ok=True)
    try:
        with open(NOTES_FILE, "x") as file:
            json.dump([], file)
    except FileExistsError:
        pass 


def show_notes_menu():
    display_heading("NOTES MANAGER")
    print("\n1. Add Note")
    print("\n2. Show Notes")
    print("\n3. Return to main menu")


def run_notes_manager():

    initialize_storage()
    
    while True:
        show_notes_menu()
        try:
            command = int(input("\nEnter the command: "))
            
        except ValueError:
            display_message(["Enter appropriate command", "Available commands {1, 2, 3}"])
            continue

        if command == 1:
            add_note()

        elif command == 2:
            show_notes()

        elif command == 3:
            display_message(["Returning to main menu"])
            break
        else:
            display_message(["Enter appropriate command", "Available commands {1, 2, 3}"])


def add_note():
    note = input("\nEnter the Note: ").strip()

    while not note:
        choice = input("\nYour note is empty. Enter 'D' to Discard or 'T' to Try again: ").lower().strip()
        if choice == 'd':
            display_message(["Note discarded."])
            return
        elif choice == 't':
            note = input("\nEnter the Note: ").strip()

        else:
            display_message(["Invalid choice. Please enter 'D' to Discard or 'T' to Try again."])

    timestamp = datetime.now().strftime("%d %B (%A) %Y, %I:%M:%S %p")
    new_note = {
    "text": note,
    "created_at": timestamp,
    }



    previous_notes = load_notes()

    if previous_notes is None:
        return 
       
    previous_notes.append(new_note)

    if save_notes(previous_notes):
        display_message(["Note saved successfully!"])

    else:
        display_message(["Notes saving failed due to an error. Please check the notes file and try again."])

def save_notes(previous_notes):

    try:
        with open(NOTES_FILE, "w") as file:
            json.dump(previous_notes, file, indent=4)
            return True
    except OSError:
        display_message(["Error: Unable to access the notes file. Check file permissions and availability."])
        return False


def show_notes():
    
    notes = load_notes()

    if notes is None:
        return

    display_subheading(["YOUR NOTES"])
    if notes:
        for index, note in enumerate(notes):
            print(f"\nNote {index + 1}:")
            print(f"Text: {note['text']}")
            print(f"Created At: {note['created_at']}")
    else:
        display_message(["No notes found."])

    
def load_notes():
    required_keys = ("text", "created_at")
    try:
        with open(NOTES_FILE, "r") as file:
            notes = json.load(file)

    except json.JSONDecodeError:
        display_message(["Error reading notes. The notes file may be corrupted."])
        return 

    except OSError:
        display_message(["Error: Unable to access the notes file. Check file permissions and availability."])
        return

    
    if not isinstance(notes, list):
        display_message(["Error: Notes file is corrupted."])
        return 
    if not all(isinstance(note, dict) 
               and key in note 
               and isinstance(note[key], str) 
               for note in notes 
               for key in required_keys):
        display_message(["Error: Notes file is corrupted."])
        return 
        
    return notes