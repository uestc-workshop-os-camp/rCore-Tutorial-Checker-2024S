import base
from ch4 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    r"Test getpid OK! pid = (\d+)",
    "Test spawn0 OK!",
    "Test wait OK!",
    "Test waitpid OK!",
    "ch5 Usertests passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED, NOT_EXPECTED)
