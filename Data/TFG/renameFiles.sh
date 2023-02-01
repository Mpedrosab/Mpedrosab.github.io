#!/bin/bash
for f in *
do 
if [[ $f == *".xls"* ]]; then
  echo "It's there!"
  mkdir "${f/.xls/}"
  mv $f "${f/.xls/}/${f/.xls/_IMG.xlsx}"
fi
	echo $f
done