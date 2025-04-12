**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2023/11/go-with-the-flow-relative-positioning-with-the-flow-deck](https://www.bitcraze.io/2023/11/go-with-the-flow-relative-positioning-with-the-flow-deck)**

2023-11-27 
 | 
 
Kimberly McGuire 
 | 
 
1 Comment

The Flow deck has been around for some time already, officially released in 2017 (see this blog post), and the Flow deck v2 was released in 2018 with an improved range sensor. Compared to MoCap positioning and the Loco Positioning System (based on Ultrawideband) that were already possible before, optical flow-based positioning for the Crazyflie opened up many more possibilities. Flight was no longer confined to lab environments with set-up external systems; people could bring the Crazyflie home and do their hacking there. Moreover, doing research for exploration techniques that cannot rely on external positioning systems was possible with it as well. For example, back in my day as a PhD student, I relied heavily on the Flow deck for multi-Crazyflie autonomous exploration. This would have been very difficult without it.

However, despite the numerous benefits that the Flow deck provides, there are also several limitations. These limitations may not be immediately familiar to many before purchasing a Crazyflie with a Flow deck. A while ago, we wrote a blog post about positioning systems in general and even delved into the Loco Positioning System in detail. In this blog post, we will explore the theory of how the Flow deck enables the Crazyflie to fly, share general tips and tricks for ensuring stable flight, and highlight what to avoid. Moreover, we aim to make the Flow deck the focus of next week’s Developer meeting, with the goal of improving or clarifying its performance further.

Theory of the Flow deck
-----------------------

I won’t delve into too much detail but will provide a generic indication of how the Flow deck works. As previously explained in the positioning system blog post, the Flow deck is a relative positioning system with onboard estimation. “Relative” means that wherever you start is the (0, 0, 0) position. The extended Kalman filter processes flow and height information to determine velocity, which is then integrated to estimate the position—essentially dead reckoning. The onboard Kalman filter manages this process, enabling the Crazyflie to use the information for stable hovering.

*Image from Positioning System Overview blogpost*

The optical flow sensor (PMW3901) calculates pixel flow per frame (this old blog post explains it well), and the IR range sensor (VL53L1x) measures height up to 4 meters (under ideal conditions). The Kalman filter incorporates a measurement model that describes the relationship between these two values and the velocity of the Crazyflie. More detailed information can be found in the state estimation documentation. This capability allows the Crazyflie to hover, as explained in the getting started tutorial.

*Image from state estimation repo documentation*

Tips & Tricks and Limitations
-----------------------------

If you want to fly with the Crazyflie and the Flow deck, there are a couple of things to take in mind:

* Take off from a floor with texture. Natural texture like wood flooring is probably the best.
* The floor shouldn’t be too shiny, and be aware of infrared scattering for the height sensor
* The room should be well-lit, as the sensor needs to see the texture.

There are certain situations that the Flow deck has some issues with:

* Low or no texture. Flying above something that is only one plain color
* Black areas. Similar reason to flying above no texture, but it’s more difficult than usual. Especially with startup, the position estimate diverges
* Low light conditions
* Flying over its own shadow

We made a video that shows these types of behaviors, starting of course with the most ideal flying conditions:

Moreover, it is also important to note that you shouldn’t fly too high or yaw too often. The latter will make the Crazyflie drift, as the optical flow cannot be distinguished as being caused by the yaw movement.

Developer meeting about Flow deck
---------------------------------

We believe that many of the issues people experience are primarily due to the invisibility of the positioning quality. In many of our examples, the Crazyflie will not take off if the position is stable. However, we don’t have a corresponding functionality in our CFclient, as it is more up to the user to recognize when the positioning is diverging. There is a lot of room for improvement in this regard.

This is the reason why the next developer meeting will specifically focus on the Flow deck, which will be on **Wednesday the 6th of December, 3 pm central European time**. During the meeting, we will explain more about the Flow deck, discuss the issues we are facing, and explore ways to enhance the visibility of positioning quality. Check out this discussion thread for information on how to join.

 
Crazyflie, Frontpage, Random stuff, Video 
  autonomy, crazyflie, Flow deck, video