import base
# from ch2 import EXPECTED, NOT_EXPECTED

EXPECTED = [
    """string from data section
strinstring from stack section
strin
Test write1 OK!
Test write0 OK!""",
    "Test set_priority OK!",
]
NOT_EXPECTED = []
if __name__ == '__main__':
    base.test(EXPECTED, NOT_EXPECTED)
