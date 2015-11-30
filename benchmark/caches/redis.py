import pssh
from benchmark.server import  Server
from benchmark import settings


class Redis(Server):

    GREP_CMD = "ps -ef | grep '[R]edis'"
    KILL_CMD = "kill %s"

    def __init__(self, server_conf, instances=1):
        self.host = settings.SERVERS
        self.instances = instances
        self.server_conf = server_conf

        self.connections = self._make_connection()

    def _make_connection(self):
        return [pssh.ParallelSSHClient(self.host)]

    def run(self, command):
        print("[Redis] Executing command '%s'" % command)
        return [instance.run_command(command) for instance in self.connections]

    def kill(self):
        instance = self.connections[0]
        command_out = instance.run_command(self.GREP_CMD)
        for hostname, res in command_out.iteritems():
            for pid in res['stdout']:
                tokens = pid.split()
                print("[Server] Running 'kill %s'" % tokens[1])
                instance.run_command(self.KILL_CMD % tokens[1])

