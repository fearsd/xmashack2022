#!/bin/bash

# array=(rus)
# for i in "${array[@]}"
# do
echo "Downloading rus.traineddata"
wget -qO rus.traineddata https://github.com/tesseract-ocr/tessdata_best/blob/main/rus.traineddata?raw=true
# done
# echo "Done"