#!/bin/bash

input="remote_update/data.txt"
while IFS= read -r i
do
  echo "$i"
  remote-viewer vnc://192.168.1.$i:590$i
done < "$input"
