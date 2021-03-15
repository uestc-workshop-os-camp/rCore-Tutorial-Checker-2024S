import base

EXPECTED = [
    "Test set_priority OK!",
    r"get_time OK! (\d+)",
    "Test sleep OK!",
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed!",
]

if __name__ == '__main__':
    base.test(EXPECTED)
