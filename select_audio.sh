#!/bin/bash

#first run ffmpeg -i $1 to determine the audio streams. The command below will select the 0:3 audio stream

INPUT_FILE=$1

echo $INPUT_FILE
command=$(ffmpeg -i "$INPUT_FILE" 2>&1 | /home/bfincher/select_audio/select_audio.py)

if [ $? -eq 0 ]; then
    echo "command = $command"
    extension="${INPUT_FILE##*.}"

    outFile="tmp.${extension}"
    echo "outFile = $outFile"
    ffmpeg -i "$INPUT_FILE" $command $outFile

    #ffmpeg -i $1 -map 0:0 -map 0:3 -c:v copy -c:a:3 libmp3lame -b:a:0 128k -strict -2 tmp.m4v
    mv "$1" "${1}.bak"
    mv "${outFile}" "$1"
else
    echo "command = $command"
    exit -1
fi
   
