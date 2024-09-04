# API Overview

## SETUP
Get the API username, password, and key from Davis. Create a file named **.env** in the file **./TDX/API/dist/TDX** and paste the following text into it, replaceing the bracked sections with the username, password and key.


>API_USER=[Username]<br>
>API_PASS=[Password]<br>
>API_KEY=[Key]<br>
>UPDATE_ENDPOINT=https://umn-prod-apigw.boomi.cloud:8077/prd/ws/rest/ReUsetoTDX/UpdateAsset


## Instructions

Run **TDX.exe** in ***./TDX/API/dist/** to start the program.

A GUI will appear, enter your university internet id to the Operator Section.

To submit an entry select ***Pending Repair*** or ***Pending Disposal***, enter the computer's ***serial number***, and the ***HDD serial number*** if one exists. If there is not a hard drive leave the HDD Serial number section empty. After every relevant feild is filled in press the submit button.

### Hotkeys

>***Pending Repair***: ```F1```<br>
>***Pending Disposal***: ```F2```<br>
>***Submit***: ```Esc```<br>

## Development

### Init
Install Python, set the working directory to the Git repo, then Run:

>python -m venv ./venv<br>
>pip install -r ./TDX/API/requirments.txt

### Export to exe

Run:

>cd ./TDX/API<br>
>pyinstaller -F ./TDX.py

This will create the directories build and dist. The .exe file is in dist.