import os
import shutil
from collections import defaultdict

# File categories
FILE_TYPES = {
    "Images": [".jpg", ".jpeg", ".png", ".gif", ".bmp"],
    "Documents": [".pdf", ".docx", ".doc", ".txt", ".pptx", ".xlsx"],
    "Videos": [".mp4", ".mkv", ".avi", ".mov"],
    "Music": [".mp3", ".wav", ".aac"],
    "Archives": [".zip", ".rar", ".7z"],
    "Programs": [".exe", ".msi"]
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension in extensions:
            return category
    return "Others"

def organize_files(folder_path):
    summary = defaultdict(int)

    if not os.path.exists(folder_path):
        print("❌ Folder does not exist!")
        return

    for file in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file)

        if os.path.isfile(file_path):
            _, ext = os.path.splitext(file)
            ext = ext.lower()

            category = get_category(ext)
            category_path = os.path.join(folder_path, category)

            if not os.path.exists(category_path):
                os.makedirs(category_path)

            shutil.move(file_path, os.path.join(category_path, file))
            summary[category] += 1

    print("\n✅ File Organization Summary:")
    print("--------------------------------")
    for category, count in summary.items():
        print(f"{category}: {count} files moved")

if __name__ == "__main__":
    folder = input("Enter folder path to organize: ")
    organize_files(folder)
