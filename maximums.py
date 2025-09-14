# Replace the "ANSWER HERE" for your answer
def max_of_two(x, y):
    """Given x and y, that are 2 numbers, return the biggest number."""
    if x == y:
        mayor = x
    elif x > y:
        mayor = x
    elif x < y:
        mayor = y
    return mayor # Remove this line and implement

def max_of_three(x, y, z):
    """Given x, y and z, that are 3 numbers, return the biggest number of the three."""
    if (x == y) and (x == z):
        mayor = x
    elif x > y and x > z:
        mayor = x
    elif y > x and y > z:
        mayor = y
    elif z > x and z > y:
        mayor = z
    return mayor # Remove this line and implement