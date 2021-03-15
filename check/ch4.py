import sys

EXPECTED = [
    "Test 04_1 OK!",
    "Test 04_4 test OK!",
    "Test 04_5 ummap OK!",
    "Test 04_6 ummap2 OK!",
]

NOT_EXPECTED = [
    "Should cause error, Test 04_2 fail!",
]

output = sys.stdin.read(1000000)

count = 0
total = len(EXPECTED) + len(NOT_EXPECTED)

for pattern in EXPECTED:
    if output.find(pattern) != -1:
        count += 1
        print('\033[92m[PASS]\033[0m', pattern)
    else:
        print('\033[91m[FAIL]\033[0m', pattern)

for pattern in NOT_EXPECTED:
    if output.find(pattern) == -1:
        count += 1
        print('\033[92m[PASS]\033[0m', pattern)
    else:
        print('\033[91m[FAIL]\033[0m', pattern)

print('\nTest passed: %d/%d' % (count, total))
assert count == total
