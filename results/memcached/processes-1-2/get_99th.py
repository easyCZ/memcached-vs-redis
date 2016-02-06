import sys

parse = False

for line in sys.stdin:
    line = line.strip()
    if parse:
        op, msec, percent = line.split()
        msec = float(msec)
        percent = float(percent)
        if percent > 99.0:
            print msec
            parse = False

    if line == '---':
        parse = True

