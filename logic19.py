def main(x):
    """
    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    return x % 10 == x // 100

x = int(input())
print(main(x))