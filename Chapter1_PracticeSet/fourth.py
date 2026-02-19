import os

# specify the directory path
directory = "/"

# getting list of files and folders
contents = os.listdir(directory)

print(f"Contents of '{directory}' directory:")
for item in contents:
    print(item)
