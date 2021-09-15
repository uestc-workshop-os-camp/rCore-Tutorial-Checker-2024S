import base


EXPECTED = [
    r"get_time OK! (\d+)",
    "Test sleep OK!",
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed!",
    "Test 04_1 OK!",
    "Test 04_4 test OK!",
    "Test 04_5 ummap OK!",
    "Test 04_6 ummap2 OK!",
]

NOT_EXPECTED = [
    "Should cause error, Test 04_2 fail!",
]

if __name__ == '__main__':
    base.test(EXPECTED, NOT_EXPECTED)
