# OBD_Diag_CMD
# Car Diagnostic Software using PyOBD

This command line software allows you to read vehicle information, diagnostic trouble codes, and real-time engine parameters using the ELM-327 OBD2 adapter.

## Prerequisites

* Python 3.x
* PyOBD library ```__pip install obd__```
> if you are using a bluetooth adapter on Linux, you also need to install and configure the bluetooth tools. 
`On Debian-based systems :```$ sudo apt-get install bluetooth bluez-utils blueman``
* ELM-327 OBD2 Adapter

## Usage

* Connect the ELM-327 Adapter to the vehicle's port.
* Open a terminal and navigate to the project directory
* Execute by running the command ```__python car_diag.py__```
* The software will display the vehicle information, diagnostic trouble codes and real-time engine parameters 
* To clear the diagnostic trouble codes, uncomment the line ```__connection.query(obd.commands.CLEAR_DTC)__```. A V2 of this app will include a more user-friendly way to use the software.
* To stop the software, press '___Ctrl+C___'

The software should work on most operating systems.
However, if you encounter any issue, please make sure the ELM adapter is properly connected and that the Python OBD library is downloaded.

## Notes

* The software has been tested on Windows 11 and Ubuntu 20.04. To be tested : Windows 10-, MacOs, Arch + Debian distros.
* Feel free to add or remove features by modifying the source code on your machine. However a more CarSoft-like version of this software is in WIP.

## Author

_KLAK Karolina_
_kklak.pro@gmail.com_

This software was written by _KLAK Karolina_.
Feel free to pull an issue ticket if needed or to send me directly a message with your issue.