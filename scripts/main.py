import sys
import os
import argparse
from clients import Clients
from server import Server


def run(type, server_conf, memtier_conf, output_dir):

    server = Server(type, server_conf)
    server.run()

    clients = Clients(type, memtier_conf)
    results = clients.run()

    print("[Main] Writing results to files.")
    for hostname, res in results.iteritems():

        filename = '%s/%s.out' % (output_dir, hostname)
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

        with open(filename, 'w') as f:
            for line in res['stdout']:
                f.write(line)
                f.write('\n')

        print("[Main] Wrote results for %s" % hostname)

        # out = "\n".join([line for line in res['stdout']])
        # print("%s: %s\n" % (hostname, out))

    # Clean up
    # server.kill()


def parse_config(path):
    with open(path) as f:
        return " ".join([line.strip() for line in f])


def main(argv):
    parser = argparse.ArgumentParser(description='Run performance tests.')
    parser.add_argument('-type', dest='type', help='Type of cache', required=True, choices=['memcached', 'redis'])
    parser.add_argument('-server-conf', dest='server_conf', help='Server config', required=True)
    parser.add_argument('-memtier-conf', dest='memtier_conf', help='Memtier config', required=True)
    parser.add_argument('-output', dest='output', help='The directory to put the output of clients into', required=True)

    args = parser.parse_args()

    if args.type == 'redis':
        # Use the filename directly
        server_conf = args.server_conf
    else:
        server_conf = parse_config(args.server_conf)
    memtier_conf = parse_config(args.memtier_conf)
    run(args.type, server_conf, memtier_conf, args.output)

if __name__ == "__main__":
    main(sys.argv)