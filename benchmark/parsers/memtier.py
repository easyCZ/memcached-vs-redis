from collections import defaultdict

class MemtierResultsParser(object):

    def __init__(self, generators):
        self.generators = generators

    def _get_stdout(self, generator):
        output = {}
        for hostname, out in generator.iteritems():
            output[hostname] = [line for line in out['stdout']]
        return output

    def read(self):
        results = [self._get_stdout(generator) for generator in self.generators]

        # group by hostname
        grouped = defaultdict(list)
        for result in results:
            for hostname, output in result.iteritems():
                grouped[hostname].append(output)

        return grouped



