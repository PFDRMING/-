This Python script generates a sorted list of filenames from a specified folder, saves the list to a text file, and names the output file with the current date in the format "List-YYYY-MM-DD.txt". Here’s how it works:

Prompt for Folder Paths: The script prompts the user to enter the source folder path (to read files) and the destination folder path (to save the output file).
Check Folder Validity: It checks if the source folder exists and verifies or creates the destination folder if it doesn’t already exist.
Sort and List Filenames: It retrieves the filenames, filters out subdirectories, sorts them alphabetically (A-Z), and numbers them in a list format.
Generate Output with Date: The list is saved to a file named "List-YYYY-MM-DD.txt" (with the current date in the format YYYY-MM-DD) in the specified destination folder.
This script is useful for quickly generating organized, date-stamped lists of files from a directory.
