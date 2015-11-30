import pssh
import settings


class Server(object):

    MPSTAT_CMD = 'mpstat 1 23'
    ULIMIT_CMD = 'ulimit -n 65535'

    def __init__(self, cache_type, server_conf, instances=1):
        self.instances = instances
        self.host = settings.SERVERS
        self.server_conf = server_conf
        self.cache_type = cache_type
        self.connections = self._make_connections()

    def _make_connections(self):
        return [pssh.ParallelSSHClient(self.host) for i in range(self.instances)]

    def execute(self, command):
        print("[Server] Running command '%s'" % command)
        return [instance.run_command(command) for instance in self.connections]

    def kill(self, pid):
        return self.execute('kill %s' % (str(pid)))

    def kill_cache(self):
        ps_grep = "ps -ef | grep '[%s]%s'" % (
            self.cache_type[0],
            self.cache_type[1:]
        )
        ps_grep_out = self.connections[0].run_command(ps_grep)

        killed_pids = []
        for hostname, res in ps_grep_out.iteritems():
            for processes in res['stdout']:
                pid = processes.split()[1]
                self.kill(pid)
                killed_pids.append(pid)

        print('[Server] Killed %s' % ', '.join(killed_pids))


    def start_cache(self):
        command = '%s; %s %s' % (
            self.ULIMIT_CMD,
            settings.CACHES[self.cache_type],
            self.server_conf
        )
        return self.execute(command)

    def log_cpu(self):
        return self.execute(self.MPSTAT_CMD)
