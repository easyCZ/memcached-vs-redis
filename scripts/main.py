import sys
import argparse
from clients import Clients
from server import Server


def run(type, port, server_conf, memtier_conf):

    server = Server(type, server_conf)
    server.run()

    clients = Clients(type, memtier_conf)
    results = clients.run()
    print results

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