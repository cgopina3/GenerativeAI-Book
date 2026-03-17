eps = 1.0
one = 1.0
while one + eps != one:
    eps /= 2.0
eps *= 2.0
print("Machine epsilon:", eps)
print("1.0 + eps =", one + eps)
print("1.0 + eps/2 =", one + eps/2)
