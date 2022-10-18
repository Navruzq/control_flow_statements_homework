def main(a):
    """
    Given an integer a, check the following conditions:
    "two-digit odd number",
    "two-digit even number",
    "three-digit odd number",
    "three-digit even number"

    Args:
        a: integer
    Returns:
        string: the message to print
    """
    m=0
    
    if abs(a)<100:
          if a%2>0:
             m="two-digit odd number" 
          if a%2==0:
             m="two-digit even number"
    if abs(a)>=100:
          if a%2>0:
             m="three-digit odd number" 
          if a%2==0:
             m="three-digit even number"
    return m
print(main(-242))

