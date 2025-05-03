import os
import shutil

FILE_CATEGORIES = {
    'Documents': ['.pdf', '.txt', '.docx', '.xlsx'],
    'Images': ['.jpg', '.jpeg', '.png', '.gif', '.bmp'],
    'Videos': ['.mp4', '.mkv', '.avi', '.mov'],
    'Music': ['.mp3', '.wav', '.flac'],
    'Archives': ['.zip', '.rar', '.tar', '.gz'],
}

def create_folders(directory):
    """Create necessary folders based on file categories."""
    for category in FILE_CATEGORIES:
        category_path = os.path.join(directory, category)
        if not os.path.exists(category_path):
            os.makedirs(category_path)

def move_files(directory):
    """Move files to appropriate folders based on file extensions."""
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)

        # Skip if it's a directory
        if os.path.isdir(file_path):
            continue

        # Get file extension
        file_extension = os.path.splitext(filename)[1].lower()

        # Determine the category of the file and move it to the corresponding folder
        for category, extensions in FILE_CATEGORIES.items():
            if file_extension in extensions:
                category_folder = os.path.join(directory, category)
                shutil.move(file_path, os.path.join(category_folder, filename))
                print(f"Moved: {filename} to {category}/")
                break

def file_organizer(directory):
    """Main function to organize files."""
    create_folders(directory)
    move_files(directory)
    print("File organization complete!")


directory = input("Enter the directory path to organize: ")
file_organizer(directory)
