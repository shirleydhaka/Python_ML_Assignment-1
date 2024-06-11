# Ask user for input
choice = input("Enter 'C' to convert from Celsius to Fahrenheit, "
               "or 'F' to convert from Fahrenheit to Celsius: ")

# Perform conversion based on user choice
if choice == 'C' or choice == 'c':
    celsius = float(input("Enter temperature in Celsius: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius}°C is equal to {fahrenheit}°F")
elif choice == 'F' or choice == 'f':
    fahrenheit = float(input("Enter temperature in Fahrenheit: "))
    celsius = (fahrenheit - 32) * 5/9
    print(f"{fahrenheit}°F is equal to {celsius}°C")
else:
    print("Invalid choice. Please enter 'C' or 'F'.")
