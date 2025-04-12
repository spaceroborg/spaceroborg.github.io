**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2022/03/updates-on-simulation-work/](https://www.bitcraze.io/2022/03/updates-on-simulation-work/)**

2022-03-14 
 | 
 
Kimberly McGuire 
 | 
 
Leave a comment

In December we had a blogpost where we gave an overview of existing simulation models that were out there. In the mean time, I have done some work during my Fun Fridays to get this to work even further. Currently I moved the efforts from my personal Github repo to the Bitcraze organization github called crazyflie-simulation. It is all still very much work in progress but in this blogpost I will explain the content of the repository and what these elements can already do.

Low Poly CAD model
------------------

The first thing that you will need to have for any simulation, is a 3D model of the Crazyflie. There is of course already great models available from the CrazyS project, the sim\_cf project and the multi\_uav\_simulator, which are completely fine to use as well. But since we have direct access to the exact geometries of the real crazyflie itself, I wanted to see if I could abstract the shapes myself. And also I would like to improve my Blender skills, so this seemed to be a nice project to work with! Moreover, it might be handy to have a central place if anybody is looking for a 3D simulation model of the Crazyflie.

For simulations with only one or a few Crazyflie, the higher resolution models from the other repository are absolutely sufficient, especially if you are not using a very complicated physics geometry model (because that is where most of the computation is). But if you would like to simulate very big swarms, then the polygon count will have more influences on the speed of the simulation. So I managed to make it to 1970 vertices with the below Crazyflie model, which is not too bad! I am sure that we can make it even with lesser polygons but this is perhaps a good place to start out with for now.

In the crazyflie-simulation, you can find the Blender, stl files and collada files under the folder ‘meshes’.

Webots model
------------

We implemented the above model in a Webots simulator, which was much easier to implement than I thought! The tutorials they provide are great so I was able to get the model flying within a day or two. By combining the propeller node and rotational motor, and adjusting the thrust and drag coefficient to be a bit more ‘Crazyflie like’, it was able to take off. It would be nice to perhaps base these coefficients on the system identification of the Crazyflie, like what was done for this bachelor thesis, but for now our goal is just to make it fly!

The webots model can found in the same simulation repository under */webots/*. You can try out the model by

```
webots webots/world/crazyfly_world.wbt
```

It would then be possible to control the pitch and roll with the arrow keys of your keyboard while it is maintaining a current height of 1 meter. This is current state of the code as of commit 79640a.

[](https://www.bitcraze.io/wp-content/uploads/2022/03/crazyflie_world.mp4)

Ignition Gazebo model
---------------------

Ignition will be the replacement for Gazebo Classic, which is already a well known simulator for many of you. Writing controllers and plugins is slightly more challenging as it is only in C++ but it is such a landmark in the world of simulation, it only makes sense that we will try to make a Gazebo model of the Crazyflie as well! In the previous blogpost I mentioned that I already experimented a bit with Ignition Gazebo, as it has the nice multicopter motor model plugin standard within the framework now. Then I tried to make it controllable with the intergrated multicopter velocity control plugin but I wasn’t super successful, probably because I didn’t have the right coefficients and gains! I will rekindle these efforts another time, but if anybody would like to try that out, please do so!

First I made my own controller plugin for the gazebo model, which can be found in the repository in a different branch under /gazebo-ignition/. This controller plugin needs to be built first and it’s bin file added to the path IGN\_GAZEBO\_SYSTEM\_PLUGIN\_PATH, and the Crazyflie model in IGN\_GAZEBO\_RESOURCE\_PATH , but then if you try to fly the model with the following:

```
 ign gazebo crazyflie_world.sdfCode language: CSS (css)
```

It will take off and hover nicely. Unfortunately, if you try out the key publisher widget with the arrow keys, you see that the Crazyflie immediately crashes. So there is still something fishy there! Please check out the issue list of the repo to check the state on that.

Controllers
-----------

So the reason why I made my own controller plugins for the above mentioned simulation models, is that I want to experiment with a way that we can separate the crazyflie firmware controllers, make a code wrapper for them, and use those controllers directly in the simulator. So this way it will become a hybrid software in the loop without having to compile the entire firmware that contains all kinds of extra things that the simulation probably does not need. We can’t do this hybrid SITL yet, but at least it would be nice to have the elements in place to make it possible.

Currently I’m only experimenting with a simple fixed height and attitude PID controller written in C, and some extra files to make it possible to make a python wrapper for those. The C-controller itself you can try out in Webots as of this commit 79640a, but hopefully we will have the python version of it working too.

What is next?
-------------

As you probably noticed, the simulation work are still very much work in process and there is still a lot enhancements to add or fix. Currently this is only done on available Fridays so the progress is not super fast unfortunately, but at least there is one model flying.

Some other elements that we would like to work on:

* Velocity controller, so that the models are able to react on twist messages.
* Crazyflie firmware bindings of controllers
* Better system variables (at least so that the ign gazebo model and the webots model are more similar)
* CFlib integration
* Add a multiranger and/or camera.
* and more!

I might turn a couple of these into topics that would be good for contribution, so that any community members can help out with. Please keep an eye on the issue list, and we are communicating on the Crazyswarm2 Discussion page about simulations if you want to share your thoughts on this as well.

 
Crazyflie, Frontpage, Fun Friday, Random stuff, Software, Video 
  crazyflie, gazebo, simulation, webots