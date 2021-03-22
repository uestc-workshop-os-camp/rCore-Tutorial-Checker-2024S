import base

EXPECTED = [
    "Test hello_world OK!",
    "Test power OK!",
    "Test write1 OK!",
]

TEMP = [
    "Test write0 OK!",
]

NOT_EXPECTED = [
    "FAIL: T.T",
]

if __name__ == '__main__':
    base.test(EXPECTED + TEMP, NOT_EXPECTED)
