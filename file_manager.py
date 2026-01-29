import os
import shutil
from pathlib import Path

def list_files():
    files = os.listdir('.')
    print("Files in current directory:")
    print("-" * 30)
    for file in files:
        print("#",file)
    print("-" * 30)
    print(f"Total files: {len(files)}")

def create_file():
    filename = input(("Enter the name of the file to create: ")).strip()
    if not filename:
        print("Filename cannot be empty.")
        return
    try:
        print(f"\n Creating file '{filename}'...")
        with open(filename, 'x') as f:
            pass
        print(f"File '{filename}' created successfully.")
        print(f"Absolute path: {Path(filename).resolve()}")
    except FileExistsError:
        print(f"File '{filename}' already exists.") 


def create_folder():
    folder_name = input("Enter the name of the folder to create: ").strip()
    if not folder_name:
        print("Folder name cannot be empty.")
        return
    try:
        os.makedirs(folder_name)
        print(f"Folder '{folder_name}' created successfully.")
        print(f"Absolute path: {Path(folder_name).resolve()}")
    except FileExistsError:
        print(f"Folder '{folder_name}' already exists.")

def delete_file():
    print("\nCurrent files and folders:")
    list_files()
    filename = input("Enter the name of the file to delete:").strip()
    try:
        os.remove(filename)
        print(f"File '{filename}' deleted successfully.")
    except FileNotFoundError:
        print(f"File '{filename}' not found.")

def rename_file():
    print("\nCurrent files and folders:")
    list_files()
    old_name = input("Enter the current name of the file:").strip()
    new_name = input("Enter the new name of the file:").strip()
    try:
        os.rename(old_name, new_name)
        print(f"File '{old_name}' renamed to '{new_name}' successfully.")
    except FileNotFoundError:
        print(f"File '{old_name}' not found.")

def copy_file():
    print("\nCurrent files and folders:")
    list_files()
    source = input("Enter the name of the file to copy:").strip()
    destination = input("Enter the destination path:").strip()
    try:
        shutil.copy(source, destination)
        print(f"File '{source}' copied to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"File '{source}' not found.")

def move_file():
    print("\nCurrent files and folders:")
    list_files()
    source = input("Enter the name of the file to move:").strip()
    destination = input("Enter the destination path:").strip()
    try:
        shutil.move(source, destination)
        print(f"File '{source}' moved to '{destination}' successfully.")
    except FileNotFoundError:
        print(f"File '{source}' not found.")

def menu():
    print("======Welcome to the File Manager=======")
    print("\n1.list files - List all files in the current directory")
    print("2.create file - Create a new file")
    print("3.create folder - Create a new folder")
    print("4.delete file - Delete a file")
    print("5.rename file - Rename a file")
    print("6.copy file - Copy a file")
    print("7.move file - Move a file")
    print("8.exit - Exit the File Manager application \n")
    print("*"*70)


def main():
    menu()
    while True:
        try:
            choice = int(input("Enter your choice:(1-8): ").strip())
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 8.")
            continue
        else:

            match choice:
                case 1:
                    list_files()
                case 2:
                    create_file()
                case 3:
                    create_folder()
                case 4:
                    delete_file()
                case 5:
                    rename_file()
                case 6:
                    copy_file()
                case 7:
                    move_file()
                case 8:
                    print("Exiting File Manager. Goodbye!")
                    break   
                case _:
                    print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()  
