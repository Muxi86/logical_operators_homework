def main(a):
    """
    Given a two-digit integer a,  check the following statement "All digits sum is odd".
    Args:
        a(int): parameter a
    Returns:
        bool: answer
    """
    return (int(a//10) + int(a%10))%2 != 0

a = int(input())

print(main(a))