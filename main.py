import os

# Set the paths of the folders to be compared
folder1_path = "C:/Users/username/Documents/folder1"
folder2_path = "C:/Users/username/Documents/folder2"

# Get the list of files and folders in the first folder
folder1_contents = os.listdir(folder1_path)

# Get the list of files and folders in the second folder
folder2_contents = os.listdir(folder2_path)

# Check if all the items in the first folder are also present in the second folder
for item in folder1_contents:
    if item not in folder2_contents:
        print(f"{item} is missing from {folder2_path}")
