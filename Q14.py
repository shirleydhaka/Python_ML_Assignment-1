lines = []
line = input("Enter a line (or press Enter to finish): ")

while line != "":
    lines.append(line)
    line = input("Enter a line (or press Enter to finish): ")

print("\nYou entered:")
print("\n".join(lines))
