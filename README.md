# ReUse

## monitor_specs
Contains the GUI.py file that is designed to automate monitor information gathering.

## os_install
Contains the os_clone BASH script used for writing OSs to hard drives.
ISO files can be found [here](https://drive.google.com/drive/folders/18ejyXTB1vsjlzQfxChp4izIAkGgJYXoE?usp=sharing).

![image](https://user-images.githubusercontent.com/43316251/162587454-0e244102-0a49-49b6-9daf-89cb994373fc.png)

This program will check for images in the _os_install/iso/_ directory. Each image is composed of a base folder that needs to have a executable of the same name and optionally a conf file also with the folder's name to give a discription. Folder _/foo/_ will have the executable _/foo/foo_, but many images will often have _/foo/foo.conf_ and sometimes a _/foo/bar.iso_ if desired. 

The job of the executable is to completely handle the disk operations, being passed two peramiters, The first peramiter is the name of the device in /dev/ and the second is the path to _/foo/foo.iso_. _(Note: this arguemnt can be ignored)._

The .conf file should contain one line of text. That line will be displayed in the GUI.


## pc_specs
Under development, but will contain a program for gathering the specs of computer hardware.

# License
gpl-3.0
