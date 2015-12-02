from clients import Clients
from parsers.memtier import MemtierResultsParser
from server import Server

s = Server('memcached', '-d -p 11120 -m 1024', 11120, 4)
s.start_cache()

c = Clients('memcached', '-s nsl200 -p 11123 --test-time=30 -c 1 -t 1 -P memcache_binary', 11120, 4)
results = c.run_memtier()

parser = MemtierResultsParser(results)
parser.read()
averages = parser.get_averaged_totals()
average_99th = parser.get_average_99th()