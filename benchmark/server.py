import pssh
import settings
from parsers.config import ServerConfigParser


class Server(object):

    MPSTAT_CMD = 'mpstat 1 %d'
    ULIMIT_CMD = 'ulimit -n 65535'

    def __init__(self, cache_type, server_conf, base_port, instances=1):
        self.instances = instances
        self.port = base_port
        self.host = settings.SERVERS
        self.server_conf = server_conf
        self.cache_type = cache_type
        self.connections = self._make_connections()

    def _get_port(self, config):
        tokens = config.split()
        return tokens[tokens.index()]

    def _make_connections(self):
        return [pssh.ParallelSSHClient(self.host) for i in range(self.instances)]

    def execute(self, command):
        print("[Server] Running command '%s'" % command)
        return [instance.run_command(command) for instance in self.connections]

    def execute_single(self, command):
        print("[Server] Running command '%s'" % command)
        return self.connections[0].run_command(command)

    def kill(self, pid):
        return self.execute_single('kill %s' % (str(pid)))

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
        # Generate unique configs for each instance
        configs = []
        for port_offset in range(self.instances):
            parser = ServerConfigParser(self.server_conf, self.cache_type)
            config = parser.set_port(self.port + port_offset)
            configs.append(config)

        base_command = '%s; %s %s; %s' % (self.ULIMIT_CMD, settings.CACHES[self.cache_type], '%s')
        commands = [base_command % config for config in configs]

        return [self.execute_single(command) for command in commands]

    def pin(self):
        command = 'memcached_pid=($(ps -ef | grep [m]emcached | awk \'{ print $2 }\')); memcached_tids=$(ps -p $memcached_pid -o tid= -L | sort -n | tail -n +2 | head -n -1); for i in {0..5}; do taskset -pc $i ${myarr[$i]} ; done'
        return self.execute_single(command)

    def log_cpu(self, duration=30):
        return self.execute_single(self.MPSTAT_CMD % duration)
