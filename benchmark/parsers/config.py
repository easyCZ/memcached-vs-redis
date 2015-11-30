import settings


class ConfigParser(object):

    def __init__(self, config, type):
        self.config = config
        self.config_tokens = config.split()
        self.type = type

    def _get_port_arg(self):
        return '--port' if self.type == settings.CACHES['redis'] else '-p'

    def _get_port_index(self):
        flag = self._get_port_arg()
        return self.config_tokens.index(flag) + 1

    def get_port(self):
        return int(self.config_tokens[self._get_port_index()])

    def set_port(self, port=11120):
        flag = self._get_port_arg()
        tokens = list(self.config_tokens) # need to copy
        tokens[self._get_port_index()] = port
        return ' '.join(map(str, tokens))

