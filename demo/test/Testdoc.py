def fact(n):
    '''
    Python内置的“文档测试”（doctest）模块可以直接提取注释中的代码并执行测试
    Calculate 1*2*...*n

    >>> fact(1)
    1
    >>> fact(10)
    ?
    >>> fact(-1)
    ?
    '''
    if n < 1:
        raise ValueError()
    if n == 1:
        return 1
    return n * fact(n - 1)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
