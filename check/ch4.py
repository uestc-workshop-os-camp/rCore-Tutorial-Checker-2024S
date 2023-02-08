import base
from ch3 import EXPECTED, NOT_EXPECTED


EXPECTED += [
    "Test sbrk almost OK!",
]

NOT_EXPECTED += [
    "Test sbrk failed!",
]

if __name__ == "__main__":
    base.test(EXPECTED, NOT_EXPECTED)
