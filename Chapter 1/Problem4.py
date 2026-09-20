import os

# Select the directory whose content you want to list 
dir_path = '/' 

# Use the os module to list the directory content 
contents = os.listdir(dir_path)

# Print the contents of the directory
print(contents)
