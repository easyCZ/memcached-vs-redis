
SERVERS = ['nsl200']
CLIENTS = ['nsl201', 'nsl202', 'nsl203', 'nsl204', 'nsl205', 'nsl206', 'nsl207']

CACHES = {
    'memcached': '~/memcached-1.4.24/memcached',
    'redis': '~/redis-stable/src/redis-server ~/redis-stable/redis.conf'
}

CACHE_CONFIGS = {
    'memcached': '~/configs/memcached.conf',
    'redis': '~/configs/redis.conf'
}

MEMTIER = '~/memtier_fork/memtier_benchmark'
MEMTIER_ZIPF = '~/memtier_zipf/memtier_benchmark'