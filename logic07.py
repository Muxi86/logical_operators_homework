def main(a,b):
    """
    Given two integers a, b,  check the following statement "At least one  of the numbers 'a' and 'b' is negative".
    Args:
        a(int): parameter a
        b(int): parameter b
    Returns:
        bool: answer
    """
    return (a >= 0 and b < 0) or (a < 0 and b >= 0)

a = int(input())
b = int(input())

print(main(a,b))