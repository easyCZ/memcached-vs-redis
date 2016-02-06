import settings


class ServerConfigParser(object):

    def __init__(self, config, type):
        self.config = config
        self.config_tokens = config.split()
        self.type = type

    def _get_port_arg(self):
        return '--port' if self.type == 'redis' else '-p'

    def _get_port_index(self):
        flag = self._get_port_arg()
        print('flag', flag)
        return self.config_tokens.index(flag) + 1

    def get_port(self):
        return int(self.config_tokens[self._get_port_index()])

    def set_port(self, port=11120):
        flag = self._get_port_arg()
        tokens = list(self.config_tokens) # need to copy
        tokens[self._get_port_index()] = port
        return ' '.join(map(str, tokens))


class MemtierConfigParser(object):

    def __init__(self, config):
        self.config = config
        self.config_tokens = config.split()

    def _get_port_index(self):
        return 1 + self.config_tokens.index('-p')

    def get_port(self):
        return self.config_tokens[self._get_port_index()]

    def set_port(self, port):
        tokens = list(self.config_tokens)
        tokens[self._get_port_index()] = port
        return ' '.join(map(str, tokens))
