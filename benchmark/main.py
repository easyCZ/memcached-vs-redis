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
        for row in content:
            f.write(str(row))
            f.write('\n')


def run(type, server_conf, memtier_conf, output_dir, base_port=11120, instances=1, duration=30):
    server = Server(type, server_conf, base_port, instances)
    clients = Clients(type, memtier_conf, base_port, instances)

    server.start_cache()
    server_cpu = server.log_cpu(duration)

    client_results = clients.run_memtier()

    memtier_parser = MemtierResultsParser(client_results)

    memtier_parser.read()

    # write results
    write(
        ', '.join(memtier_parser.get_totals_headers()),
        memtier_parser.get_averaged_totals(),
        '%s/totals.csv' % output_dir
    )


    #
    #
    # avg_latencies = []
    # last_percentiles = []
    #
    # for hostname, res in results.iteritems():
    #
    #     filename = '%s/%s.out' % (output_dir, hostname)
    #     if not os.path.exists(os.path.dirname(filename)):
    #         os.makedirs(os.path.dirname(filename))
    #
    #     content = [line for line in res['stdout']]
    #     latency_parser = LatencyParser(content)
    #
    #     avg_latency = latency_parser.get_average_latency()
    #     last_percentile = latency_parser.get_99th_latency()
    #
    #     avg_latencies.append(avg_latency)
    #     last_percentiles.append(last_percentile)
    #
    #     with open(filename, 'w') as f:
    #         for line in content:
    #             f.write(line)
    #             f.write('\n')
    #
    #     print("[Main] Wrote results for %s" % hostname)


    # cpu_average = 0
    # for hostname, res in cpu.iteritems():
    #
    #     content = [line for line in res['stdout']]
    #     cpu_average, usr_cpu, sys_cpu = CPUParser(content).get_average()
    #     print("[Main] CPU Average: " + str(cpu_average))
    #
    # # Aggregate latencies
    # with open('%s/cpu-vs-latencies.out' % output_dir, 'w') as f:
    #     f.write(str(cpu_average))
    #     f.write(', ')
    #     f.write(str(usr_cpu))
    #     f.write(', ')
    #     f.write(str(sys_cpu))
    #     f.write(', ')
    #
    #     f.write(str(avg(avg_latencies)))
    #     f.write(', ')
    #     f.write(str(avg(last_percentiles)))
    #     f.write('\n')


    # print("[Main] Writing CPU results")
    # for hostname, res in cpu.iteritems():
    #
    #     content = [line for line in res['stdout']]
    #     cpu_average = CPUParser(content).get_average()
    #
    #     with open('%s/%s.cpu.log' % (output_dir, hostname), 'w') as f:
    #         f.write(str(cpu_average))
    #         f.write('\n')
    #     print("[Main] CPU Average: " + str(cpu_average))

    # Clean up
    server.kill()


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
        args.duration
    )

if __name__ == "__main__":
    main(sys.argv)