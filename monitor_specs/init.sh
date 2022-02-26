#!/bin/bash

sudo echo "Starting..."
yes | sudo apt-get update
yes | sudo apt-get install python3-tk hwinfo
yes | sudo apt-get install xvfb libfontconfig wkhtmltopdf
