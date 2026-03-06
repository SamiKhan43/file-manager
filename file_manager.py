import os
import shutil
from pathlib import Path

class Colors:
    RESET   = "\033[0m"
    BOLD    = "\033[1m"
    RED     = "\033[91m"
    GREEN   = "\033[92m"
    YELLOW  = "\033[93m"
    BLUE    = "\033[94m"
    CYAN    = "\033[96m"
    WHITE   = "\033[97m"
    PURPLE  = "\033[95m"

class FileManager:

    MENU_ITEMS = [
        (1, "List Files",    "List all files in current directory"),
        (2, "Create File",   "Create a new empty file"),
        (3, "Create Folder", "Create a new folder"),
        (4, "Delete File",   "Permanently delete a file"),
        (5, "Rename File",   "Rename an existing file"),
        (6, "Copy File",     "Copy a file to a new location"),
        (7, "Move File",     "Move a file to a new location"),
        (8, "Exit",          "Exit the File Manager"),
    ]

    def __init__(self):
        self.working_dir = Path('.')

    def _clear(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def _print_header(self):
        c = Colors
        width = 60
        print(f"\n{c.CYAN}{c.BOLD}╔{'═' * width}╗")
        print(f"║{' FILE MANAGER':^{width}}║")
        print(f"╚{'═' * width}╝{c.RESET}")
        cwd = str(Path('.').resolve())
        print(f"  {c.PURPLE} {cwd}{c.RESET}\n")

    def _print_menu(self):
        c = Colors
        width = 60
        print(f"{c.BLUE}┌{'─' * width}┐{c.RESET}")
        for num, name, desc in self.MENU_ITEMS:
            num_str  = f"{c.YELLOW}{c.BOLD} {num}{c.RESET}"
            name_str = f"{c.WHITE}{c.BOLD}{name:<16}{c.RESET}"
            desc_str = f"{c.PURPLE}{desc}{c.RESET}"
            print(f"{c.BLUE}│{c.RESET}  {num_str}  {name_str}  {desc_str}")
        print(f"{c.BLUE}└{'─' * width}┘{c.RESET}\n")

    def _prompt(self, text):
        c = Colors
        return input(f"{c.CYAN}{c.BOLD}  > {text}{c.RESET}").strip()

    def _success(self, msg):
        print(f"\n  {Colors.GREEN}{msg}{Colors.RESET}\n")

    def _error(self, msg):
        print(f"\n  {Colors.RED}{msg}{Colors.RESET}\n")

    def _info(self, msg):
        print(f"\n  {Colors.CYAN}{msg}{Colors.RESET}\n")

    def _divider(self):
        print(f"  {Colors.BLUE}{'─' * 50}{Colors.RESET}")

    def list_files(self):
        files = os.listdir(self.working_dir)
        c = Colors
        print(f"\n{c.CYAN}{c.BOLD}  Contents of: {Path('.').resolve()}{c.RESET}")
        self._divider()
        if not files:
            self._info("Directory is empty.")
            return
        for i, file in enumerate(sorted(files), 1):
            color = c.BLUE if Path(file).is_dir() else c.WHITE
            icon = "[DIR]" if Path(file).is_dir() else "[FILE]"
            print(f"  {c.YELLOW}{i:>3}.{c.RESET}  {icon}  {color}{file}{c.RESET}")
        self._divider()
        print(f"  {c.PURPLE}Total: {len(files)} item(s){c.RESET}\n")

    def create_file(self):
        filename = self._prompt("Enter filename to create: ")
        if not filename:
            self._error("Filename cannot be empty.")
            return
        try:
            with open(filename, 'x'):
                pass
            self._success(f"'{filename}' created at {Path(filename).resolve()}")
        except FileExistsError:
            self._error(f"'{filename}' already exists.")

    def create_folder(self):
        folder_name = self._prompt("Enter folder name to create: ")
        if not folder_name:
            self._error("Folder name cannot be empty.")
            return
        try:
            os.makedirs(folder_name)
            self._success(f"'{folder_name}' created at {Path(folder_name).resolve()}")
        except FileExistsError:
            self._error(f"'{folder_name}' already exists.")

    def delete_file(self):
        self.list_files()
        filename = self._prompt("Enter filename to delete: ")
        confirm = self._prompt(f"Are you sure you want to delete '{filename}'? (y/n): ")
        if confirm.lower() != 'y':
            self._info("Deletion cancelled.")
            return
        try:
            os.remove(filename)
            self._success(f"'{filename}' deleted.")
        except FileNotFoundError:
            self._error(f"'{filename}' not found.")

    def rename_file(self):
        self.list_files()
        old_name = self._prompt("Enter current filename: ")
        new_name = self._prompt("Enter new filename: ")
        try:
            os.rename(old_name, new_name)
            self._success(f"'{old_name}' -> '{new_name}'")
        except FileNotFoundError:
            self._error(f"'{old_name}' not found.")

    def copy_file(self):
        self.list_files()
        source = self._prompt("Enter filename to copy: ")
        destination = self._prompt("Enter destination path: ")
        try:
            shutil.copy(source, destination)
            self._success(f"'{source}' -> '{destination}'")
        except FileNotFoundError:
            self._error(f"'{source}' not found.")

    def move_file(self):
        self.list_files()
        source = self._prompt("Enter filename to move: ")
        destination = self._prompt("Enter destination path: ")
        try:
            shutil.move(source, destination)
            self._success(f"'{source}' -> '{destination}'")
        except FileNotFoundError:
            self._error(f"'{source}' not found.")

    def run(self):
        self._clear()
        self._print_header()
        self._print_menu()

        while True:
            try:
                choice = int(self._prompt("Enter your choice (1-8): "))
            except ValueError:
                self._error("Please enter a number between 1 and 8.")
                continue

            match choice:
                case 1: self.list_files()
                case 2: self.create_file()
                case 3: self.create_folder()
                case 4: self.delete_file()
                case 5: self.rename_file()
                case 6: self.copy_file()
                case 7: self.move_file()
                case 8:
                    print(f"\n  {Colors.CYAN}Goodbye!{Colors.RESET}\n")
                    break
                case _:
                    self._error("Invalid choice. Please try again.")

            input(f"  {Colors.PURPLE}Press Enter to continue...{Colors.RESET}")
            self._clear()
            self._print_header()
            self._print_menu()


if __name__ == "__main__":
    manager = FileManager()
    manager.run()