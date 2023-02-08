import base
from ch6 import EXPECTED, NOT_EXPECTED

EXPECTED += [
    # ch7b_sig_simple
    "signal_simple: Done",

    # ch7b_sig_simple2
    "signal_simple2: child done",
    "signal_simple2: parent Done",

    # ch7b_pipetest
    "pipetest passed!",

    # ch7b_pipe_large_test
    "pipe_large_test passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED, NOT_EXPECTED)
