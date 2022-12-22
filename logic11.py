def main(a):
    """
    Given integer a,  check the following statement "The integer is three-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (99 < a and a < 1000) or (-99 > a and a > -1000)

a = int(input())

print(main(a))