**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2021/12/simulation-possibilities/](https://www.bitcraze.io/2021/12/simulation-possibilities/)**

2021-12-13 
 | 
 
Kimberly McGuire 
 | 
 
8 Comments

I have returned from my family visit in California, who I’ve haven’t seen them in 3 years due to Covid. To spend the most possible time with them, the plan was that I would still work full time for Bitcraze from my father’s home. The problem became however, that it wouldn’t fit so well in our current way of work as I would miss all the morning stand up meetings due to the large time difference between Sweden and California (-9 hours). That is why we settled that I would work on separate projects/investigations during my time away. So I thought it would be a great opportunity to dig into ROS and 3D simulations again and see what the latest state of that is! So about the simulations is what I’ll be mostly talking about right in this blog post, in terms of what simulators are out there and what simulation development is currently ongoing.

Need for simulation?
--------------------

Why would it be actually be necessary to have a simulation in our current frame work? Just to give an example, my new colleague Jonas recently tried out his hand on the CFlib swarm class for the first time for the BAMdays tutorials, and simulator would have been great during that initial porcess. Namely, most of the crashes were not necessary due to low batteries or bad communication, but mostly due to the fact that he was not able to double check his script beforehand. If one is able to check if all the programmed positions of the Crazyflies are implemented as they should before an actual flight, this would prevented a lot of broken propellers!

Just to note here that there are a lot of types of simulations that you can think of. Earlier this year had our ex-interns Max and Josephine finish an Renode simulation of the Crazyflie’s microcontrollers. We’ve also seen the word Simulink pop-up multiple times on the forum which indicates that quite some control classes are investigating the dynamic model of the Crazyflie. However, the type of simulation that I’m currently referring to are the 3D simulators in which a robot or quadcopter can move and interact with a virtual environment, with usually an physics engine in effect.

Crazyflie in Gazebo (+ROS)
--------------------------

During some initial investigation there were already some simulations that pop out. First of all I went and looked into what is available for Gazebo at the moment, which is:

* CrazyS: https://github.com/gsilano/CrazyS (ROS Melodic and Gazebo 9)
* sim\_cf: https://github.com/wuwushrek/sim\_cf (ROS Kinetic and Gazebo 7)

CrazyS is based on the RotorS simulation with some additional off-board crazyflie controllers for position control. I wasn’t able to build it for my Ubuntu 20.04 just yet myself, but that there is ongoing work to port CrazyS to ROS Noetic. For now on a virtual machine with ROS melodic it build just fine! Note my laptop did had to work quite hard when I wanted to simulate more than 1 Crazyflie, but the physics and plugins that were made for Gazebo is enabling many to do a lot for their research. Please check out the core papers about CrazyS!

Sim\_cf is perhaps a little lesser known, but the project does stand out as it has some interesting features to it. It is for instance, possible to use the actual c-based firmware in software-in-the-loop (SITL) mode, which controls the simulated Crazyflie. It is even possible to use an actual crazyflie with an hardware-in-the-loop (HITL) simulation. Eventhough the project is not actively maintained anymore, I did manage to build it from source for ROS Noetic and Gazebo 11, although I was not able to fly more than 4 do to errors.

Other Simulators
----------------

Ofcourse Gazebo is not the only possibility out there. I also had a quick go at another simulator called Webots, which is quite an interesting option indeed as well. Currently there is only one quadcopter model available, so it only makes sense for it to also contain an Crazyflie! They do use their own robotic format, so probably the easiest process would be, is to convert an existing model for Gazebo/ROS into an format that Webots can understand.

Also, quite recently, a trending tweet has brought us to the attention of a Rviz based Crazyflie simulation! This looks quite promising as well, so I will try this out quite soon too.

*Crazyflie in Ignition Gazebo*

Ongoing work in Ignition Gazebo
-------------------------------

So in the future, the current Gazebo in its form will disappear and will be only be part of Ignition. So that is why it made sense for me to start playing with an separate Crazyflie model and plugins for the Ignition frame work instead. Moreover, it seems that quite some elements and plugins based on the RotorS simulation for the original gazebo, are now fully integrated within the Ignition gazebo framework, which should make it more easier to make quadcopter models fly. Currently it’s still work in progress, so right now is only to be found on my personal github repository, but as soon as it becomes more fleshed out and stable, this will probably transferred to Bitcraze’s github repos and we will write a more elaborate blogpost about it. For now, I’ll try to work on it further as my Fun Friday project!

In the mean time, we have started a simulation discussion thread in the Crazyswarm2 repository, which is an ongoing port of Crazyswarm to ROS2. It would be the ideal situation if we would be able to use this simulator for both Crazyswarm and our native CFlib! But I’ve mostly have used Gazebo in the past, so if there are any other simulators that we should try out too, please join the discussion and let us know!

 
Crazyflie, Frontpage, Fun Friday, How we work, Random stuff, Software 
  crazyflie, gazebo, ROS, simulation