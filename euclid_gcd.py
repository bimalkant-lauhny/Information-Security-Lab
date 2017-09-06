def gcd(a, b):
    if (a == 0):
        return b
    else:
        return gcd(b%a, a)


print("Enter two numbers:")
a = int(input("First number:"))
b = int(input("Second number:"))
print("GCD({0}, {1}): {2} ".format(a, b, gcd(a, b)))
