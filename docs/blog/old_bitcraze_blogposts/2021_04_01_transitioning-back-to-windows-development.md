**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2021/04/transitioning-back-to-windows-development/](https://www.bitcraze.io/2021/04/transitioning-back-to-windows-development/)**

2021-04-05 
 | 
 
Kimberly McGuire 
 | 
 
Leave a comment

When I was started my Robotics Master back in 2012, I remembered how frustrated I was at the time to setup my development environment in Windows for the C++ beginners course. My memory is a bit fuzzy of course but I remembered it took me days to get all the right drivers, g++ libraries right, and to setup all in the path environmental in Eclipse at the time. Once I started working on Ubuntu for my Master thesis, forced to due to ROS, I was hooked and swore I will never go back to Windows for robotics development again… until now!

I always used Windows on my personal machine on the side for gaming and have a dual-boot on the work computer for some occasional video editing, but especially I had begun to learn game development for Fun Fridays, I started to be drawn to the windows side of the dual boot more and more. But if I needed to try something out on the Crazyflie or needed to debug a problem on the forum, I needed to restart the computer to switch operating systems and that was starting to become a pain! Slowly but steadily I tried out several aspects of the crazyflie ecosystem for development on Windows 10 and actually…. it is not so traumatic as it was almost 10 years ago.

Python Library and Client
-------------------------

It went quite smooth when I first try to install python on windows again. Adding it to the PATH environment variable is still very important but luckily the new install manager provides that as an option. Moreover, Visual Studio Code also provides the possibility to switch between python environments so that you try different versions of python, but for now version 3.8 was plenty for me.

With the newest versions of the Windows install of Python, pip is by definition already installed, but I experienced that it would still be necessary to upgrade pip by typing the following in either a Command Prompt or (my favorite) Powershell:

```
python -m pip install --upgrade pip
```

After this, install the cflib from release was quite an ease (‘pip install cflib’) but even installing it from source with Git configured on Windows was no problem at all and very similar to a native Ubuntu install.  
  
Until recently the cfclient was a bit more challenging to install through pip from due the SDL2 windows library had to be downloaded separately, so the only options would have been installing from source or the .exe application release. The later has not been updated since the 2020.09 release due to building errors. Luckily, with the latest release, this has now been fixed as a SLD2 python library was found. Now the cfclient can be installed with a simple ‘pip install cfclient’.

Firmware Building with WSL
--------------------------

The firmware development was the next thing that I tried to get up and running, which managed to be slightly trickier. About a year ago I tried to get Cygwin to work on Windows, but my bad memories of the past came back due to the clunkiness of it all and I abandoned it again. Also there are some reported issues with the out-of-tree build (aka the App layer). Some colleagues at Bitcraze already mentioned the Windows Subsystem for Linux (WSL) but I never really looked at it until the need came to move back to Windows for development. And I must say, I wish I had tried it out a while ago.

With some repositories downloaded already on my Windows system with Git, I installed Ubuntu 20.04 WSL, got the appropriate gcc libraries and accessed the crazyflie-firmware by *‘cd /mnt/c/my/repos*‘. Building the firmware with *‘make all’* went pretty okay… although it took about a minute which is a little long compared to the 20 secs on the native Ubuntu install. The big problem was that I could not use Docker and the handy bitcraze toolbelt due to the WSL version still being 1. These functionalities were only available for version 2 so I went ahead and upgraded the WSL and linked it to docker desktop. But after upgrading, building the firmware from that same repository on the C:/ drive took insanely long (almost 10 minutes). So I switched back the WSL ubuntu 20.04 to version 1, installed a second WSL (this time Ubuntu 18.04), updated that one to WSL2 and used solely for docker and toolbelt purposes. Not ideal quite yet… but luckily with visual studio code it is very easy to switch the WSL .

But there is more though! Recently I timed how long it took to build the crazyflie-firmware with ‘make all -j8’ from both WSL version in a repository that is on the C:/ drive on Windows (accessible by /mnt/c from the WLS), or from a repository on the local file system:

* WSL 2 (ubuntu 18.04)
  + C:/ = 11m06s
  + WSL local = *00m19s*
* WSL 1 (ubuntu 20.04)
  + C:/ = 01m04s
  + WSL local = 00m59s

This is done on an Windows laptop with an i7-6700HQ with 32 Gb RAM. The differences with WLS2 between build firmware on the windows file system or the local WSL file system is huge! So that means that the right way is to have WSL2 with the repo on the WSL file system, which is similar to build time as a native install of Ubuntu.

Flashing the Crazyflie
----------------------

The main issue still with WSL is that it does not allow USB access… So even if the crazyradio driver is installed on windows with Zadig, you will not be able to see if you type ‘*lsusb*‘ in WSL for both version 1 and 2. So when I still had the repository on the C:/ drive and build the crazyflie-firmware from there I could flash the Crazyflie through the Cfclient or Cflib (with cfloader) through Powershell, but building it from the local subsystem, which is way faster for WSL2, would require to first copy the cf2.bin file to my C drive before doing that.

Another option, although still in Alpha phase, is to use the experimental Crazyradio server for WSL made by Arnaud, for which the user instructions can be found in an issue thread only for now. The important thing is that the Zadig installed driver has to be switched to WinUSB and switched back again to LibUSB if you want to use the Cfclient on windows. It would still needs some work to improve the user experience but gives promise of better integration of WSL development for the Crazyflie.

To Conclude
-----------

Soon I’m planning to soon reinstall the Windows part on the dual boot laptop but there are already some things that I will integrate on my freshly installed Windows based on what I experienced so far:

* Keep using Python on windows and install the Cfclient and Cflib by pip only.
* Only use Ubunu 20.04 as WSL2 and install the Crazyflie-firmware on the WSL local file system.
* Use Visual Studio Code as the editor for both C:/ based and WSL based repos.
* Use the Crazyradio server or copy the bin file to C:/ whenever I need to flash the crazyflie with development firmware.

For any AIdeck development, I would still need to use the native Ubuntu part or the bitcraze-VM since there is not a USB access or server yet for the programmer. However, if Windows would support USB devices and a graphical interface for WSL, that will make all our Windows-based Crazyflie development dreams come true!

 
Crazyflie, Frontpage, Software