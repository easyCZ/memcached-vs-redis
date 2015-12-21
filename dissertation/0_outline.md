1. Abstract
2. Introduction
    * Motivation
    * Current State
    * Prior Work
    * Expectation

3. Object Caches
    * Purpose
    * Desired qualities
    * Design & Implementations
    * Performance measurements and methodology
    * Current State of caches & Usage in industry

4. Testing Methodology
    * Quality of Service (99th < 1ms?)
    * Testing setup
    * Comparison to testbeds in other papers
    * Memtier & comparison to others
    * Justify Memtier
    * Open loop vs closed loop
    * What are we interested in
    * Discuss error conditions and repeatability

5 Memcached
    * Outline
    * Implementation and implications


5.1 Memcached Throughput under QoS
    * Latency vs Throughput
    * CPU vs QoS

5.2 Memcached thread scalability
    * # of threads vs QoS
    * Thread pinning
    * Rx/Tx queues

