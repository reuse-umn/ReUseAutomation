# TDX JavaScript Modification

## Overview
This page will explain how to modify the JavaScript used by TDX to add new features or fix bugs.

GreaseMonkey works by injecting JavaScript into the page. This JavaScript can be used to preform any arbitrary actions on the page. This is useful for automating tasks that are commonly preformed on the page.

Each script has a list of pages that it will run on. This is defined in the GUI of the GreaseMonkey addon. The script will only run on pages that match the list of pages, allowing us to write scripts that are specific to a single page or task. 

## TDX Home Page
The TDX home page is the page that is displayed when the user first logs in. 

There are several optimizations to this page:
1. Automatically open the Assets tab.
2. The ```F1``` key will automatically keep the cursor in the search field.
3. The ```F2``` key will automatically open a new asset with the contents of the search field as the asset's serial number.

### Usage
#### **Entering New Assets**
The intended usage of this script is to press ```F1``` when the page loads to scan assets without needing to bring focus back to the search field. With focus on the search field, the user can scan an asset. If the asset exists, the page should come up with the asset's information. If the asset does not exist, the ```F2``` key can be pressed to open a new asset with the contents of the search field as the asset's serial number.

#### **Updating Sold Assets**
To set the status of sold assets, hit ```Ctrl+F12``` to open a dialog box. Enter a CSV list of asset serial numbers and hit OK. The script will then open each asset when ```F12``` is pressed. With each opened asset, press ```F12``` to set the status to sold. 

## TDX Asset Page
The TDX asset page is the page that is displayed when the user opens an asset.

There are several optimizations to this page:
1. Automatically populate the asset's serial number and name fields.
2. Automatically populate the asset's HDD SN field.
3. The ```F1``` key will automatically set most fields to represent an asset to kept for resale. The title will say *Pending Repair*.
4. The ```F2``` key will automatically set most fields to represent an asset to kept for parts. The title will say *Pending Disposal*.
5. The ```F3``` key will automatically add a comment to the asset saying there was no HDD in the asset.
6. The ```F4``` key will automatically add a comment to the asset, moving the cursor to the HDD SN field. The HDD's SN should then be scanned, including the line-break at the end. The line-break is necessary for the script to parse the SN for the field at the bottom of the document. 
7. The ```F12``` key will automatically set the asset's status to sold, automatically entering the edit mode and pressing the save button.
8. The ```Esc``` key will automatically open edit mode and save the asset.

### Usage

A typical workflow will go as follows:
1. Open an asset.
2. Press ```F1``` or ```F2``` to set the asset's status.
3. Press ```F3``` or ```F4``` to add a comment. If ```F4``` is pressed, scan the HDD SN.
4. Press ```Esc``` to save the asset.
5. Press ```Ctrl+W``` to close the asset page.



# Technical Details
This implementation uses JavaScript to automate user actions. The scripts above work by listening for keyboard events and then preforming actions based on the key pressed.

The actions preformed by the scripts include:
- Pressing a button.
- Setting the value of a field.
- Opening a new asset page.
- Moving the focus of the cursor. 

All of those actions are not complex in nature, but they are tedious to preform manually. 

## Getting the ID of an Element
All of these actions require the ID of the elements that are being modified. The ID of an element can be found by inspecting the element in the browser. The ID is the value of the ```id``` attribute of each element. The JavaScript can then call the ```getElementById``` method to get the element.

*Note: The IDs of elements are not constant. They can change between versions of TDX. If the IDs change, the scripts will need to be updated. This can cause things to break, especially in the Asset Page.*

The process for getting the ID of an element is as follows:
1. Open the page in a browser.
2. Right click on the element.
3. Click on ```Inspect Element```.
4. Make sure the correct element is selected in the HTML tree.
5. The ID of the element will be the value of the ```id``` attribute.

**This process is significantly more complicated for Fields in the Asset Page**

The Asset Page uses a custom auto-complete method for their fields, so the text that the user sees is not actually the value of the field. The value of the field is stored in a hidden field that is not visible to the user. The ID of the hidden field is the ID that should be used to set the value of the field. The visible field is used to show that the change has been made.

Even worse, these fields' IDs do not uniquely identify the field. Their IDs are based on their position in the form, so the IDs will change if the form changes. That makes ensuring the script is working properly somewhat difficult, requiring testing to ensure the script is working properly. 

*Note: That also means that the script can fail silently, without visually showing any errors.*

Refer to the Assets Page script for examples of what the IDs look like. The IDs for both the visible and hidden fields should be in different formats, making it easy to tell which is which. Often, the only difference between any two fields will be the number at the end of the ID.

## Pressing a Button
The main method for pressing a button would be to get the button's ID and then call the button's ```click()``` method. This is the method used by the ```F12``` key to edit and save the asset, as well as ```F2``` to open a new asset. 

## Setting the Value of a Field
The main method for setting the value of a field would be to get the field's ID and then set the field's ```value``` attribute. This is the method used in the Asset Page by the ```F1``` and ```F2``` keys to set the asset's status, as well as ```F3``` and ```F4``` to add a comment.