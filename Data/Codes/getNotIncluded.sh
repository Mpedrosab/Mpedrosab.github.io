#!/bin/bash

path="../Data/"
echo "" > ${path}notIncluded.txt

for f in $( ls ${path}* )
do

echo "File ${f}"
isthere=$(grep -c f "${path}DataDB.json")

if [[ $isthere != 0 ]]
then
echo $f >> ${path}notIncluded.txt
fi
done

