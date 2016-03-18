import sys
import os
import argparse
from clients import Clients
from parsers.memtier import MemtierResultsParser
from server import Server
from parsers.cpu import CPUParser
from parsers.latency import LatencyParser


def avg(data):
    if len(data) > 0:
        return sum(data) / len(data)
    return 0

def write(headers, content, path):
    if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
    with open(path, 'w') as f:
        f.write(headers)
        f.write('\n')
        f.write(', '.join(map(str, content)))
        f.write('\n')

def write_dict(data, path):
    if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))

    with open(path, 'w') as f:
        headers = data.values()
        values = [data[header] for header in headers]
        f.write(', '.join(headers))
        f.write('\n')
        f.write(', '.join(values))
        f.write('\n')

def write_stats(content, path):
    if not os.path.exists(os.path.dirname(path)):
            os.makedirs(os.path.dirname(path))
    for key, values in content.iteritems():
        for i, instance in enumerate(values):
            with open(path + '/%s.%d.out' % (key, i), 'w') as f:
                for line in instance:
                    f.write(line)
                    f.write('\n')


def run(type, server_conf, memtier_conf, output_dir, base_port=11120, instances=1, duration=30, zipf=False, pin=False):
    server = Server(type, server_conf, base_port, instances)
    clients = Clients(type, memtier_conf, base_port, instances, zipf=zipf)

    server.start_cache()

    if pin:
        server.pin()

    server_cpu = server.log_cpu(duration + 1)

    cpu_parser = CPUParser()

    client_results = clients.run_memtier(False)

    memtier_parser = MemtierResultsParser(client_results)

    memtier_parser.read()

    # print(memtier_parser.content)
    write_stats(memtier_parser.content, output_dir)

    # write results
    write(
        ', '.join(memtier_parser.get_totals_headers()),
        memtier_parser.get_averaged_totals(),
        '%s/totals.csv' % output_dir
    )

    write(
        '99th latency',
        [memtier_parser.get_average_99th()],
        '%s/latency.csv' % output_dir
    )

    server_cpu_averages = cpu_parser.get_average_stats(server_cpu)
    print('CPU', server_cpu_averages)

    write_dict(server_cpu_averages, '%s/cpu.csv' % output_dir)

    # write(
    #     ', '.join(cpu_parser.get_labels()),
    #     server_cpu_averages.values(),
    #     '%s/cpu.csv' % output_dir
    # )

    print('Average 99th:', memtier_parser.get_average_99th())

    # Clean up
    server.kill_cache()


def parse_config(path):
    with open(path) as f:
        return " ".join([line.strip() for line in f if not line.strip().startswith('#')])


def main(argv):
    parser = argparse.ArgumentParser(description='Run performance tests.')
    parser.add_argument('-type', dest='type', help='Type of cache', required=True, choices=['memcached', 'redis'])
    parser.add_argument('-server-conf', dest='server_conf', help='Server config', required=True)
    parser.add_argument('-memtier-conf', dest='memtier_conf', help='Memtier config', required=True)
    parser.add_argument('-output', dest='output', help='The directory to put the output of clients into', required=True)
    parser.add_argument('-base-port', dest='base_port', default=1, type=int)
    parser.add_argument('-instances', type=int, dest='instances', default=1)
    parser.add_argument('-duration', type=int, dest='duration', default=30)
    parser.add_argument('-zipf', type=bool, dest='zipf', default=False)
    parser.add_argument('-pin', type=bool, dest='pin', default=False)


    args = parser.parse_args()
    server_conf = parse_config(args.server_conf)
    memtier_conf = parse_config(args.memtier_conf)

    run(
        args.type,
        server_conf,
        memtier_conf,
        args.output,
        args.base_port,
        args.instances,
        args.duration,
        zipf=args.zipf,
        pin=args.pin
    )

if __name__ == "__main__":
    main(sys.argv)
