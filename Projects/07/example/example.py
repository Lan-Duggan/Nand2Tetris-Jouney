def factorial(n):
    """计算n的阶乘（递归实现）"""
    if n <= 1:
        return 1
    return n * factorial(n - 1)