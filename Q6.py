file_path = 'your_file.txt'  # Replace with the path to your file

file = open(file_path, 'r')
content = file.read()
print(content)
file.close()
