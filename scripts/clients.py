import pssh
import settings


class Clients(object):

    def __init__(self, cache_type):
        self.cache_type = cache_type
        self.connections = pssh.ParallelSSHClient(settings.CLIENTS)

    def get_command(self):
        return '%s' % settings.MEMTIER