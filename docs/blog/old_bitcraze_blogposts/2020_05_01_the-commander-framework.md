**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2020/05/the-commander-framework/](https://www.bitcraze.io/2020/05/the-commander-framework/)**

2020-05-11 
 | 
 
Kimberly McGuire 
 | 
 
Leave a comment

Here is another blog post where we try to explain parts of the stabilizer framework of the Crazyflie. Last time, we talked about the controllers and state estimators as part of the s*tabilizer.c* module which was introduced in this blog post back in 2016. Today we will go into the commander framework, which handles the setpoint of the desired states, which the controllers will try to steer the estimated state to.

The Commander module
--------------------

The commander module handles the incoming setpoints from several sources (src/modules/src/commander.c in the firmware). A setpoint can be set directly, either through a python script using the cflib/ cfclient or the app layer (blue pathways in the figure), or by the high-level commander module (purple pathway). The High-level commander in turn, can be controlled remotely from the python library or from inside the Crazyflie.

General framework of the stabilization structure of the crazyflie with setpoint handling. \* *This part is takes place on the computer through the CFlib for python, so there is also communication protocol in between. It is left out of this schematics for easier understanding*.

It is important to realize that the commander module also checks how long ago a setpoint has been received. If it has been a little while (defined by threshold COMMANDER\_WDT\_TIMEOUT\_STABILIZE in commander.c), it will set the attitude angles to 0 on order to keep the Crazyflie stabilized. If this takes longer than COMMANDER\_WDT\_TIMEOUT\_SHUTDOWN, a null setpoint will be given which will result in the Crazyflie shutting down its motors and fall from the sky. This won’t happen if you are using the high level commander.

Setpoint structure
------------------

In order to understand the commander module, you must be able to comprehend the setpoint structure. The specific implementation can be found in src/modules/interface/stabilizer\_types.h as setpoint\_t in the Crazyflie firmware.

There are 2 levels to control, which is:

* Position (X, Y, Z)
* Attitude (pitch, roll, yaw or in quaternions)

These can be controlled in different modes, namely:

* Absolute mode (*modeAbs*)
* Velocity mode (*modeVelocity*)
* Disabled (*modeDisable*)

Setpoint structures per controller level

So if absolute position control is desired (go to point (1,0,1) in x,y,z), the controller will obey values given *setpoint.position.xyz* if *setpoint.mode.xyz* is set to *modeAbs*. If you rather want to control velocity (go 0.5 m/s in the x-direction), the controller will listen to the values given in *setpoint.velocity.xyz* if s*etpoint.mode.xyz* is set to *modeVel*. All the attitude setpoint modes will be set then to disabled (*modeDisabled*). If only the attitude should be controlled, then all the position modes are set to *modeDisabled*. This happens for instance when you are controlling the crazyflie with a controller through the cfclient in attitude mode.

High level commander
--------------------

Structure of the high level commander

As already explained before: The high level commander handles the setpoints from within the firmware based on a predefined trajectory. This was merged as part of the Crazyswarm project of the USC ACT lab (see this blogpost). The high-level commander uses a planner to generate smooth trajectories based on actions like ‘take off’, ‘go to’ or ‘land’ with 7th order polynomials. The planner generates a group of setpoints, which will be handled by the High level commander and send one by one to the commander framework.

It is also possible to upload your own custom trajectory to the memory of the Crazyflie, which you can try out with the script examples/autonomous\_sequence\_high\_level of.py the crazyflie python library repository. Please see this blogpost to learn more.

Support in the python lib (CFLib)
---------------------------------

There are four main ways to interact with the commander framework from the python library.

1. Send setpoints directly using the Commander class from the Crazyflie object, this can be seen in the autonomousSequence.py example for instance.
2. Use the MotionCommander class, as in motion\_commander\_demo.py. The MotionCommander class exposes a simplified API and sends velocity setpoints continuously based on the methods called.
3. Use the high level commander directly using the HighLevelCommander class on the Crazyflie object, see autonomous\_sequence\_high\_level.py.
4. Use the PositionHlCommander class for a simplified API to send commands to the high level commander, see the position\_commander\_demo.py

Documentation
-------------

We are busy documenting the stabilizer framework in the Crazyflie firmware documentation, including the content of this blogpost. If you feel that anything is missing or not explaining clearly enough about the stabilizer framework, please drop a comment below or comment on the forum.

 
Crazyflie, Frontpage, Software