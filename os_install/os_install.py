#!/usr/bin/env python3

from tkinter import *
from tkinter import ttk
import tkinter as tk
from os_install_helper import *

ROMs=[];
devices=[];

#------------------------------------------------

def refresh(event=None):
    return

def flash(event=None):
    dev=ROMData['DEVICE'].get()
    rom=ROMData['ROM'].get()
    if(len(dev)==0 or len(rom)==0):
        print('ERROR: Empty input')
        return
    path=""
    for ROM in ROMs:
        if(ROM['name']==rom):
            path=ROM['path']+'/'+ROM['name']
    if(len(path)==0):
        print('ERROR: Invalid path')
    os.system(path+' '+dev+' '+path+'.iso')


def refresh_ROM():
    tmp=[]
    for ROM in ROMs:
        tmp.append(ROM['name'])
    ROM_combo['values']=tmp

def refresh_device():
    normal_file=os.path.expanduser("~/.config/ReUseAutomation/os_install/ignore.json")
    devices=get_block_devices(normal_file)
    tmp=[]
    for device in devices:
        tmp.append(device['name'])
    device_combo['values']=tmp


def update_about(event):
    rom=ROMData['ROM'].get()
    for ROM in ROMs:
        if(rom==ROM['name']):
            ROMData['ABOUT'].set(ROM['about'])
    
#------------------------------------------------


def generateGrid(grid, stick): 
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if(grid[i][j]!=None):
                grid[i][j].grid(row=i, column=j, sticky=stick[j])


def generateROMGrid(base):
    grid=[]
    sticky=["NE", "NW"]
    
    global ROM_combo
    ROM_combo= ttk.Combobox(base, textvariable=ROMData['ROM'], values=[], postcommand=refresh_ROM)
    global device_combo
    device_combo=ttk.Combobox(base, textvariable=ROMData['DEVICE'], values=[], postcommand=refresh_device)
    ROM_combo['state']='readonly'
    device_combo['state']='readonly'
    ROM_combo.bind('<<ComboboxSelected>>', update_about)
    grid.append([Label(base, text="Device:"), device_combo]) 
    grid.append([Label(base, text="ROM:"), ROM_combo])
    grid.append([Label(base, text="About:"), Entry(base, textvariable=ROMData["ABOUT"])])
    
    generateGrid(grid, sticky)
    return grid

 
def generateButtonsGrid(base):
    grid=[]

    grid.append([Button(base, text="Flash", command=flash)])
    grid.append([Button(base, text="Refresh", command=refresh)]) 

    generateGrid(grid, ["NSEW"])
    return grid


root=Tk()
#EDIT LATER
ROMs_path='/home/reuse/ReUseAutomation/os_install/iso'
ROMs=get_iso_roms(ROMs_path)
ROMData={
        "DEVICE" : StringVar(),
        "ROM" : StringVar(),
        "ABOUT" : StringVar()}
root.title("OS Flashing")
root.bind("<Control-r>", refresh)
fr_entry=Frame(master=root, width=300)
fr_buttons=Frame(master=root, width=50)
fr_entry.grid(row=0, column=0)
fr_buttons.grid(row=0, column=1)

monitor=generateROMGrid(fr_entry)
generateButtonsGrid(fr_buttons)

refresh()
root.mainloop()
