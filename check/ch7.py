import base
from ch6 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    "Test file0 OK!",
    "Test fstat OK!",
    "Test link OK!",
]

if __name__ == '__main__':
    base.test(EXPECTED, NOT_EXPECTED)
