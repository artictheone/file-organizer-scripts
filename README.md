# File Organizer Scripts

## Overview

This repository contains two Python scripts that help to keep your computer organized and clutter-free by moving files and folders to an "Archive" folder and removing empty folders.

## Scripts

### Organization Script (`organizacion.py`)

The Organization Script helps to organize files and folders on your computer. It takes two folders, Desktop and Downloads, and moves their contents to an "Archive" folder with the current date. The script skips alias files and folders, and renames files with the same name by adding a "_1" suffix. The script also logs its progress and any errors that occur during the organization process.

### Clean Script (`clean.py`)

The Clean Script cleans up empty folders in the "Archive" folders of your Desktop and Downloads folders. It walks through the folder tree, checks for empty folders, and moves them to the trash. The script logs its progress and any errors that occur during the cleaning process.

## Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/artictheone/file-organizer-scripts.git
   cd file-organizer-scripts

2. **Set up a virtual environment (optional but recommended)**:
    ```bash
    python3 -m venv venv
    source venv/bin/activate

3. **Make the scripts executable**:

     ```bash
    chmod +x organizacion.py clean.py

## Usage
Running the Scripts Manually
To run the scripts, use the following commands in your terminal:

      python3 organizacion.py
      python3 clean.py

## Automating with Automator (macOS)
For a seamless experience, you can set up these scripts to run automatically using Automator on macOS. Here's how:

1. Open Automator and create a new "Application".
2. Add a "Run Shell Script" action.
3. Set the Shell to /bin/bash and Pass input to as arguments.
4. In the script area, enter the path to your script. For example:

      ```bash
      python3 /path/to/your/file-organizer-scripts/organization.py
      python3 /path/to/your/file-organizer-scripts/clean.py

5. Save the Automator application.
You can now run these scripts by double-clicking the Automator application.

## Note
These scripts have been tested only on macOS. Compatibility with other operating systems has not been verified.

## License
This project is licensed under the MIT License. See the LICENSE file for details.
