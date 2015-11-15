#!/usr/bin/python
# mapper.py
import sys

lines = []
for line in sys.stdin:
    line = line.strip()
    # join every 3 lines
    if len(lines) == 3:
        print(', '.join(lines))
        lines = []

    lines.append(line)

print(', '.join(lines))