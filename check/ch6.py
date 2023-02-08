import base
from ch5 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    # ch6b_filetest_simple.rs
    "file_test passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED, NOT_EXPECTED)
