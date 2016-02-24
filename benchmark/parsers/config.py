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

        index = self._get_key_index('--key-maximum=')
        token = self.config_tokens[index]
        key, value = token.split('=')
        self.max_key = value

    def _get_port_index(self):
        return 1 + self.config_tokens.index('-p')

    def _get_key_index(self, key):
        for (i, token) in enumerate(self.config_tokens):
            if str(token).startswith(key):
                return i

    def get_port(self):
        return self.config_tokens[self._get_port_index()]

    def set_port(self, port):
        tokens = list(self.config_tokens)
        index = self._get_port_index()
        tokens[index] = port
        self.config_tokens[index] = port
        return ' '.join(map(str, tokens))


    def _set_key(self, key, key_value):
        tokens = list(self.config_tokens)
        index = self._get_key_index(key)
        token = tokens[index]
        key, value = token.split('=')
        value = key_value

        self.config_tokens[index] = '='.join([str(key), str(value)])

    def set_key_min(self, key_min):
        return self._set_key('--key-minimum=', key_min)

    def set_key_max(self, key_max):
        return self._set_key('--key-maximum=', key_max)

    def get(self):
        return ' '.join(map(str, self.config_tokens))