**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2022/08/crazyflie-ros2-summer-update/](https://www.bitcraze.io/2022/08/crazyflie-ros2-summer-update/)**

2022-08-01 
 | 
 
Kimberly McGuire 
 | 
 
2 Comments

Now it is time to give a little update about the ongoing ROS2 related projects. About a month ago we gave you an heads-up about the Summer ROS2 project I was working on, and even though the end goal hasn’t been reached yet, enough has happened in the mean time to write a blogpost about it!

Crazyflie Navigation
--------------------

Last time showed mostly mapping of a single room, so currently I’m trying to map a bigger portion of the office. This was initially more difficult then initially anticipated, since it worked quite well in simulation, but in real life the multi-ranger deck saw obstacles that weren’t there. Later we found out that was due to this year old issue of the multi-ranger’s driver incapability to handle out-of-range measurements properly (see this ongoing PR). With that, larger scale mapping starts to become possible, which you can see here with the simple mapper node:

If you look at the video until the end, you can notice that the map starts to diverge a bit since the position + orientation is solely based on the flow deck and gyroscopes , which is a big reason to get the SLAM toolbox to work with the multi-ranger. However, it is difficult to combine it with such a sparse ‘Lidar’ , so while that still requires some tuning, I’ve taken this opportunity to see how far I get with the non-slam mapping and the NAV2 package!

As you see from the video, the Crazyflie until the second hallway. Afterwards it was commanded to fly back based on a NAV2 waypoint in RViz2. In the beginning it seemed to do quite well, but around the door of the last room, the Crazyflie got into a bit of trouble. The doorway entrance is already as small as it is, and around that moment is also when the mapping started to diverge, the new map covered the old map, blocking the original pathway back into the room. But still, it came pretty close!

The diverging of the map is currently the blocker for larger office navigation, so it would be nice to get some better localization to work so that the map is not constantly changed due to the divergence of position estimates, but I’m pretty hopeful I’ll be able to figure that out in the next few weeks.

Crazyflie ROS2 node with CrazySwarm2
------------------------------------

Based on the poll we set out in the last blogpost, it seemed that many of you were mostly positive for work towards a ROS2 node for the Crazyflie! As some of you know, the Crazyswarm project, that many of you already use for your research, is currently being ported to ROS2 with efforts of Wolfgang Hönig’s IMRCLab with the Crazyswarm2 project. Instead of in parallel creating separate ROS2 nodes and just to add to the confusion for the community, we have decided with Wolfgang to place all of the ROS2 related development into Crazyswarm2. The name of the project will be the same out of historical reasons, but since this is meant to be the standard Crazyflie ROS2 package, the names of each nodes will be more generic upon official release in the future.

To this end, we’ve pushed a cflib python version of the crazyflie ros2 node called crazyflie\_server\_py, a bit based on my hackish efforts of the crazyflie\_ros2\_experimental version, such that the users will have a choice of which communication backend to use for the Crazyflie. For now the node simply creates services for each individual Crazyflie and the entire swarm for *take\_off*, *land* and *go\_to* commands. Next up are logging and parameter handling, positioning support and broadcasting implementation for the CFlib, so please keep an eye on this ticket to see the process.

So hopefully, once the summer project has been completed, I can start porting the navigation capabilities into the the Crazyswarm2 repository with a nice tutorial :)

ROScon talk
-----------

As mentioned in a previous blogpost, we’ll actually be talking about the Crazyflie ROS2 efforts at ROScon 2022 in Kyoto in collaboration with Wolfgang. You can find the talk here in the ROScon program, so hopefully I’ll see you at the talk or the week after at IROS!

 
Crazyflie, Frontpage, Fun Friday, Random stuff, Software, Video 
  crazyflie, navigation, ROS2