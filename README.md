# ReUse IT Automation Scripts

## [```monitor_specs```](./monitor_specs)
Contains the GUI.py file that is designed to automate monitor information gathering.

### Usage
1. Run the [```reuse_monitor_spec```](./reuse_monitor_spec) script. *Note: This is the same as (```monitor_specs/GUI.py```)[./monitor_specs/GUI.py].*
2. Use the *Refresh* button to update the current monitor information. 
3. Update any incorrect or missing information, then click *Add* to add the monitor to the list.
4. Repeat steps 2 and 3 until all monitors have been added. *Note: The current list of monitors can be viewed from the terminal.*
5. Click the *Print* button to print the list of monitors to the printer. This will empty the list of monitors.

The *(Remove)* button can be used to remove a monitor from the list. This is useful if a monitor is added by mistake.
The *(Reprint)* button can be used to reprint the list of monitors. This is useful if the printer jams or the printout is lost.

### Installation
To setup the program, run the [```/monitor_specs/init.sh```](./monitor_specs/init.sh) script. This will install the required packages and initialize the configuration files. 

There are two configurtion files:
1. *Monitor Allowlist* - This file contains a list of any monitors that should not be detected by the program. This is useful for preventing the program from detecting the computers's own monitors. 
2. *Printer Name* - This file contains the name of the printer that the program should print to. 

## (```os_install```)[./os_install]
Contains the os_clone BASH script used for writing OSs to hard drives.
ISO files can be found [here](https://drive.google.com/drive/folders/18ejyXTB1vsjlzQfxChp4izIAkGgJYXoE?usp=sharing).

![image](https://user-images.githubusercontent.com/43316251/162587454-0e244102-0a49-49b6-9daf-89cb994373fc.png)

This program will check for images in the _os_install/iso/_ directory. Each image is composed of a base folder that needs to have a executable of the same name and optionally a conf file also with the folder's name to give a discription. Folder _/foo/_ will have the executable _/foo/foo_, but many images will often have _/foo/foo.conf_ and sometimes a _/foo/bar.iso_ if desired. 

The job of the executable is to completely handle the disk operations, being passed two peramiters, The first peramiter is the name of the device in /dev/ and the second is the path to _/foo/foo.iso_. _(Note: this arguemnt can be ignored)._

The .conf file should contain one line of text. That line will be displayed in the GUI.



## GreaseMonkey
### Usage
Script used to interface with the TDX asset modification form:
- F1 Sets the form to have the asset repaired.
- F2 Sets the form to have the asset recycled.
- F3 Adds the HDD comment with no HDD present.
- F4 Adds the HDD comment with a single HDD.
- F5 Moves the Cursor to the SN entery field. 
- F6 Moves the Cursor to the Name field and pressing tab will move to the ST entery field.
- F12 Submits the form.

This script may provide diffrent values in the text boxes for dropdowns, but the actual values being submitted are correct.

### Installation
1. Install the [GreaseMonkey](https://addons.mozilla.org/en-US/firefox/addon/greasemonkey/) addon for Firefox.
2. Click the GreaseMonkey icon in the top right of the browser and select *Import a Backup.
3. Select the [```/TDX/Greasemonkey/main.zip```](./TDX/Greasemonkey/main.zip) file.

The script should now be installed and ready to use.

*Note: THIS SCRIPT IS NOT GUARANTEED TO WORK ON ANY BROWSER OTHER THAN FIREFOX.*

### Modification
For details on how to modify the script, refer to [this](./TDX/) page.

Refer to the [GreaseMonkey Documentation](https://wiki.greasespot.net/Greasemonkey_Manual:API) for more information on how to modify the script.

## License
gpl-3.0
