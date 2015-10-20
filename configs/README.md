## General

### Memory Allocation
*nsl200* has about 6GB free memory out of 8GB - set this as the bound. This achieves about 80% memory usage.

### Deamon Mode
Run both applications as deamons

### Number of Threads
Server has 6 cores


## Redis

### Disable redis saving
To bring redis closer to memcached, disable saving of the content

### Receive Packet Steering (RPS)
[tuning](https://access.redhat.com/documentation/en-US/Red_Hat_Enterprise_Linux/6/html/Performance_Tuning_Guide/network-rps.html)
RPS should be enabled to allow interrupts to be processed by other processes due to Redis being single threaded.

### Kernel Network Tuning
```
vm.swappiness=0                       # turn off swapping
net.ipv4.tcp_sack=1                   # enable selective acknowledgements
net.ipv4.tcp_timestamps=1             # needed for selective acknowledgements
net.ipv4.tcp_window_scaling=1         # scale the network window
net.ipv4.tcp_congestion_control=cubic # better congestion algorythm
net.ipv4.tcp_syncookies=1             # enable syn cookied
net.ipv4.tcp_tw_recycle=1             # recycle sockets quickly
net.ipv4.tcp_max_syn_backlog=NUMBER   # backlog setting
net.core.somaxconn=NUMBER             # up the number of connections per port
net.core.rmem_max=NUMBER              # up the receive buffer size
net.core.wmem_max=NUMBER              # up the buffer size for all connections
```
[ref](http://shokunin.co/blog/2014/11/11/operational_redis.html)