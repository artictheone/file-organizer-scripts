"""
Clean up empty folders within specific directories on a user's system.

This script walks through the specified folder paths, checks for empty folders,
and moves them to the trash.
"""

import os  # provides a way to use operating system dependent functionality
import shutil  # offers high-level file operations, such as moving files
import logging  # allows for logging events and errors

def clean_empty_date_folders():
    """
    Clean up empty folders within specific directories on a user's system.

    This function walks through the specified folder paths, checks for empty folders,
    and moves them to the trash.
    """
    folders_to_check = [
        os.path.join(os.path.expanduser("~"), "Desktop", "Archive"),  # Check Desktop/Archive
        os.path.join(os.path.expanduser("~"), "Downloads", "Archive")  # Check Downloads/Archive
    ]  # List of folder paths to check for empty folders

    for folder_path in folders_to_check:
        """
        Iterate through each folder path and its subdirectories.
        """
        for root, dirs, files in os.walk(folder_path):
            """
            Walk through the folder path and its subdirectories.
            """
            for dir in dirs:
                dir_path = os.path.join(root, dir)  # Construct the full path to the subdirectory
                """
                Check if the subdirectory is empty.
                """
                if not os.listdir(dir_path):
                    logging.debug(f"Moving empty folder {dir_path} to trash")
                    try:
                        """
                        Attempt to move the empty folder to the trash.
                        """
                        shutil.move(dir_path, os.path.join(os.path.expanduser("~"), "Trash"))
                    except Exception as e:
                        """
                        Log an error message if an exception occurs while moving the folder.
                        """
                        logging.error(f"Error moving folder to trash: {e}")

if __name__ == "__main__":
    """
    Run the clean_empty_date_folders function when the script is executed directly.
    """
    clean_empty_date_folders()