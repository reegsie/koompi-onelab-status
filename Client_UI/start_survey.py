#!/usr/bin/python 

import os
import time

start_id = [4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,26,27,28,29,30,31,32,33,34,35,36,37,38,39]

for i in start_id: 

    os.system("ssh admin@192.168.1.{} 'export DISPLAY=:0 && python /home/admin/client-onelab/upload_image.py && break'".format(i))    
    print ('done {}'.format(i))
    time.sleep(1)
    continue 
