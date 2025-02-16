import os
import shutil

def organize_files_by_extension(root_folder):
    # Get a list of all files and folders in the root directory
    for item in os.listdir(root_folder):
        item_path = os.path.join(root_folder, item)
        
        # Skip directories and the script file itself
        if os.path.isdir(item_path) or item == "File_Organizer.py":
            continue

        # Get the file extension
        file_extension = os.path.splitext(item)[1].lower()  # Extension in lowercase
        
        # Skip files without an extension
        if not file_extension:
            continue
        
        # Create a folder for the extension if it doesn't exist
        folder_name = file_extension[1:]  # Remove the dot from the extension
        folder_path = os.path.join(root_folder, folder_name)
        os.makedirs(folder_path, exist_ok=True)
        
        # Move the file to the appropriate folder
        shutil.move(item_path, os.path.join(folder_path, item))
        print(f"Moved: {item} to {folder_name} folder.")

# Main function to organize files in the root folder
if __name__ == "__main__":
    root_folder = os.path.abspath(".")  # Current directory as root folder
    organize_files_by_extension(root_folder)
    print("File organization complete.")