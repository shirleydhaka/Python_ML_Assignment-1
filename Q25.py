# Open the source file for reading
try:
    with open("source.txt", "r") as source_file:
        # Read the contents of the source file
        content = source_file.read()

        # Open the destination file for writing
        with open("destination.txt", "w") as destination_file:
            # Write the contents to the destination file
            destination_file.write(content)

        print("File copied successfully.")
except FileNotFoundError:
    print("Source file not found.")
except Exception as e:
    print(f"An error occurred: {str(e)}")
