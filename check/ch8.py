import base
from ch6 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    # ch7b
    "pipetest passed!",
    # ch8b
    "mpsc_sem passed!",
    "philosopher dining problem with mutex test passed!",
    "race adder using spin mutex test passed!",
    "sync_sem passed!",
    "test_condvar passed!",
    "threads with arg test passed!",
    "threads test passed!",
]

EXPECTED = list(set(EXPECTED) - set(["Test sbrk almost OK!"]))

if __name__ == "__main__":
    base.test(EXPECTED, NOT_EXPECTED)
