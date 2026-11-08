# Reusable terminal UI formatting functions for the assistant.

import shutil


def display_heading(heading):
    width = shutil.get_terminal_size().columns
    print()
    print("=" * width)
    print(heading.center(width))
    print("=" * width)
    print()


def display_subheading(subheading):
    width = shutil.get_terminal_size().columns
    print()
    print("-" * width)
    for i in subheading:
        print(i.center(width))
    print("-" * width)
    print()

def display_message(message):
    width = shutil.get_terminal_size().columns
    print()
    print("-" * width)
    for i in message:
        print(i)
    print("-" * width)
    print()