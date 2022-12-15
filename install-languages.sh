#!/bin/bash

array=(rus)
for i in "${array[@]}"
do
  echo "Downloading ${i}.traineddata"
  wget -qO ${i}.traineddata https://github.com/tesseract-ocr/tessdata_best/blob/main/${i}.traineddata?raw=true
done
echo "Done"