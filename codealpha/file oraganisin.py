import os
import shutil

def organize_files(directory):
    # Dictionary to hold file extensions and corresponding folders
    extensions_folders = {
        "": "Other",
        ".txt": "Text",
        ".pdf": "PDF",
        ".jpg": "Images",
        ".png": "Images",
        ".xlsx": "Spreadsheets",
        ".docx": "Documents",
        ".pptx": "Presentations"
        # Add more file extensions and corresponding folders as needed
    }

    # Create folders if they don't exist already
    for folder in extensions_folders.values():
        folder_path = os.path.join(directory, folder)
        os.makedirs(folder_path, exist_ok=True)

    # Organize files
    for filename in os.listdir(directory):
        if os.path.isfile(os.path.join(directory, filename)):
            file_extension = os.path.splitext(filename)[1]
            dest_folder = extensions_folders.get(file_extension, "Other")
            dest_path = os.path.join(directory, dest_folder, filename)
            src_path = os.path.join(directory, filename)
            shutil.move(src_path, dest_path)
            print(f"Moved {filename} to {dest_folder} folder.")

if __name__ == "__main__":
    directory = input("Enter the directory path to organize files: ")
    if os.path.isdir(directory):
        organize_files(directory)
        print("Files organized successfully.")
    else:
        print("Invalid directory path.")
