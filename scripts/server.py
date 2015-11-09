import pssh
import settings


class Server(object):

    def __init__(self, cache_type, server_conf):
        self.host = settings.SERVERS
        self.server_conf = server_conf
        self.cache_type = cache_type
        self.connection = pssh.ParallelSSHClient(self.host)

    def get_cpu_command(self):
        return 'mpstat 1 63'

    def get_cache_command(self):
        cache = settings.CACHES[self.cache_type]
        return '%s %s' % (cache, self.server_conf)

    def run(self, command):
        print("[Server] Running command '%s'" % command)
        return self.connection.run_command(command)

    def start(self):
        return self.run(self.get_cache_command())

    def log_cpu(self):
        return self.run(self.get_cpu_command())

    def kill(self):
        command = "ps -ef | grep '[%s]%s' | awk '{print $2}'" % (
            self.cache_type[0],
            self.cache_type[1:]
        )
        command_out = self.connection.run_command(command)
        print("Getting process ID: %s" % command_out)
        pid = command_out[self.host]['stdout']
        print("Attempting to kill process #%s" % pid)
        return self.connection.run_command("kill %s" % pid)


