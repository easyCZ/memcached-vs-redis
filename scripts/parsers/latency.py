__author__ = 'easy'

class LatencyParser(object):

    TOTALS_DELIM = '------------------------------------------------------------------------'
    GETS_DELIM = '---'

    def __init__(self, content):
        self.content = content

    def get_average_latency(self):
        first_index = self.content.find(self.TOTALS_DELIM)
        totals = self.content[first_index+3]
        latency = totals.split()[4]
        return latency

    def get_99th_latency(self):
        gets_start = self.content.find(self.GETS_DELIM)
        gets = self.content[gets_start+1:]

        for get in gets:
            # return first item past 99
            method, msec, percent = get.split()
            percent = float(percent)

            if percent >= 99.0:
                return float(msec)

        return 100.0
