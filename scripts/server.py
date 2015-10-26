import pssh
import settings


class Server():

    def __init__(self, cache_type):
        self.host = settings.SERVERS
        self.cache_type = cache_type

    def get_command(self):
        cache = settings.CACHES[self.cache_type]
        config = settings.CACHE_CONFIGS[self.cache_type]
        flags = {
            '-d': ''
        }
        return '%s' % cache

    def run(self):
        self.server = pssh.ParallelSSHClient(self.host)
        self.server.run_command(self.get_command(), {
            '-d': ''
        })
