__author__ = 'easy'

class CPUParser(object):

    def get_labels(self):
        return ('usr', 'nice', 'sys', 'iowait', 'irq', 'soft', 'steal', 'guest', 'idle')

    def get_stats(self, output):
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
        # TODO
        pass

    def get_average_stats(self, output):
        for hostname, output in output.iteritems():
            # average is the last line
            average_line = [line for line in output['stdout']][-1]
            instance_averages = self._parse_average_row(average_line)

            return dict(zip(self.get_labels(), instance_averages))


    def _parse_average_row(self, input):
        tokens = input.split()[2:]
        return [float(token) for token in tokens]

    def get_irq(self, averages):
        return averages['irq']
