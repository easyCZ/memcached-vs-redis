import pssh
import settings
from parsers.config import MemtierConfigParser


class Client(object):

    MEMTIER_CMD = '%s %s' % (settings.MEMTIER, '%s')

    def __init__(self, cache_type):
        self.cache_type = cache_type
        self.hosts = settings.CLIENTS
        self.connections = self._make_connections()

    def _make_connections(self):
        return pssh.ParallelSSHClient(self.hosts)

    def execute(self, command):
        print("[Client] Running command '%s'" % command)
        return self.connections.run_command(command)

    def run_memtier(self, config):
        return self.execute(self.MEMTIER_CMD % config)
        # self.clients.pool.join()


class Clients(object):

    def __init__(self, cache_type, config, base_port, instances=1):
        self.instances = instances
        self.base_port = base_port
        self.cache_type = cache_type
        self.config = config

        self.clients = self._make_connections()

    def generate_configs(self):
        configs = []
        for i in range(self.instances):
            config = MemtierConfigParser(self.config).set_port(self.base_port + i)
            configs.append(config)
        return configs

    def run_memtier(self):
        configs = self.generate_configs()
        output = []
        for client, config in zip(self.clients, configs):
            out = client.run_memtier(config)
            output.append(out)

        return output

    def _make_connections(self):
        return [Client(self.cache_type) for i in range(self.instances)]