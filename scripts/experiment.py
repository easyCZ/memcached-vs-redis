from pssh import ParallelSSHClient

hosts = ['nsl200', 'nsl201', 'nsl202', 'nsl203', 'nsl204', 'nsl205', 'nsl206', 'nsl207']

client = ParallelSSHClient(hosts)
client.enable_host_logger()

output = client.run_command('ls -ltr')


for host in output:
    for line in output[host]['stdout']:
        print "Host %s - output: %s" % (host, line)