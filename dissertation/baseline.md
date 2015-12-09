# Establishing memcached baseline

## Introduction
In order to be able to effectively study the performance of Memcached and Redis, it is essential to establish a baseline performance. Firstly the focus is on establishing level of throughput with mean latency of 1ms on a basic configuration of the cache. Secondly, scaling of memcached in terms of threads and processes is presented. Finally, the baseline performance is compared to previous research in the area.

## Methodology

### Hosts
Benchmarks are run on 8 machines with the following configuration: 6 core Intel(R) Xeon(R) CPU E5-2603 v3 @ 1.60GHz, 8 GB RAM and 1Gb/s NIC.

### Network
The network topology is a star with one host acting as cache server with the remaining seven machines acting as clients generating load on the cache server.

### Benchmark executiong
Benchmark execution is performed as a parallel SSH into the hosts in question and executing Memtier benchmark. Results are collected and aggregated.


## Single instance baseline
To establish a single cache instance baseline, benchmarks of increasing load in terms of the number of requests are used to determine the maximum throughput a single instance is able to cope with.

### Configuration
The memcached server is configured with the following parameters, other parameters are left in default settings:
* Memory usage: 6GB
* Number of threads: 4 (default)

The clients use the following configuration (rest in default configuration):
* Number of connections: *n*
* Number of threads per connection: 4
* Memcached binary protocol: true
* Generate random data
* Key range: 100 - 10000 (min - max)

where *n* is being varied from 1 to 40 with linear increments of 1.

### Latency vs Throughput
![SingleInstance](./single-instance-baseline.png)

From the figure above, we can see that as we increase the load on the server, the mean latency increases steadily until we get close to 400 000 operations and start seeing a sharp increase in mean latency without significant improvement in throughput. This is the saturation point at which the cache latency stops scaling linearly with load.

The highest throughput occurs with mean latency of 0.668ms at 474936 operations per second. This corresponds to a configuration of 17 conncetions at 4 threads each per each load generating host. This gives a total of 476 simultaneous connections.

The mean throughput below 1ms is 404391 operations per second with a mean latency of 0.563ms.

Moving forward, we can use 16 connections with 4 threads each as a reasonable baseline.



