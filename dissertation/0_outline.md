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
    * Define Quality of Service (99th < 1ms?)
    * What are we interested in (in terms of stats)
    * Testing setup
    * Comparison to testbeds in other papers
    * Memtier & comparison to others
    * Memtier
        - Justify why memtier
        - Outline how memtier works
    * Open loop vs closed loop
    * Discuss error conditions and repeatability

5. Memcached
    * Outline
    * Design decisions
        - Multi-threaded
        - Locks
        - Memory allocation
    * Important configuration options and defaults
    * Memcached Throughput under QoS
        - Latency vs Throughput
        - CPU vs QoS
    * Memcached thread scalability
        - # of threads vs QoS
        - Thread pinning
        - Rx/Tx queues

