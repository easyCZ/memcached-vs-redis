__author__ = 'easy'

class CPUParser(object):

    def __init__(self, content):
        self.content = content

    def get_average(self):
        last = self.content[-1]
        tokens = last.split()
        return 100 - float(tokens[-1])