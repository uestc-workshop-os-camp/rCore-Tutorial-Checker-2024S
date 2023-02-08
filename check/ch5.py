import base
from ch4 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    # ch5b_exit.rs
    "exit pass.",

    # ch5b_forktest_simple.rs
    "hello child process!",
    r"child process pid = (\d+), exit code = (\d+)",
    
    # ch5b_forktest.rs
    "forktest pass.",
]

if __name__ == '__main__':
    base.test(EXPECTED, NOT_EXPECTED)
