#!/bin/bash

sudo echo "Starting..."
echo "Updating software..."
yes | sudo apt-get update
yes | sudo apt-get install python3-tk hwinfo
yes | sudo apt-get install xvfb libfontconfig wkhtmltopdf

clear
printf '_______________________________________________\n'
lpstat -p -d
mkdir -p ~/.config/ReUseAutomation/monitor_specs/
printf '_______________________________________________\n'
read -p "Enter the name of the printer (leave empty to skip): "
if [ ! -z "$REPLY" ] 
then
	echo "$REPLY" > ~/.config/ReUseAutomation/monitor_specs/printer.txt
	echo "Updating printer..."
else 
	echo "Skipping..."
fi

read -p "Update Witelist (leave empty to skip): "
if [ ! -z "$REPLY" ] 
then
	echo "Whitelisting current monitors..."
	python3 ./init.py > ~/.config/ReUseAutomation/monitor_specs/ignore.txt
	python3 ./init.py
else 
	echo "Skipping..."
fi


printf "Done.\n"
