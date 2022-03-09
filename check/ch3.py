import base
# from ch2 import EXPECTED, NOT_EXPECTED

EXPECTED = [
    """
string from task info test

Test task info OK!"""
]
NOT_EXPECTED = []
if __name__ == '__main__':
    base.test(EXPECTED, NOT_EXPECTED)
