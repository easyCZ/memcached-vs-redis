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

    def get_instance_totals(self, rows):
        return self.get_instance_averages(rows)[-1]

    def get_averages(self, content=None):
        if content is None: content = self.content

        averages = {}
        for hostname, results in content.iteritems():
            matrix = [self.get_instance_totals(rows) for rows in results]
            print(matrix)
            averages[hostname] = self._average_matrix(matrix)

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

    def _average_matrix(self, matrix):
        """
        [
            ([
                779.42999999999995,
                0.0,
                0.0,
                0.11799999999999999,
                60.039999999999999
            ], [
                7793.9700000000003,
                19.77,
                7774.1999999999998,
                0.112,
                296.0
            ], [
                8573.3999999999996,
                19.77,
                7774.1999999999998,
                0.113,
                356.04000000000002
            ]),
            ([
            819.10000000000002, 0.0, 0.0, 0.112, 63.100000000000001], [8190.8100000000004, 20.170000000000002, 8170.6499999999996, 0.107, 311.06999999999999], [9009.9099999999999, 20.170000000000002, 8170.6499999999996, 0.107, 374.17000000000002]), ([773.10000000000002, 0.0, 0.0, 0.11899999999999999, 59.560000000000002], [7730.6400000000003, 18.73, 7711.9099999999999, 0.113, 293.58999999999997], [8503.7399999999998, 18.73, 7711.9099999999999, 0.114, 353.14999999999998]), ([744.0, 0.0, 0.0, 0.123, 57.310000000000002], [7439.9499999999998, 18.100000000000001, 7421.8500000000004, 0.11799999999999999, 282.55000000000001], [8183.9499999999998, 18.100000000000001, 7421.8500000000004, 0.11799999999999999, 339.87])]
        """
        rows = len(matrix)
        cols = len(matrix[0])

        results = []
        for col in range(cols):
            average = sum([matrix[row][col] for row in range(rows)]) / rows
            results.append(average)

        return tuple(results)









