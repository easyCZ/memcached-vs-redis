__author__ = 'easy'

class CPUParser(object):

    def __init__(self, content):
        """
        content is a generator
        """
        self.content = content

    def get_labels(self):
        return ('usr', 'nice', 'sys', 'iowait', 'irq', 'soft', 'steal', 'guest', 'idle')

    def get_stats(self, output_generators):
        """
        16:03:02     all    1.51    0.00    1.17    0.00    0.00    0.00    0.00    0.00   97.32
        16:03:03     all    0.33    0.00    0.67    0.00    0.00    0.00    0.00    0.00   99.00
        16:03:04     all    0.17    0.00    0.50    0.00    0.00    0.00    0.00    0.00   99.33
        16:03:05     all    0.17    0.00    0.67    0.00    0.00    0.00    0.00    0.00   99.16
        16:03:06     all    0.50    0.00    1.00    0.00    0.00    0.00    0.00    0.00   98.50
        16:03:07     all    0.17    0.00    0.50    0.00    0.00    0.00    0.00    0.00   99.33

        16:03:07     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest   %idle
        16:03:08     all    0.33    0.00    0.50    0.00    0.00    0.00    0.00    0.00   99.16
        Average:     all    0.32    0.00    0.62    0.02    0.00    0.00    0.00    0.00   99.04
        """
        stats = []
        for instance in output_generators:
            # Each instance is a generator
            for hostname, output in instance.iteritems():
                # average is the last line
                average_line = [line for line in output['stdout']][-1]
                instance_averages = self._parse_average_row(average_line)

                stats.append(dict(zip(self.get_labels(), instance_averages)))

        return stats

    def get_average_stats(self, stats):




    def _parse_average_row(self, input):
        """
        Average is the last row of the input
        """
        tokens = input.split()[2:]
        return [float(token) for token in tokens]


    def get_stats(self):



        last = self.content[-1]
        tokens = last.split()
        usr = float(tokens[2])
        sys = float(tokens[4])
        total = 100 - float(tokens[-1])
        return (total, usr, sys)