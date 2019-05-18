<p align="center"><img src="./static/icons/laptop.png" border="0" alt="Laptop-Controller Logo" height="150px" width="150px"></p>

<h1 align="center"> Laptop Controller </h1>

<span align="center">
  
[![Python Version](https://img.shields.io/badge/python-3.6-blue.svg?style=for-the-badge)](https://www.python.org/downloads/)
[![Issues](https://img.shields.io/github/issues/Vir-al/Laptop-Controller.svg?style=for-the-badge)](https://github.com/Vir-al/Laptop-Controller/issues)
![Language Count](https://img.shields.io/github/languages/count/Vir-al/Laptop-Controller.svg?style=for-the-badge&color=7cbeff)
[![Requirements](https://img.shields.io/requires/github/Vir-al/Laptop-controller.svg?style=for-the-badge)](https://github.com/raoniz/CAPSLG/blob/master/requirements.txt)
![Top Language](https://img.shields.io/github/languages/top/Vir-al/Laptop-controller.svg?style=for-the-badge&color=d33696)
[![License: GPL-3.0](https://img.shields.io/badge/License-GPL--3.0-success.svg?style=for-the-badge)](https://opensource.org/licenses/GPL-3.0)
![Size](https://img.shields.io/github/repo-size/Vir-al/Laptop-controller.svg?style=for-the-badge&color=eb0552)




The remote controller to control your Laptop/Computer using the cell phone.


</span>

----

# For Direct Use

## Configuration in computer
* Download the <img src="./static/icons/laptop.png" border="0" alt="Laptop_Controller_icon" height="25px" width="25px"> [laptop_controller.exe](https://github.com/Vir-al/Laptop-Controller/Computer/) for windows user.
* Connect your computer to a network via LAN cable through your router or to your wifi (The connection must be shared between computer as well as mobile).
* Run the Executable file (laptop_controller.exe) as administrator.

## Configuration in mobile
* Downlod the [laptop_controller.apk]().
* Install the apk in your phone.
* Connect to the wifi (same as to which your computer is connected).
* Now you can either serach your compter IP via search option.
* Or you an directly enter the IP address shown in the laptop_controller.exe (running on your computer).
* Once you registered to the computer IP adress, you can controller the basic funtionalities such as mouse, volume, brightness and media.

# For Custom Use

## Pre-requisites

* Python 3.5+ (If not available, kindly download from [here](https://www.python.org/downloads/))
* Android Studio 2+ (If not available, kindly download from [here](https://developer.android.com/studio))

## Configuration

1. Create a folder named *controller* .
2. Clone or download the repository inside the *controller* folder.

      ```console
      cd controller
      git clone https://github.com/Vir-al/Laptop-Controller.git
      ```
       
3. Install all the required python packages.

      ```console
      cd Computer
      pip install -r requirements.txt
      ```
4. Add any custom functionalities you want in computer/laptop_controller.py , find the Guide to edit [here]() ([Defualt](https://github.com/Vir-al/Laptop-Controller/Computer/laptop_controller.py)).

5. Open the android studio and select open an existing android studio project.

6. Navigate to the *controller* folder and Select the *Laptop Controller* project.

7. Add the corresponding functionalities added in python file (Find the Guide to edit [here]()).

8. Complie and run the APK in mobike and run the python file in computer.
