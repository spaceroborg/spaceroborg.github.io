**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2020/07/ai-deck-sees-in-color/](https://www.bitcraze.io/2020/07/ai-deck-sees-in-color/)**

2020-07-13 
 | 
 
Kimberly McGuire 
 | 
 
Leave a comment

It has been about a month since the AI-deck became available in Early Access. Since then there are now quite a few of you that own an AI-deck yourself. A new development we would like to share: we thought before that we had selected a gray-scale image sensor. However, it came to our attention that the camera actually contains a *color image sensor*, which on second viewing of the video presented in this blogpost is pretty obvious in hindsight (thanks PULP project ETH Zurich for letting us know!).

A color image from the AI-deck

This came as a little surprise, but a color camera can also add some new possibilities, like making the Crazyflie follow a orange ball, or also train the CNNs incorporate color in their classification training as well. The only thing is that it will require an extra preprocessing task in order to retrieve the color image, which will be explained in the next section.

Demosaicing
-----------

Essentially all CMOS image sensors are gray-scale by definition. In order to retrieve color from a scene, manufacturers add a Bayer filter on top of the image sensor, so it filters out the red, green and blue on each pixels. This Color filter array does not need to be RGB, but all kinds of colors, but we will only talk about the Bayer filter. If the pattern of the filter is known, the pixels that related to a certain color will be interpolated with each-other in order to fill in the gaps in between. This process is called demosaicing and it creates the RGB channels that are converted to a color image.

Process of demosaicing with a Bayer filter

Currently we only implemented a simple nearest-neighbor interpolation scheme for demosaicing, which is fine for demonstration purposes, however is not the best technique out there. Such a simple interpolation is not very ‘edge and detail’ aware and can therefore cause artifacts, like these Moiré effects seen here below. Anyway, we are still experimenting how to get a better image and how to translate that to all the examples of the AI-deck example repository (see this issue if you would like to follow or take part in the discussion).

Moiré effect

So technically, once we have the color image, this can be converted to a gray-scale images which can be used for the examples as is. However, there is a reduction in quality since the full pixel resolution is not used for obtaining the full scale image. We are currently discussing if it would be useful to get the gray-scale version of this camera and make this available as well, **so let us know if you would be interested!**

Feedback and Early Access
-------------------------

Like we said before, there now quite a few of you out there that have an AI-deck in their procession. As it is in Early Access, the software part is still in full development. However, since we have not received any negative feedback of you, we believe that everything is fine and peachy!

Just kidding ;) we know that the AI-deck is quite a challenging deck to work with and we know for sure that many of you probably have questions or have something to say about working with it. Buying an Early Access product also comes with a little bit of responsibility. The more feedback we get from you guys, the more we can tailor the software and support to help you and others, thereby advancing the product forward and getting it out of the early access phase.

So please, let us know if you are having any trouble starting up by posting a thread on the forum (we have a special AI-deck group!). If there are any issues with the examples or the documentation of the AI-deck repo. We and also our collaborators at Greenwaves Technologies (from the GAP8 chip) are more than happy to help out. That is what we are here for :)

 
AI-deck, Crazyflie, Electronic, Frontpage, Software