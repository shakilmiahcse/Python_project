a = float(1.0)
b = float(2.0)
epsilon = float(0.0001)
c = float(0.0)
iterations = 0
while abs(b-a) >= epsilon:
    c = (a + b)/2
    result = float(pow(c, 3) - c - 1)
    if result == 0.0:
        break
    elif result * (pow(a, 3) - a - 1 < 0):
        b = c
    else:
        a = c
    iterations += iterations

print("Root found after ", iterations, "iterations.\n")
print("Approximate root: ", c, "\n")
