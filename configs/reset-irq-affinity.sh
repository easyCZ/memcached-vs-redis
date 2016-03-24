for i in $(seq 81 1 87); do
    echo 0-5 | sudo tee /proc/irq/$i/smp_affinity_list;
done
