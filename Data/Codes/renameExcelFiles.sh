#!/bin/bash
myFiles="MemF1D_W0209"
for f2 in "${myFiles}"*;
do 
echo "${f2}"
for f in "${f2}/DataRaw/"*;
do
echo $f
if [[ $f == *".xls"* ]]; then
  echo "It's there! ${f}"
  #echo "Hola"

  mv $f "${f/File/${f2}}"
fi
done
echo "No excel there ${f2} of ${f}"
done