ssh nsl200 << 'ENDSSH'

    echo 0-5 | sudo tee /proc/irq/81/smp_affinity_list;

    for i in $(seq 82 1 87); do
        echo $(($i % 6)) | sudo tee /proc/irq/$i/smp_affinity_list;
    done

ENDSSH