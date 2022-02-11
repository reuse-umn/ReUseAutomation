#!/bin/bash

clear
lsblk | grep "^[^loop]"
read -p 'Device: ' DEV
if [ $DEV = "sda" ]
then
	echo "Bad move"
	exit 1	
fi
clear

sudo umount /dev/"$DEV"* &> /dev/null
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"
sudo dd if="$DIR"/MBR.iso of=/dev/"$DEV" bs=10M count=1000 status=progress

(echo d; echo n; echo p; echo 1; echo ""; echo ""; echo "n"; echo w;) | sudo fdisk /dev/"$DEV"

sudo e2fsck -f /dev/$"$DEV"1
sudo resize2fs /dev/$"$DEV"1

echo "END"
