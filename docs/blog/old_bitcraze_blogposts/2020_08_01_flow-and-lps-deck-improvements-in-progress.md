**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2020/08/flow-and-lps-deck-improvements-in-progress/](https://www.bitcraze.io/2020/08/flow-and-lps-deck-improvements-in-progress/)**

2020-08-17 
 | 
 
Kimberly McGuire 
 | 
 
2 Comments

Now that we are all back from our summer holiday, we are back on what we were set on doing a while ago already: fixing issues and stabilizing code. In the last two weeks we have been focusing on fixing existing issues of the Flowdeck and LPS positioning system. It is still work in progress and even though we fixed some problems, we still have some way to go! At least we can give you an update of our work of the last few weeks.

Flow-deck Kalman Improvements
-----------------------------

When we started working on the motion commander tutorials (see this blogpost), which are mostly based on flying with the flowdeck, we were also hit by the following error that probably many of you know: the Crazyflie flies over a low texture area, wobbles, flips and crashes. This won’t happen as long as you are flying of high texture areas (like a children’s play mat for instance), but the occasional situation that it is not, it should not crash like it does now. The expected behavior of the Crazyflie should be that it glides away until it flies over something with sufficient texture again (That is the behavior that you see if when you are flying manually with a controller, and you just let the controls go). So we decided to investigate this further.

First we thought that it might had something to do with the rotation compensation by the gyroscopes, which is part of the measurement model of the flowdeck, since maybe it was overcompensating or something like that. But if you remove that parts, it starts wobbling right away, *even* with high texture areas… so that was not it for sure… Even though we still think that it causes the actual wobbling itself (compensating flow that is not detected) but we still had to dig a bit deeper into the issue.

Eventually we did a couple of measurements. We let the Crazyflie fly over a low and high texture area while flying an 8 shape and log a couple of important values. These were the detected flow, the ground truth position, and a couple of quality measurements that the Pixart’s PMW3901 flow sensor provided themselves, namely the amount of features (motion.squal) and the automatic shutter time (motion.shutter). With the ground truth position we can transform that to the ground truth flow that the flowdeck is supposed to measure. With that we can see what the standard deviation of the measurement vs groundtruth flow is supposed to be, and see if we can find a relation the error’s STD and the quality values, which resulted in these couple of nice graphs:



Three major improvements were added to the code based on these results:

* The standard deviation is the flow measurement is increased from 0.25 to 2.0 pixels, since this is actually a more accurate depiction of the measurement noise to be expected by the Kalman filter
* An adaptive std based on the *motion.shutter* has been implemented (since there is a stronger correlation there than with *motion.squal*), which can activated putting the parameter *motion.adaptive* to True or 1. Its put by default on False or 0 since the heightened STD of the first improvement already increased the quality of flight significantly.
* If the flow sensor indicates there is no motion detected (log *motion.motion*), it will now prevent to send any measurement value to the Kalman filter. Also it will adjust the difference in time (dt) between samples based on the last measurement received.

Now when the Crazyflie flies over low texture areas with the Flowdeck alone, it will not flip anymore but simply glide away! Check out this closed issue to know more about the exact implementation and it should be part of the next release.

The LPS and Flowdeck
--------------------

### Kalman filter conflicts

The previous fix of the flow deck also took care of this issue, which caused the Crazyflie to also flip in the LPS system if it does not detect any flow.. This happened because the Kalman filter trusted the Flow measurement much more than the UWB distance measurement in the previous firmware version, but not anymore! If the Flowdeck is out of range or can’t detect motion, the state estimation will trust the LPS system more. However, once the Flowdeck is detecting motion, it will help out with the accuracy of the positioning estimate.

Moreover, now it is possible to make the Crazyflie fly in and out of the LPS system area with the Flowdeck! however, be sure that it flies using velocity commands, since there are situations where the position estimate can skip:

* 1- LPS system is off 2- take off Crazyflie with only Flowdeck, 3 – turn on the LPS nodes
* 1- Take off in LPS, 2- fly out of LPS system’s reach for a while (position estimate will drift a bit) 3- Fly back into the LPS system with position estimation drift due to Flowdeck.

As long as your are flying with velocity commands, like with the assist modes with the controller in the CFclient, this should not be a problem.

### Deck compatibility problems

The previous fixes only work with the LPS methods *TDOA2* and *TDOA3*. Unfortunately, there is still some work to be done with the Deck incompatibility with the TWR method and the Flowdeck. The deck stops working quickly after the Crazyflie is turned on and this seems to be related to the SPI bus that is shared by the LPS deck and the flowdeck. Reading the flow sensor takes some time, which blocks the TWR algorithm for a while, making it miss an event. Since the TWR algorithm relies on a continues stream of events from the DWM1000 chip, it simply stops working if it does not … or at least that is our current theory …

Please check out this issue to follow the ongoing discussion. If you have maybe an idea of what is going on, drop a comment and see if we can work together to iron out this issue once and for all!

 
Crazyflie, Frontpage, Loco Positioning, Random stuff, Software