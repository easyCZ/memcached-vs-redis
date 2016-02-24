import pssh
import settings
from parsers.config import MemtierConfigParser


class Client(object):

    MEMTIER_CMD = 'ulimit -n 65555; %s %s' % (settings.MEMTIER, '%s')

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
        results = self.execute(self.MEMTIER_CMD % config)
        self.connections.pool.join()
        return results


class Clients(object):

    def __init__(self, cache_type, config, base_port, instances=1):
        self.instances = instances
        self.base_port = base_port
        self.cache_type = cache_type
        self.config = config

        self.clients = self._make_connections()

    def generate_configs(self, zipf=False):
        step = 10000 / 7

        configs = []
        for i in range(self.instances):
            parser = MemtierConfigParser(self.config)

            parser.set_port(self.base_port + i)

            if zipf:
                lower = max(1, step * i)
                upper = max(1, step * (i + 1))
                parser.set_key_min(lower)
                parser.set_key_max(upper)


            config = parser.get()
            configs.append(config)
        return configs

    def run_memtier(self, zipf=False):
        configs = self.generate_configs(zipf)
        output = []
        for client, config in zip(self.clients, configs):
            out = client.run_memtier(config)
            output.append(out)

        return output

    def _make_connections(self):
        return [Client(self.cache_type) for i in range(self.instances)]