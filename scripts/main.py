import sys
import os
import argparse
from clients import Clients
from server import Server
from parsers.cpu import CPUParser
from parsers.latency import LatencyParser


def avg(data):
    if len(data) > 0:
        return sum(data) / len(data)
    return 0


def run(type, server_conf, memtier_conf, output_dir):

    server = Server(type, server_conf)

    # Temporary
    if type != 'redis':

        server.start()

    # Enable CPU logging
    cpu = server.log_cpu()

    clients = Clients(type, memtier_conf)
    results = clients.run()

    print("[Main] Writing results to files.")

    avg_latencies = []
    last_percentiles = []

    for hostname, res in results.iteritems():

        filename = '%s/%s.out' % (output_dir, hostname)
        if not os.path.exists(os.path.dirname(filename)):
            os.makedirs(os.path.dirname(filename))

        content = [line for line in res['stdout']]
        latency_parser = LatencyParser(content)

        avg_latency = latency_parser.get_average_latency()
        last_percentile = latency_parser.get_99th_latency()

        avg_latencies.append(avg_latency)
        last_percentiles.append(last_percentile)

        with open(filename, 'w') as f:
            for line in content:
                f.write(line)
                f.write('\n')

        print("[Main] Wrote results for %s" % hostname)


    cpu_average = 0
    for hostname, res in cpu.iteritems():

        content = [line for line in res['stdout']]
        cpu_average, usr_cpu, sys_cpu = CPUParser(content).get_average()
        print("[Main] CPU Average: " + str(cpu_average))

    # Aggregate latencies
    with open('%s/cpu-vs-latencies.out' % output_dir, 'w') as f:
        f.write(str(cpu_average))
        f.write(', ')
        f.write(str(usr_cpu))
        f.write(', ')
        f.write(str(sys_cpu))
        f.write(', ')

        f.write(str(avg(avg_latencies)))
        f.write(', ')
        f.write(str(avg(last_percentiles)))
        f.write('\n')


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
    if type != 'redis':
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

    args = parser.parse_args()
    server_conf = parse_config(args.server_conf)
    memtier_conf = parse_config(args.memtier_conf)
    run(args.type, server_conf, memtier_conf, args.output)

if __name__ == "__main__":
    main(sys.argv)