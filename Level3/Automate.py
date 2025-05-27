"""Identify a repetitive task, such as data
processing, file management, or report
generation, and develop a script to
automate it using Python. This task will
showcase their problem-solving skills and
familiarity with Python's automation
capabilities."""

import os
import shutil

def organize_files_by_extension(folder_path):
    # Create a directory for each file extension
    for filename in os.listdir(folder_path):
        if os.path.isfile(os.path.join(folder_path, filename)):
            ext = filename.split('.')[-1]
            ext_folder = os.path.join(folder_path, ext)
            os.makedirs(ext_folder, exist_ok=True)
            shutil.move(os.path.join(folder_path, filename), os.path.join(ext_folder, filename))
def main():
    folder_path = input("Enter the path to the folder to organize: ")
    if not os.path.isdir(folder_path):
        print("The provided path is not a valid directory.")
        return
    organize_files_by_extension(folder_path)
    print("Files have been organized by their extensions.")

if __name__ == "__main__":
    main()