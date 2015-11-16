__author__ = 'easy'

class CPUParser(object):

    def __init__(self, content):
        self.content = content

    def get_average(self):
#         0:50:23     CPU    %usr   %nice    %sys %iowait    %irq   %soft  %steal  %guest   %idle
# 10:50:23     all    0.08    0.01    0.27    0.00    0.00    0.13    0.00    0.00   99.52
        last = self.content[-1]
        tokens = last.split()
        usr = float(tokens[2])
        sys = float(tokens[4])
        total = 100 - float(tokens[-1])
        return (total, usr, sys)