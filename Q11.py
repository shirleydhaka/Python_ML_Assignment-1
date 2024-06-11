n = int(input("Enter the number of terms: "))

a, b = 0, 1

fib_sequence = []

for _ in range(n):
    fib_sequence.append(a)
    a, b = b, a + b

print("Fibonacci sequence:")
print(fib_sequence)
