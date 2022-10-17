def main(a,b,c):
    """
    Find how many negative numbers there are in the given numbers.
    Args:
        a: integer
        b: integer
        c: integer
    returns:
        integer: the number of negative numbers in the given numbers
    """
    
    if a>0:
        s=0
    if a<0:
        s=1
    if b>0:
       k=0
    if b<0:
       k=1
    if c>0:
       d=0
    if c<0:
       d=1
    return d+k+s
print(main(-7,-9,8))
