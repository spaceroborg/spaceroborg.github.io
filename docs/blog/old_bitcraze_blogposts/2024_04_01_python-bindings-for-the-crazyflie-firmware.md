**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2024/04/python-bindings-for-the-crazyflie-firmware/](https://www.bitcraze.io/2024/04/python-bindings-for-the-crazyflie-firmware/)**

2024-04-01 
 | 
 
Kimberly McGuire 
 | 
 
Leave a comment

Today, we’d like to take the opportunity to spotlight a feature that’s been in our code base for some time, yet hasn’t been the subject of a blog post: the Python bindings for our Crazyflie firmware. You may have noticed it mentioned in previous blog posts, and now we’ll delve into more detail about what it is, how we and others are utilizing it, and what its future holds.

What are the Python bindings?
-----------------------------

Language bindings, in essence, are libraries that encapsulate chunks of code, enabling one programming language to interface with another. For instance, consider the project Zenoh. Its core library is crafted in Rust, but it offers bindings/wrappings for numerous other languages like Python, C/C++, and so on. This allows Zenoh’s API to be utilized in scripts or executables written in those languages. This approach significantly broadens the functionality without necessitating the rewriting of code across multiple programs. A case in point from the realm of robotics is ROS(1), which initially created all of their APIs for different languages from scratch—a maintenance nightmare. To address this, for ROS 2, they developed the primary functionality entirely in C and provided wrappers for all other programming languages. This strategy eliminates the need to ‘reinvent the wheel’ with each iteration.

Rather than redeveloping the firmware in Python, our esteemed collaborators Wolfgang Hönig and James Preiss took a pragmatic approach. They selected parts of the Crazyflie firmware and wrapped them for Python use. You can see the process in this ticket. This was a crucial step for the simulation of the original Crazyswarm (ROS1) project and was continued for its use in the Crazyswarm2 project, which is based on ROS 2. They opted for SWIG, a tool specifically designed to wrap C or C++ programs for use with higher-level target languages. This includes not only Python, but also C#, GO, Javascript, and more, making it the clear choice for implementing those bindings at the time. We also strongly recommend checking out a previous blogpost by Simon D. Levy, who used Haskell to wrap the C-based Crazyflie Firmware for C++.

Where are the Python bindings being used?
-----------------------------------------

As previously mentioned, the Crazyswarm1 & 2 projects heavily utilize Python bindings for testing key components of the firmware (such as the high-level commander, planner, and controller) and for a (hybrid) software-in-the-loop simulation. During the project’s installation, these Python bindings must be compiled so they can be used during simulation. This approach allows users to first test their trajectories in a simulated environment before deploying them on actual Crazyflies. The advantage is that minimal or no modifications are required to achieve the same results. While simulations do not perfectly mirror real-world conditions, they are beneficial because they operate with the same controller as the one used on the Crazyflie itself. In our own Crazyflie simulation in Webots, it’s also possible to use these same bindings in the simulator by following these instructions.

Three controllers (PID, Mellinger, and Brescianini), intra-drone collision avoidance, and the high-level commander planner have all been converted into Python bindings. Recently, we’ve added a new component: the Extended Kalman Filter (EKF). This addition is ideal as it allows us to test the filter with recorded data from a real Crazyflie and experiment with different measurement models. As we discussed in a previous blogpost, estimators are complex due to their dependence on chance and environmental factors. It’s beneficial for developers to have more control over the inputs and expected outputs. However, the EKF is deeply integrated into the interconnected processes within the Crazyflie Firmware. After a significant refactoring effort, these were added to the bindings by creating an EKF emulator (see this PR). This enabled Kristoffer to further enhance the TDOA outlier filter for the Crazyflie by emulating the full process of the EKF, including IMU data.

In addition to SITL simulation and EKF development, Python bindings are also invaluable for continuous integration. They enable comprehensive testing that encompasses not just isolated code snippets, but entire processes. For instance, if there’s a recording of a Crazyflie flight complete with sensor data (such as flow, height, and IMU data), and it’s supplemented with a recorded ground truth (from lighthouse/mocap), this sensor data can be fed into the EKF Python binding. We can then compare the outputted pose with the ground truth to verify accuracy. The same principle applies to the controllers. Consequently, if any changes are made to the firmware that affect these crucial aspects of Crazyflie flight, these tests can readily detect them.

If you like to try the python bindings tests for yourself, clone the Crazyflie-firmware repo and build/install the python bindings via these instructions. Make sure you are in the root of the repository and run: `python3 -m pytest test_python/`. Mind that you might need to put the bindings in the same path with `export PYTHONPATH=<PATH_TO_>/crazyflie-firmware/build:$PYTHONPATH` (please see this open ticket)

The next steps of the python bindings
-------------------------------------

We’ve seen how Python bindings have proven to be extremely useful, and we’re keen to further expand their application. At present, only the Loco positioning system has been incorporated into the EKF part of the Python bindings. Work is now underway to enable this for the Lighthouse system (see this draft PR). Incorporating the Lighthouse system will be somewhat more complex, but fortunately, much of the groundwork has already been laid, so we hope it won’t be too challenging. However, we have encountered issues when using the controller bindings with simulation (see this open ticket). It appears that some hardware-specific timing has been hardcoded throughout the PID controller in particular. Therefore, work needs to be done to separate the hardware abstraction from the code, necessitating additional refactoring work for the controller.

Recent projects like Sim\_CF2 (see this blogpost) and Crazysim (see this discussion thread) have successfully compiled the Crazyflie firmware to run as a standalone node on a computer. This allows users to connect it to the Crazyflie Python library as if it were an actual Crazyflie. This full Software-In-The-Loop (SITL) functionality, already possible with autopilot suites like PX4 and Ardupilot, is something we at Bitcraze are eager to implement as well. However, considering the extensive work required by the aforementioned SITL projects to truly separate the hardware abstraction layer from the codebase, we anticipate that refactoring the entire firmware will be a substantial task. We’re excited to see what we can achieve in this area.

Indeed, even with a more comprehensive Software-In-The-Loop (SITL) solution, there’s no reason to completely abandon Python bindings. For developments requiring more input/output control—such as the creation of a new controller or an addition to the Extended Kalman Filter (EKF)—it’s beneficial to start with just that portion of the firmware code. Python bindings and a SITL build can coexist, each offering its own advantages and disadvantages for different stages of the development process. By leveraging the tools at our disposal, we can minimize the risk of damaging Crazyflies during development. Let’s continue to make the most of these valuable resources!

 
Crazyflie, Frontpage, Simulation, Software, Testing 
  crazyflie, simulation