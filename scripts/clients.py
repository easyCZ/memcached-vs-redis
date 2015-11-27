import pssh
import settings


class Clients(object):

    def __init__(self, cache_type, config, server_count):
        self.cache_type = cache_type
        self.config = config
        self.connections = pssh.ParallelSSHClient(settings.CLIENTS)

    def get_command(self):
        return '%s %s' % (settings.MEMTIER, self.config)

    def run(self):
        command = self.get_command()
        print("[Clients] Running command '%s'" % command)

        results = self.connections.run_command(command)
        print("[Clients] Waiting for results to finish...")
        self.connections.pool.join()

        print("[Clients] Results completed.")
        return results