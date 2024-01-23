#!/bin/bash
path="/mnt/d/Documentos_D/Google_Drive_UGR/Data_analysis/Data/"
fileSave="${path}queryComments.sql"
rm $fileSave

beginString='SELECT Name,ExpDate, Comments from "'
endString='".LBExp'

echo "" > $fileSave

for f in "${path}"*
do
#echo $f
for f2 in "${f}/DataRaw/"*
do
#echo $f2
#echo "${path}${f}/DataRaw/${f2}"
if [[ $f2 == *"abs"* ]]
then
#echo "YESSSS"
echo "${beginString}${f2}${endString}" >> $fileSave
echo  "UNION ALL" >> $fileSave
fi
done
done
#echo  "SORT BY ExpDate" >> $fileSave
sed -i "s/\/mnt\/d/D:/" ${fileSave}

echo "ALL SAVED TO ${fileSave}"