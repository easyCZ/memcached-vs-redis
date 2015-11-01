import sys
import argparse
from clients import Clients
from server import Server


def run(type, port, server_conf, memtier_conf):

    server = Server(type, server_conf)
    server.run()

    clients = Clients(type, memtier_conf)
    results = clients.run()
    print("Waiting for results to finish.")

    for hostname, res in results.iteritems():

        with open('../out/test/%s.out' % hostname, 'w') as f:
            for line in res['stdout']:
                f.write(line)

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
    parser.add_argument('-port', dest='port', help='Port number for server', required=True)
    parser.add_argument('-server-conf', dest='server_conf', help='Server config', required=True)
    parser.add_argument('-memtier-conf', dest='memtier_conf', help='Memtier config', required=True)

    args = parser.parse_args()
    server_conf = parse_config(args.server_conf)
    memtier_conf = parse_config(args.memtier_conf)
    run(args.type, args.port, server_conf, memtier_conf)

if __name__ == "__main__":
    main(sys.argv)