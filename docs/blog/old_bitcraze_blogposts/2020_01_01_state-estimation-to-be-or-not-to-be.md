**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2020/01/state-estimation-to-be-or-not-to-be/](https://www.bitcraze.io/2020/01/state-estimation-to-be-or-not-to-be/)**

2020-01-20 
 | 
 
Kimberly McGuire 
 | 
 
2 Comments

How does a Crazyflie manage to fly and stay in the air in the first place? Many of us tend to take this for granted as much research tend to happen on the application level. Although we try to make the low level elements of flight as stable as possible, it might happen that whatever you are trying to implement on the application level actually effects the Crazyflie on the low level controls and estimation. We therefore would like to focus a little bit on the inner-workings of the autopilot of the Crazyflie, starting with *state estimation.* The state estimation is part of the stabilizer loop in the Crazyflie, an overview of is was made in a previous blog post.

State estimation is really important in quadrotors (and robotics in general). The Crazyflie needs to first of all know in which angles it is at (roll, pitch, yaw). If it would be flying at a few degrees slanted in roll, the crazyflie would accelerate into that direction. Therefore the controller need to know an good estimate of current angles’ state and compensate for it. For a step higher in autonomy, a good position estimate becomes important too, since you would like it to move reliably from A to B.

There are two types of state estimators in the crazyflie firmware, namely a *Complementary Filter* and *an Extended Kalman Filter*.

#### Complementary Filter

The complementary filter is consider a very lightweight and efficient filter which in general only uses the IMU input of the gyroscope (angle rate) and the accelerator. The estimator has been extended to also include input of the ToF distance measurement of the Zranger deck. The estimated output is the Crazyflie’s attitude (roll, pitch, yaw) and its altitude (in the z direction). These values can be used by the controller and are meant to be used for manual control. If you are curious how this code is implemented exactly, we encourage you to checkout the firmware in estimator\_complementary.c and sensfusion6.c. The complementary filter is set as the *default* state estimator on the Crazyflie firmware.

Schematic overview of inputs and outputs of the Complementary filter.

#### Extended Kalman Filter

The (extended) Kalman filter is an step up in complexity compared to the complementary filter, as it accepts more sensor inputs of both internal and external sensors. It is an recursive filter that estimates the current state of the Crazyflie based on incoming measurements (in combination with a predicted standard deviation of the noise), the measurement model and the model of the system itself. We will not go into detail on this but we encourage people to learn more about (extended) Kalman filters by reading up some material like this.

Schematic overview of inputs and outputs of the Extended Kalman Filter

Shortly said, because of the more state estimation possibilities, we preferred the Kalman filter in combination with several decks: Flowdeck, Loco positioning deck and the lighthouse deck. If you look in the deck driver firmware (like for instance this one), you see that we set the required estimator to be the Kalman and that is of course because we want position/velocity estimates :). Important though is that each input of the measurement effects the quality of the position, as positioning of the Lighthouse deck (mm precision) is much more accurate that the loco positioning deck (cm precision), which has all to do with the standard deviation of the measurement of those values. Please check out the content of estimator\_kalman.c and kalman\_core.c to know more about the implementation. Also good to know that the Kalman filter has an supervisor, which resets if the position or velocity estimate is gets out of hand.

Of course this blogpost does not show the full detailed explanation of state estimation, but we do hope that it gives some kind of overview so you know where to look if you would like to improve anything. The Kalman filter can easily be extended to accept more inputs, or the models on which the estimates are based can be improved. If you would like implement your own filter, that would be perfectly possible to do so too.

It would be great if you guys could share your thoughts and questions about the state estimation on the crazyflie on the forum!

 
Crazyflie, Frontpage, Software