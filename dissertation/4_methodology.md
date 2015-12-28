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
Firstly, it is important to define an acceptale quality of service (QoS) for an object cache in question. Distributed systems are increasingly more popular with responses to requests being a composition of smaller responses from respective sub-systems. Given all sub-systems must return a response before the complete response is serviced to the requestor, the slowest of all smaller responses will determine the overall response time. Frequently, the QoS aimed for is sub-1ms latency. Similar target is used by Leverich and Kozyrakis [1]. Therefore, in this study the aim will be to achieve latency under 1ms in 99% of cases.



[1] Reconciling High Server Utilization
and Sub-millisecond Quality-of-Service