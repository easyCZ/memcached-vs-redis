DIR=$@

echo "ops/s, hits/s, miss/s, latency, KB/s" > $DIR/totals.csv
for i in {0..120}
do
    sed -n '2p' < $DIR/$i/totals.csv >> $DIR/totals.csv
done

echo "99% latency" > $DIR/99th.csv
for i in {0..120}
do
    sed -n '2p' < $DIR/$i/latency.csv >> $DIR/99th.csv
done

echo "usr, nice, sys, iowait, irq, soft, steal, guest, idle" > $DIR/cpu.csv
for i in {0..120}
do
    sed -n '2p' < $DIR/$i/cpu.csv >> $DIR/cpu.csv
done

paste -d "," $DIR/totals.csv $DIR/99th.csv $DIR/cpu.csv > $DIR/all.csv
