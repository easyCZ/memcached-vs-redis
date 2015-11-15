import sys

lines = []

# Should receive it sorted
print('cpu, latency, 99th')
for line in sys.stdin:
    cpu, latency, last = line.strip().split(',')

    lines.append((float(cpu), float(latency), float(last)))
    if len(lines) == 3:
        avg_cpu = sum([c for c, l, q in lines]) / 3
        avg_latency = sum([l for c, l, q in lines]) / 3
        avg_last = sum([q for c, l, q in lines]) / 3
        print(', '.join([str(avg_cpu), str(avg_latency), str(avg_last)]))
        lines = []