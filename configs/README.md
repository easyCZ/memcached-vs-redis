## General

### Memory Allocation
*nsl200* has about 6GB free memory - set this as the bound

### Deamon Mode
Run both applications as deamons

### Number of Threads
Server has 6 cores


## Redis

### Receive Packet Steering (RPS)
[tuning](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Performance_Tuning_Guide/network-rps.html)
RPS should be enabled to allow interrupts to be processed by other processes due to Redis being single threaded.

