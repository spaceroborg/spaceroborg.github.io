**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2024/12/dr-kims-last-fun-friday-project/](https://www.bitcraze.io/2024/12/dr-kims-last-fun-friday-project/)**

2024-12-09 
 | 
 
Kimberly McGuire 
 | 
 
Leave a comment

Hi everyone! I have a bit of news to share… I’ve decided to leave Bitcraze at the end of 2024. But not before I share with you my latest Fun Friday project that I’ve tried my best to finish up before I leave before my Christmas holiday in December.

Frankensteining the Pololu Robot with the Crazyflie Bolt
--------------------------------------------------------

During the ROSCon talk about the lighthouse system (see the recording here), I’ve already shown a small example of how the lighthouse system could be used on other robots as well. Here you see a Pololu RPI 2040 (the hyper edition of course), with a slimmed down Crazyflie Bolt and a Lighthouse deck. The UART2 port on the Bolt (pinout is the same as Crazyflie) is interfacing with the UART0 connection on the Pololu (pinout). Then the Pololu’s 3v3 is connected to the vUSB and GND to GND (obviously), so 4 wires in total. Technically, the 3v3 port is not supplying enough power for the Crazyflie on paper, but it seemed to be enough as long as the Crazyflie Bolt doesn’t have motors connected it should be fine. But if anyone would like to do a driving-flying hybrid with this combo, you might need to check the specifications a bit closer. For now, just ignore the red low-battery LED on the Bolt, but if you see it restarting then perhaps give the Pololu a fresh set of batteries.

Since the Pololu RPI 2040 doesn’t have any wireless communication, this can be done through the Crazyflie Bolt and the Crazyradio. I’ve made an app layer variant for the Bolt to forward state estimates and velocity commands; however, it did require a bit of an extra logging variable in the firmware itself. But this allows me to control the Pololu through the CFclient! Since it’s using velocity commands, this means that the mobile app is out though, but perhaps if anyone is interested in getting this rolling, let me know. Also, the screen shows the current X, Y, Z, and yaw estimate of the Bolt transferred to the Pololu with the commands that I’ve given it.

I’d like to have connected this to a differential drive controller to make use of the position setpoints, but unfortunately the AA batteries ran out at the office and I was unable to complete this by the last day. It would have been great to use the Lighthouse positioning for this. Perhaps in the next coming months, I can try to continue with it and have my cats chase an autonomous robot around the house, who knows! If anyone is interested in playing around with this, these are the repositories/branches for both the Bolt and the Pololu:

* knmcguire/pololu-3pi-2040-robot at uart\_encoder\_motor\_control\_example (under /c/uart/)
* knmcguire/crazyflie-firmware at bolt-cmd-pose-uart (under /examples/app\_uart)

What is next?
-------------

First of all, I’ll take a long holiday in the US, first visiting New York (first time) before I hop over to Tulsa and Santa Barbara to visit family. Early 2025 I’ll be taking a long break, or a mini sabbatical of sorts, where I plan to work on some personal projects but mostly have a breather. I haven’t had a break like this in over 15 years, and given a tough 2023, I can definitely say that I’ve deserved some time off. What will happen after, I will hopefully figure out then, but for sure I will be continuing to co-lead the Aerial Robotics Interest Group at ROS and helping out in support of the Crazyswarm2 project.

I’d like to thank my colleagues at Bitcraze for an amazing 5 years here in Malmö, Sweden, and everyone that I was able to meet through them. I’ve learned a lot in terms of joint software development, code maintenance, community interaction, and, most importantly, having fun during work. I also will never forget the support I received while I was going through cancer treatment, and for that I’m very grateful. I wish you all the best and I hope the Crazyflie continues to thrive, saving more PhD projects as it did mine. Thank you.

 
Frontpage, Random stuff 
  Bitcraze, crazyflie