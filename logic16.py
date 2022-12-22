def main(a):
    """
    Given integer a,  check the following statement "The integer is a five-digit number".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return a >= pow(10,4) and a < pow(10,5)

a = int(input())

print(main(a))