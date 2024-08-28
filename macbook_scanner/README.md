# Settup for Google Vision macbook sn scanner

## Init

Install libraries from requirments.txt, then follow the "Local development environment" section of this [Guide](https://cloud.google.com/docs/authentication/provide-credentials-adc).

This in neccecary for the google vision API to operate correctly.

## Operation

Set up a document camera and plug it in to the computer. Set the camera_ind variable to the total number of cameras connected - 1, e.g. if there is one camera connected set it to 0. Run scan_sn.py, and line up the macbook serial number with the camera and zoom in as much as possible. press ```F1``` to start a video feed from the camera and ```F1``` again to select a frame. The serial number will be autmatically added to the entry box below the picture, and will also to your clipboard.