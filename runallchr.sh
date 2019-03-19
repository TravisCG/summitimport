#1/bin/bash

count=0
for i in 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 X Y MT
do
   echo $i
   count=`expr $count + 1`
   python3 summit2.py $i ../tables_txt/peak.tsv ../tables_txt/experiment.tsv ../tables_txt/tmp1.tsv >../tables_txt/summit.chr${i}.tsv &

   if [ $count = 4 ]
   then
      wait
      count=0
   fi
done

echo "Done."
