import base
from ch2 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    "Test write A OK!",
    "Test write B OK!",
    "Test write C OK!",
]

if __name__ == "__main__":
    base.test(EXPECTED, NOT_EXPECTED)
