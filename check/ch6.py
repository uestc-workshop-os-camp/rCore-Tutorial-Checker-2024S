import base
from ch5 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    # ch6b_filetest_simple.rs
    "file_test passed!",

    # ch6b_cat.rs
    "Hello World!"
]

if __name__ == '__main__':
    base.test(EXPECTED, NOT_EXPECTED)
