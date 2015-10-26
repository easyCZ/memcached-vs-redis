import pssh
import settings


class Server(object):

    def __init__(self, cache_type, port=11122):
        self.host = settings.SERVERS
        self.cache_type = cache_type
        self.connection = pssh.ParallelSSHClient(self.host)

    def get_command(self):
        cache = settings.CACHES[self.cache_type]
        config = settings.CACHE_CONFIGS[self.cache_type]
        flags = {
            '-d': ''
        }
        return '%s -d' % cache

    def run(self):
        return self.connection.run_command(self.get_command())

    def kill(self):
        command = "ps -ef | grep '[%s]%s' | awk '{print $2}'" % (
            self.cache_type[0],
            self.cache_type[1:]
        )
        pid = self.connection.run_command(command)[0]['stdout']
        return self.connection.run_command("kill %s" % pid)


