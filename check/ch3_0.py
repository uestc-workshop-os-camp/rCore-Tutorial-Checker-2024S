import sys
import re

EXPECTED = [
    "Test set_priority OK!",
    r"get_time OK! (\d+)",
    "Test sleep OK!",
    r"current time_msec = (\d+)",
    r"time_msec = (\d+) after sleeping (\d+) ticks, delta = (\d+)ms!",
    "Test sleep1 passed!",
]

output = sys.stdin.read(1000000)

count = 0
total = len(EXPECTED)

for pattern in EXPECTED:
    if re.search(pattern, output):
        count += 1
        print('\033[92m[PASS]\033[0m', pattern)
    else:
        print('\033[91m[FAIL]\033[0m', pattern)

print('\nTest passed: %d/%d' % (count, total))
assert count == total
