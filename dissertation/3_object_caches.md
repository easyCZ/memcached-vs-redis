# Memory Object Caches

In the traditional sense of way, a cache is a data structure which stores the results of a computation for later retrieval. Generally, a result of a computation is stored against a *key* with a *value* representing the computed result. When retrieving data from the cache, we say there is a *hit* if the key can be found in the cache and a *miss* otherwise. Caching is widely used across the hardware and software stack. For example, modern processors utilize a CPU cache to increase the speed of memory lookup. Similarly, a cache can also be found inside a web server to speed up retrieval of results from the server.

An object cache is a general purpose cache, generally designed as a standalone application, which provides an interface to cache any type of object - for example, an object cache can store large text documents, small tweets or binary data such as images.

A memory object cache is an object with additioanal restriction where data is only stored in the available (or assigned) RAM of the computer. This restriction is important as storing data on hardware slower than RAM would incure too high of a latency and would degrade quality of service.

Both Memcached and Redis are open-source implementations of memory object caches.