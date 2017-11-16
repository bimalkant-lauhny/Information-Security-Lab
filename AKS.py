def expand_x_1(n): 
# This version uses a generator and thus less computations
    c =1
    for i in range(n/2+1):
        c = c*(n-i)/(i+1)
        yield c
 
def aks(p):
    if p==2:
        return True
 
    for i in expand_x_1(p):
        if i % p:
# we stop without computing all possible solutions
            return False
    return True

def expand_x_1(p):
    ex = [1]
    for i in range(p):
        ex.append(ex[-1] * -(p-i) / (i+1))
    return ex[::-1]
 
def aks_test(p):
    if p < 2: return False
    ex = expand_x_1(p)
    ex[0] += 1
    return not any(mult % p for mult in ex[0:-1])
 
 
num = input("Enter a number: ")

if aks_test(int(num)):
    print("A prime!")

else:
    print("Not a prime!")
