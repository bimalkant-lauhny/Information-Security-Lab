
def mod_poly(a, b):
    print ("Received: ", a, b)
    coeff = None

    for i in range(0, len(a)):
        if a[i] != 0:
            coeff = i
            break

    if (coeff == None):
        print ("None: ", b)
        return b

    a_coeff = a[coeff]
    b_coeff = b[coeff]

    a = [i*b_coeff for i in a]
    b = [i*a_coeff for i in b]

    for i in range(0, len(a)):
        a[i] = a[i] - b[i]

    print ("mod res: ", a)
    return a

def poly_gcd(a, b):
    coeff = None
    for i in range(0, len(a)):
        if a[i] != 0:
            coeff = a[i]
            break

    if (coeff == None):
        return b
    else:
        return poly_gcd(mod_poly(b, a), a)

print ("Enter the two polynomials:")
print("Enter first polynomial (coefficients seperated by a space only):")
a = (input()).split(' ')
a = [int(i) for i in a]
print("Enter second polynomial (coefficients seperated by a space only):")
b = (input()).split(' ')
b = [int(i) for i in b]
print("GCD({0}, {1}): {2}".format(a, b, poly_gcd(a, b)))

