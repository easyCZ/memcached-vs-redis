import sys
import os
import argparse
import csv


class ConfigProcessor(object):
    pass


class RunProcessor(object):

    HEADERS = ['run', 'progress', 'time', 'threads', 'total_ops', 'latency', 'avg_latency']

    def __init__(self, output):
        """
        Args:
            content: [<string>]
        """
        # First two lines are descriptions
        self.output = output
        self.data = []

    def _parse_line(self, line):
        tokens = line.split(',')
        _, run, progress = tokens[0].split()
        time, _, threads, _, total_ops, _ = tokens[1].strip().split()
        latency, _, avg_latency, _, _ = tokens[-1].strip().split()
        avg_latency = avg_latency[:-1]

        return {
            'run': run,
            'progress': progress,
            'time': time,
            'threads': threads,
            'total_ops': total_ops,
            'latency': latency,
            'avg_latency': avg_latency
        }

    def process(content):
        content = content[2:]
        self.data.extend([self._parse_line(line) for line in content])

    def write(self):
        writer = csv.DictWriter(self.output, self.HEADERS)
        writer.writeheader()

        for item in data:
            writer.writerow(item)








# DELIMITER = '------------------------------------------------------------------------'
# TYPE_DELIMITER = '---'


# def process(dir_path):

#     files = []
#     for (dirpath, dirnames, filenames) in os.walk(dir_path):
#         files.extend(filenames)

#     print("msec,percent")
#     for filename in files:
#         with open(os.path.join(dir_path, filename), 'r') as f:
#             contents = f.read()
#             tokens = contents.split(DELIMITER)
#             latencies = tokens[-1]

#             sets, gets = latencies.split(TYPE_DELIMITER, 1)

#             # print(filename)
#             gets_lines = gets.strip().split('\n')
#             for line in gets_lines:
#                 _, msec, percent = line.split()
#                 print("{0},{1}".format(msec, percent))

#             # with open(os.path.join(dir_path, '%s.csv' % filename), 'w') as output:
#             #     output.write("msec,percent\n")
#             #     for line in gets_lines:
#             #         _, msec, percent = line.split()
#             #         output.write("{0},{1}\n".format(msec, percent))


def process(input_dir, output_dir):
    run_processor = RunProcessor(output_dir)

    files = []
    for (dirpath, dirnames, filenames) in os.walk(input_dir):
        files.extend(filenames)

    for filename in files:
        with open(os.path.join(input_dir, filename), 'r') as f:
            contents = f.read()

            config, rest = contents.split('===================================================')
            run, run_totals, distribution = rest.split('------------------------------------------------------------------------')
            run = run[2:-7]
            print run



    # print("msec,percent")
    # for filename in files:


def main(argv):
    parser = argparse.ArgumentParser(description='Process results.')
    parser.add_argument('-dir', dest='dir', help='Directory containg results', required=True)
    parser.add_argument('-out', dest='out', help='Output directory', required=True)

    args = parser.parse_args()
    process(args.dir, args.out)

if __name__ == "__main__":
    main(sys.argv)