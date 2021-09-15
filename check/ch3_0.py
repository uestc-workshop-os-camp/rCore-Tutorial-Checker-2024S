import base
from ch2 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    "Test set_priority OK!",
]

if __name__ == '__main__':
    base.test(EXPECTED, NOT_EXPECTED)
