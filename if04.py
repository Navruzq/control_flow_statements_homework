def main(a,b,c):
    """
    Find how many positive numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of positive numbers in the given numbers
    """
    if a>0:
        s=1
    if a<0:
        s=0
    if b>0:
       k=1
    if b<0:
       k=0
    if c>0:
       d=1
    if c<0:
       d=0
    return d+k+s
print(main(1,-3,7))


