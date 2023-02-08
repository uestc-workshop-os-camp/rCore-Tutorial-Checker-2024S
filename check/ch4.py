import base
from ch3 import NOT_EXPECTED


EXPECTED = [
    # ch3b_yield0
    "Test write A OK!",

    # ch3b_yield1
    "Test write B OK!",

    # ch3b_yield2
    "Test write C OK!",

    # ch4b_sbrk
    "Test sbrk almost OK!",
]

NOT_EXPECTED += [
    "Test sbrk failed!",
]

if __name__ == "__main__":
    base.test(EXPECTED, NOT_EXPECTED)
