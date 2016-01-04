# Methodology

* Quality of Service (99th < 1ms?)
* Testing setup
* Comparison to testbeds in other papers
* Memtier & comparison to others
* Justify Memtier
* Open loop vs closed loop
* What are we interested in
* Discuss error conditions and repeatability

## Quality of Service
Firstly, it is important to define an acceptale quality of service (QoS) for an object cache in question. Distributed systems are increasingly more popular with responses to requests being a composition of smaller responses from respective sub-systems. Given all sub-systems must return a response before the complete response is serviced to the requestor, the slowest of all smaller responses will determine the overall response time. Frequently, the QoS aimed for is sub-1ms latency. Similar target is used by Leverich and Kozyrakis [1]. Therefore, in this study the aim will be to achieve tail latency under 1ms, that is in 99% of cases.

## Testing setup
The performance benchmarks are run on 8 machines with the following configuration: 6 core Intel(R) Xeon(R) CPU E5-2603 v3 @ 1.60GHz [2], 8 GB RAM and 1Gb/s Network Interface Controller (NIC).

All the hosts are connected to a Pica8 P-3297 [3] switch with 48 1Gbps ports with a star as the network topology. A single host is used to run an object cache system while the remaining seven are used to generate workloads against the server.

## Workload generation
Workload for the cache server is generated using Memtier Benchmark [4]. The Memtier Benchmark provides a configurable parallel workload generation for both Memcached and Redis. Additionally, it allows for a high level of configrability. 

### Memtier Benchmark Behavior
Memtier Benchmark provides various paramters allowing for a variable configuration. As part of the configration, the user is allowed to specify the number of threads and the number of connections per each thread memtier should make. The standard lifecycle of each thread is as follows:

1. Set up n connection configurations
2. For each connection configuration, initiate the connection over the desired protocol (default: TCP)
3. Make a request
4. Tear down the connection
5. Repeat iterations

## Open loop vs Closed loop
Memtier Benchmark, in its default configuration initiates a connection to the server
For the purposes of this papare, workload generation will focus on a closed loop system. Therefore, the workload generation will not take into consideration the load of the server or the behavior of other clients generating requests. 

* [1] Reconciling High Server Utilization
and Sub-millisecond Quality-of-Service
* [2] [Intel(R) Xeon(R) E5-2603](http://ark.intel.com/products/64592/Intel-Xeon-Processor-E5-2603-10M-Cache-1_80-GHz-6_40-GTs-Intel-QPI)
* [3] [Pica8 Datasheet](http://www.pica8.com/wp-content/uploads/2015/09/pica8-datasheet-48x1gbe-p3297.pdf)
* [4] [Memtier Benchmark](https://github.com/RedisLabs/memtier_benchmark)
