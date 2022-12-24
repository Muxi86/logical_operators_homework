def main(x):
    """
    Args:
        x(int): parameter x
    Returns:
        bool: answer
    """
    return (x >= 10 and x < pow(10,2) and x%10 == x//10) or (x >= pow(10,2) and x < pow(10,3) and x%10 == x//100)

x = int(input())
print(main(x))