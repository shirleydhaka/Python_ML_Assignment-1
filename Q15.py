import csv

# Open the CSV file
with open('data.csv', mode='r', newline='') as file:
    reader = csv.reader(file)
    
    # Iterate over each row in the CSV file
    for row in reader:
        # Print the row
        print(', '.join(row))
