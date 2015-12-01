from collections import defaultdict

class MemtierResultsParser(object):

    TOTALS_DELIM = '------------------------------------------------------------------------'

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

        self.content = grouped
        return grouped

    def get_instance_averages(self, rows):
        totals_index = rows.index(self.TOTALS_DELIM)
        sets = rows[totals_index + 1]
        gets = rows[totals_index + 2]
        totals = rows[totals_index + 3]

        return (
            self._parse_sets(sets),
            self._parse_average_row(gets),
            self._parse_average_row(totals)
        )

    def get_averages(self, content=None):
        if content is None: content = self.content

        averages = {}
        for hostname, results in content.iteritems():
            instance_averages = [self.get_instance_averages(rows) for rows in results]
            N = float(len(instance_averages))
            averages[hostname] = tuple(sum(col)/N for col in zip(*instance_averages))

        return averages

    def get_average_headers(self):
        return ('ops/s', 'hits/s', 'miss/s', 'latency', 'KB/s')

    def _parse_average_row(self, row):
        tokens = row.split()[1:]
        return [float(token) for token in tokens]

    def _parse_sets(self, row):
        tokens = row.split()[1:]
        tokens[1] = 0
        tokens[2] = 0
        return [float(token) for token in tokens]








