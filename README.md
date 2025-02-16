# File Organizer by Extension

This script organizes files in a directory by their extensions. Each file is moved into a folder named after its extension.

## Features
- Automatically sorts files based on their extensions.
- Skips directories and the script file itself.
- Creates necessary folders if they don’t exist.
- Works in the current directory.

## Usage
### Prerequisites
- Python 3 installed on your system.

### Running the Script
1. Place `Files_Organizer.py` in the directory containing the files you want to organize.
2. Open a terminal or command prompt in that directory.
3. Run the script using:
   ```sh
   python Files_Organizer.py
   ```
4. The files will be sorted into folders based on their extensions.

## Example
If your directory contains:
```
document.pdf
image.jpg
script.py
```
After running the script, the directory will be organized as:
```
/pdf/document.pdf
/jpg/image.jpg
/py/script.py
```