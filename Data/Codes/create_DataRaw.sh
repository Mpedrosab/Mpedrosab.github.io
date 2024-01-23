#bin/bash
for folder in * ; do mkdir -p $folder/DataRaw; done
for folder in * ; do cd $folder; mv *.xps DataRaw/ ;cd ..; done