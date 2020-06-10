## Iterative Solution
## Plan
### Go from 1 to n, or n to 1


def iter_factorial(n):

### make a tracker: total
    total = 1
### make a while loop, and decrement n as we go
    while n != 1:
### multiply our tracker at every step
        total *= n
        n -= 1

    return total
### return tracker


print(iter_factorial(4))

def iter_power(a, b):
    product = a

    while b != 1:
        product *= a
        b -= 1

    return product


print(iter_power(5,5))

def power(a, b):
    if type(b) is not int:
        return "Sorry we don't handle decimals."
    
    if b == 0:
        return 1

    invert = False
    if b < 0:
        b *= -1
        invert = True

    product = a

    while b != 1:
        product *= a
        b -= 1


    if invert:
        return 1 / product
    else:
        return product