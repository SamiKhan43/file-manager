# File Manager
A terminal-based file management application built with Python featuring a clean, colored UI for performing common file and folder operations.

## Project Link
* [file manager](https://github.com/SamiKhan43/file-manager)

## Preview
```
╔════════════════════════════════════════════════════════════╗
║                       FILE MANAGER                        ║
╚════════════════════════════════════════════════════════════╝
  /home/user/documents

┌────────────────────────────────────────────────────────────┐
│   1  List Files        List all files in current directory
│   2  Create File       Create a new empty file
│   3  Create Folder     Create a new folder
│   4  Delete File       Permanently delete a file
│   5  Rename File       Rename an existing file
│   6  Copy File         Copy a file to a new location
│   7  Move File         Move a file to a new location
│   8  Exit              Exit the File Manager
└────────────────────────────────────────────────────────────┘

  > Enter your choice (1-8):
```

## Features
- **List Files** - Display all files and folders with `[DIR]` / `[FILE]` labels
- **Create File** - Create a new empty file
- **Create Folder** - Create a new directory
- **Delete File** - Remove a file with a confirmation prompt
- **Rename File** - Change the name of an existing file
- **Copy File** - Duplicate a file to a new location
- **Move File** - Relocate a file to a different path
- **Colored UI** - Cyan, yellow, green, red, and purple terminal colors
- **Clean Screen** - Clears terminal between actions for a tidy experience

## Requirements
- Python 3.10 or higher (uses `match-case` syntax)
- No external dependencies required (uses only standard library modules)

## Installation
1. Clone or download this repository
2. Ensure Python 3.10+ is installed on your system
3. Navigate to the directory containing the script

```bash
git clone https://github.com/SamiKhan43/file-manager.git
cd file-manager
python --version  # Verify Python version
```

## Usage
Run the application from the command line:

```bash
python file_manager.py
```

Enter a number (1-8) to select an operation.

## Examples

### Listing Files
```
  Contents of: /home/user/documents
  ──────────────────────────────────────────────────
    1.  [DIR]   projects
    2.  [FILE]  file_manager.py
    3.  [FILE]  README.md
  ──────────────────────────────────────────────────
  Total: 3 item(s)
```

### Creating a File
```
  > Enter filename to create: example.txt

  'example.txt' created at /home/user/documents/example.txt
```

### Renaming a File
```
  > Enter current filename: example.txt
  > Enter new filename: sample.txt

  'example.txt' -> 'sample.txt'
```

### Deleting a File
```
  > Enter filename to delete: sample.txt
  > Are you sure you want to delete 'sample.txt'? (y/n): y

  'sample.txt' deleted.
```

## Error Handling
The application includes error handling for common scenarios:
- **Empty filenames/folder names** - Prevents creation with blank names
- **File already exists** - Alerts when trying to create a duplicate file
- **File not found** - Notifies when attempting to operate on non-existent files
- **Invalid input** - Prompts user to enter valid numeric choices
- **Accidental deletion** - Confirmation prompt before any file is deleted

## Technical Details

### Dependencies
- `os` - File and directory operations
- `shutil` - High-level file operations (copy, move)
- `pathlib.Path` - Object-oriented filesystem paths

### Code Structure

| Class | Purpose |
|---|---|
| `Colors` | Stores ANSI color codes used across the UI |
| `FileManager` | Main class — holds all file operations and the menu loop |

| Method | Purpose |
|---|---|
| `_clear()` | Clears the terminal screen |
| `_print_header()` | Prints the top banner with current directory |
| `_print_menu()` | Prints the numbered options menu |
| `_prompt()` | Styled input prompt |
| `_success()` | Green success message |
| `_error()` | Red error message |
| `_info()` | Cyan info message |
| `list_files()` | Lists contents of current directory |
| `create_file()` | Creates a new empty file |
| `create_folder()` | Creates a new folder |
| `delete_file()` | Deletes a file with confirmation |
| `rename_file()` | Renames a file |
| `copy_file()` | Copies a file to a destination |
| `move_file()` | Moves a file to a destination |
| `run()` | Main loop — handles user input and dispatches actions |

### File Operations
All operations work within the current working directory by default. Relative or absolute paths can be specified for copy and move operations.

## Project Structure
```
file-manager/
│
├── file_manager.py   # Main application
└── README.md         # This file
```

## Limitations
- All operations are performed in the current working directory by default
- No recursive folder deletion (non-empty folders cannot be deleted)
- No file content editing capabilities
- Basic error messages without detailed logging

## Future Enhancements
Potential improvements could include:
- File content viewing and editing
- Recursive directory operations
- File search functionality
- File size and metadata display
- Support for wildcards and batch operations
- Configuration file support

## License
This project is open source and available for educational and personal use.

## Contributing
Feel free to fork this project and submit pull requests for improvements or bug fixes.

## Author
Created as a learning project for Python file management operations.

