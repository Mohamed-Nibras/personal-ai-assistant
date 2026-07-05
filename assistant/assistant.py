import shutil
width = shutil.get_terminal_size().columns
    
def show_welcome():
    
    print("=" * width)
    print("PERSONAL AI ASSISTANT".center(width))
    print("=" * width)
    print()

def show_menu(name):
        print(f"\nWhat do you want me to do {name}?")
        print("1. Sample 1")
        print("2. Sample 2")
        print("3. Exit")

def run_assistant():
    show_welcome()

    name = input("\nWhat should I call you ? ")

    while True:
        show_menu(name)
        while True:
            try:
                command = int(input(" > "))
                break

            except ValueError:
                print("Enter the correct option")

        
        if command != 3:
            process_command(command)

        else:
            show_goodbye()
            break

def process_command(command):
    print(f"\nSure, processing your command <{command}>")

    if command == 1:
        print(f"\nYour command completed <Sample 1>")
    
    elif command == 2:
        print(f"\nYour command completed <Sample 2>")

def show_goodbye():
    print("\nBye")

