**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2020/02/out-of-control/](https://www.bitcraze.io/2020/02/out-of-control/)**

2020-02-03 
 | 
 
Kimberly McGuire 
 | 
 
2 Comments

Two weeks ago, we had a blogpost about the state estimators that are available within the Crazyflie. So once the Crazyflie knows where it is, it would need to be determined where it wants to go, by means of the high level commander (implemented as part of the crazyswarm project) or set-points given by CFclient or directly from scripts using Crazyflie python lib. But exactly how would the crazyflie get to those desired positions in the first place? The differences between the current state estimates and the desired state, will need to be transformed to inputs given to the motors. Unfortunately, quadrotors like the Crazyflie do not have easy dynamics to maintain, so if you want to learn more, see this blogpost to read more about it!

Controlling the Crazyflie

So in order use the thrust of the motors in an useful way to get the Crazyflie to do what you want to do, there are several controllers to consider, which you can see on this quick overview here underneath. It shows the different control paths that can be taken from the high level commander all the way to the power distribution of the motors. Bear in mind that these are still simple representations and that the actual implementation is of course a bit more complicated, but at least it will give you a rough idea of which paths are possible to pursue.

Possible controller pathways

PID Controller
--------------

So the default settings in the Crazyflie firmware is the proportional integral derivative (PID) control for all desired state aspects. So the High Level Commander (HLC) will send desired position set-points to the PID position controller (which used to be done off-board, so outside of the Crazyflie firmware before this blogpost). These result in desired pitch and roll angles, which are sent directly to the attitude PID controller. These determine the desired angle rates which is send to the angle rate controller (which is… you guessed… also a PID controller). This is also called **Cascaded PID controller**. That results in the desired thrusts for the roll pitch yaw and height that will be handled by the power distribution by the motors. (Note that height is mostly handled by the position controller)

INDI Controller
---------------

So the Incremental Nonlinear Dynamic Inversion (INDI) controller is an controller that immediately deal with the angle rates to determine the trust. This is a very new addition to the Crazyflie firmware by one of our community members and is based on the implementation of this paper. Currently, the position control is still handled by the same PID controller mentioned in the last paragraph, Nevertheless for handling the angles, it should be faster than the attitude and rate PID controller combined. We have not yet fully tested this out but if you do, let us know how you like it on the Bitcraze forum!

Mellinger Controller
--------------------

As part of the Crazyswarm project, the controller designed by Daniel Mellinger has been implemented in the Crazyflie firmware as well. Please see this paper about the details of the Mellinger controller. It is a sort of “all in one”: based on the desired position and velocity vectors towards those position, it will calculate right away what the desired thrusts are that need to be distributed to all the motors. This results in a much smoother controlled trajectory of the high level commander and therefore advised to use when the Crazyflie has a precise position estimate (lighthouse and mocap). However, as it is so aggressive, any position estimate of a lesser quality (flowdeck or LPS) will not be sufficient for this controller. See some examples of mellinger controlled flights here and here.

Let us know what you think!
---------------------------

So do you have experience working with these controllers or want to know more about them, please drop us a message on the forum! We are currently working on stabilization and documentation of multiple aspects of the Crazyflie and the controllers is one of them, so we are really interested what your experiences are!

 
Crazyflie, Frontpage, Random stuff, Software