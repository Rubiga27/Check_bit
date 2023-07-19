A = int(input("Enter the value of A: "))
B = int(input("Enter the value of B: "))
mask = 1 << B
if (A & mask) != 0:
    result = 1
else:
    result = 0
print(result)
