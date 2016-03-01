import pssh
import settings
from parsers.config import MemtierConfigParser


class Client(object):

    MEMTIER_CMD = 'ulimit -n 65555; %s %s' % (settings.MEMTIER, '%s')
    MEMTIER_ZIPF_CMD = 'ulimit -n 65555; %s %s' % (settings.MEMTIER_ZIPF, '%s')

    def __init__(self, cache_type):
        self.cache_type = cache_type
        self.hosts = settings.CLIENTS
        self.connections = self._make_connections()

    def _make_connections(self):
        return pssh.ParallelSSHClient(self.hosts)

    def execute(self, command):
        print("[Client] Running command '%s'" % command)
        return self.connections.run_command(command)

    def run_memtier(self, config, zipf=False):
        cmd = self.MEMTIER_CMD if not zipf else self.MEMTIER_ZIPF_CMD
        results = self.execute(cmd % config)
        self.connections.pool.join()
        return results


class Clients(object):

    def __init__(self, cache_type, config, base_port, instances=1, zipf=False):
        self.instances = instances
        self.base_port = base_port
        self.cache_type = cache_type
        self.config = config
        self.zipf = zipf

        self.clients = self._make_connections()

    def generate_configs(self, zipf=False):
        configs = []
        for i in range(self.instances):
            parser = MemtierConfigParser(self.config)

            max_key = parser.max_key
            step = max_key / 7

            parser.set_port(self.base_port + i)

            if zipf:
                lower = 1
                upper = max(1, step * (i + 1))
                parser.set_key_min(lower)
                parser.set_key_max(upper)


            config = parser.get()
            configs.append(config)

        print('[Clients] Configs: ', configs)
        return configs

    def run_memtier(self, zipf=False):
        configs = self.generate_configs(zipf)
        output = []
        for client, config in zip(self.clients, configs):
            out = client.run_memtier(config, zipf=self.zipf)
            output.append(out)

        return output

    def _make_connections(self):
        return [Client(self.cache_type) for i in range(self.instances)]