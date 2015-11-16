import sys

lines = []

# Should receive it sorted
print('usr, sys, cpu, latency, 99th')
for line in sys.stdin:
    cpu, usr, sys, latency, last = line.strip().split(',')

    lines.append((float(cpu), float(usr), float(sys), float(latency), float(last)))
    if len(lines) == 3:
        avg_cpu = sum([c for c, usr, sys, l, q in lines]) / 3
        avg_latency = sum([l for c, usr, sys, l, q in lines]) / 3
        avg_last = sum([q for c, usr, sys, l, q in lines]) / 3
        avg_usr = sum([usr for c, usr, sys, l, q in lines]) / 3
        avg_sys = sum([sys for c, usr, sys, l, q in lines]) / 3
        print(', '.join([str(avg_usr), str(avg_sys), str(avg_cpu), str(avg_latency), str(avg_last)]))
        lines = []