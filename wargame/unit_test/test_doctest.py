#!/usr/bin/env python
# -*- Coding：utf-8 -*-

import doctest
import knight                                    # modules contains doctests test case
import accessoryfactory


def load_tests(loader, tests, ignore):     # required for Test Discovery to work
    tests.addTests(doctest.DocTestSuite(knight))
    tests.addTests(doctest.DocTestSuite(accessoryfactory))
    return tests


def add(a, b):
    """
    Return the addition of the arguments: a + b
     
    >>> add(1, 2)
    3
    >>> add(-1, 10)
    9
    >>> add('a', 'b')
    'ab'
    >>> add(1, '2')
    Traceback (most recent call last):
    TypeError: unsupported operand type(s) for +: 'int' and 'str'
    """
    return a + b


if __name__ == '__main__':
    # import doctest
    doctest.testmod()
