from collections import Counter
input_string = input("Enter a string: ")

frequency = Counter(input_string)

print("\nCharacter frequencies:")
for char, count in frequency.items():
    print(f"{char}: {count}")
