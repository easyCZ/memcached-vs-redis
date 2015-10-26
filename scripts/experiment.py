from pssh import ParallelSSHClient

hosts = ['nsl200', 'nsl201', 'nsl202', 'nsl203', 'nsl204', 'nsl205', 'nsl206', 'nsl207']

client = ParallelSSHClient(hosts)

output = client.run_command('ls -ltr')
print output