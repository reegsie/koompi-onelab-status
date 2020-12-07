#!/bin/bash

path=/home/alarm/Documents/projects/Koompi_Stuff/koompi-onelab-status/Master_UI/.services/remote_update/data


read -r line < $path && remote-viewer vnc://192.168.1.$line:5900
