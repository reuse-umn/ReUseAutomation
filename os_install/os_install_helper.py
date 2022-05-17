#!/bin/env python3

import os
from os.path import exists
import json

def get_block_devices(normalization):
    os.system('lsblk --json --tree > ./lsblk.tmp')

    f=open('./lsblk.tmp')
    drives=json.load(f)
    f.close()
    
    normal={'blockdevices': []}
    if(exists(normalization)):
        f=open(normalization)
        normal=json.load(f)
        f.close

    
    ret=[]
    for drive in drives['blockdevices']:
        if(drive not in normal['blockdevices']):
            ret.append(drive)
    return ret

def get_iso_roms(iso_dir):
    roms=os.listdir(iso_dir)
    iso_roms=[]
    for romf in roms:
        if(os.path.isdir(os.path.join(iso_dir,romf))):
            iso_roms.append({'path': os.path.join(iso_dir, romf), 'name': romf})
    
    valid_roms=[]
    for rom in iso_roms:
        files=os.listdir(rom['path'])
        
        if(rom['name']+'.conf' in files):
            with open(rom['path']+'/'+rom['name']+'.conf') as namef:
                rom['about']=namef.readline().strip()
        else:
            rom['about']=rom['name']

        if(rom['name'] in files):
            valid_roms.append(rom)
        else:
            print('Missing executable for: '+rom['name'])
    return valid_roms



