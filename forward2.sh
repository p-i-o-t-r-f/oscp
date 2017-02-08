for ip1 in $(seq 1 254);do
 for ip2 in $(seq 60 70);do
host 50.7.$ip2.$ip1;done |grep -v "not found" 
done
