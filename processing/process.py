import sys
import os
import argparse


DELIMITER = '------------------------------------------------------------------------'
TYPE_DELIMITER = '---'


def process(dir_path):

    files = []
    for (dirpath, dirnames, filenames) in os.walk(dir_path):
        files.extend(filenames)

    print("msec,percent")
    for filename in files:
        with open(os.path.join(dir_path, filename), 'r') as f:
            contents = f.read()
            tokens = contents.split(DELIMITER)
            latencies = tokens[-1]

            sets, gets = latencies.split(TYPE_DELIMITER, 1)

            # print(filename)
            gets_lines = gets.strip().split('\n')
            for line in gets_lines:
                _, msec, percent = line.split()
                print("{0},{1}".format(msec, percent))

            # with open(os.path.join(dir_path, '%s.csv' % filename), 'w') as output:
            #     output.write("msec,percent\n")
            #     for line in gets_lines:
            #         _, msec, percent = line.split()
            #         output.write("{0},{1}\n".format(msec, percent))


def main(argv):
    parser = argparse.ArgumentParser(description='Process results.')
    parser.add_argument(
        '-dir',
        dest='dir',
        help='Directory containg results',
        required=True)

    args = parser.parse_args()
    process(args.dir)

if __name__ == "__main__":
    main(sys.argv)