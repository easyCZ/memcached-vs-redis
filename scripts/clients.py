import pssh
import settings


class Clients(object):

    def __init__(self, cache_type, config):
        self.cache_type = cache_type
        self.config = config
        self.connections = pssh.ParallelSSHClient(settings.CLIENTS)

    def get_command(self):
        return '%s %s' % (settings.MEMTIER, self.config)

    def run(self):
        return self.connections.exec_command(self.get_command())