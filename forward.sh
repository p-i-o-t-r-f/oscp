#for name in $(cat list.txt);do
#host $name.patagonia.com|grep "has address" | cut -d " " -f1,4
#done
for name in $(cat names.txt) ;do
    host $name.megacorpone.com|grep "has address" | cut -d " " -f1,4
done

