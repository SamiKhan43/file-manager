Readme · MD
# File Manager

A simple command-line file management application built with Python that allows users to perform common file and folder operations.

## project link
* [file manager](https://github.com/SamiKhan43/file-manager)
## Features

- **List Files** - Display all files and folders in the current directory
- **Create File** - Create a new empty file
- **Create Folder** - Create a new directory
- **Delete File** - Remove a file from the system
- **Rename File** - Change the name of an existing file
- **Copy File** - Duplicate a file to a new location
- **Move File** - Relocate a file to a different path

## Requirements

- Python 3.10 or higher (uses `match-case` syntax)
- No external dependencies required (uses only standard library modules)

## Installation

1. Clone or download this repository
2. Ensure Python 3.10+ is installed on your system
3. Navigate to the directory containing the script

```bash
python --version  # Verify Python version
```

## Usage

Run the application from the command line:

```bash
python file_manager.py
```

### Menu Options

Once launched, you'll see the following menu:

```
======Welcome to the File Manager=======

1. list files - List all files in the current directory
2. create file - Create a new file
3. create folder - Create a new folder
4. delete file - Delete a file
5. rename file - Rename a file
6. copy file - Copy a file
7. move file - Move a file
8. exit - Exit the File Manager application
```

Enter a number (1-8) to select an operation.

## Examples

### Creating a File
```
Enter your choice:(1-8): 2
Enter the name of the file to create: example.txt

Creating file 'example.txt'...
File 'example.txt' created successfully.
Absolute path: /path/to/current/directory/example.txt
```

### Listing Files
```
Enter your choice:(1-8): 1
Files in current directory:
------------------------------
# file_manager.py
# example.txt
# README.md
------------------------------
Total files: 3
```

### Renaming a File
```
Enter your choice:(1-8): 5
Current files and folders:
[list displayed]
Enter the current name of the file: example.txt
Enter the new name of the file: sample.txt
File 'example.txt' renamed to 'sample.txt' successfully.
```

## Error Handling

The application includes error handling for common scenarios:

- **Empty filenames/folder names** - Prevents creation with blank names
- **File already exists** - Alerts when trying to create a duplicate file
- **File not found** - Notifies when attempting to operate on non-existent files
- **Invalid input** - Prompts user to enter valid numeric choices

## Technical Details

### Dependencies
- `os` - File and directory operations
- `shutil` - High-level file operations (copy, move)
- `pathlib.Path` - Object-oriented filesystem paths

### File Operations

All operations work within the current working directory by default. You can specify relative or absolute paths for copy and move operations.

## Limitations

- All operations are performed in the current working directory by default
- No recursive folder operations (e.g., deleting non-empty folders)
- No file content editing capabilities
- Basic error messages without detailed logging

## Future Enhancements

Potential improvements could include:
- File content viewing and editing
- Recursive directory operations
- File search functionality
- File size and metadata display
- Support for wildcards and batch operations
- Colorized terminal output
- Configuration file support

## License

This project is open source and available for educational and personal use.

## Contributing

Feel free to fork this project and submit pull requests for improvements or bug fixes.

## Author

Created as a learning project for Python file management operations.
