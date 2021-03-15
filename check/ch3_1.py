import sys

EXPECTED = [
    """AAAAAAAAAA [1/5]
BBBBBBBBBB [1/5]
CCCCCCCCCC [1/5]
AAAAAAAAAA [2/5]
BBBBBBBBBB [2/5]
CCCCCCCCCC [2/5]
AAAAAAAAAA [3/5]
BBBBBBBBBB [3/5]
CCCCCCCCCC [3/5]
AAAAAAAAAA [4/5]
BBBBBBBBBB [4/5]
CCCCCCCCCC [4/5]
AAAAAAAAAA [5/5]
BBBBBBBBBB [5/5]
CCCCCCCCCC [5/5]
Test write A OK!
Test write B OK!
Test write C OK!""",
]

output = sys.stdin.read(1000000)

count = 0
total = len(EXPECTED)

for pattern in EXPECTED:
    if output.find(pattern) != -1:
        count += 1
        print('\033[92m[PASS]\033[0m', pattern)
    else:
        print('\033[91m[FAIL]\033[0m', pattern)

print('\nTest passed: %d/%d' % (count, total))
assert count == total
