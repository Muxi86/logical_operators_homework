def main(a,b,c):
    """
    Given three integers a, b, c,  check the following statement "The number b is between a and c".
    Args:
        a(int): parameter a
        b(int): parameter b
        c(int): parameter c
    Returns:
        bool: answer
    """
    return (a>b and b>c) or (a<b and b<c)

a = int(input())
b = int(input())
c = int(input())

print(main(a,b,c))