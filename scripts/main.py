from server import Server


def main():
    server = Server('memcached')
    server.run()
#
# # Start cache
# server_ssh = pssh.ParallelSSHClient(settings.SERVERS)
# server_ssh.run_command('')
#
#
#
#
# client = pssh.ParallelSSHClient(hosts)
# pssh.utils.enable_host_logger()
#
# output = client.run_command('ls -ltr')
#
#
# # for host in output:
# #     for line in output[host]['stdout']:
# #         print "Host %s - output: %s" % (host, line)

main()