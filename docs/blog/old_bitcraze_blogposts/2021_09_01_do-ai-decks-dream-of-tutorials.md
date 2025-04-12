**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2021/09/do-ai-decks-dream-of-tutorials/](https://www.bitcraze.io/2021/09/do-ai-decks-dream-of-tutorials/)**

2021-09-20 
 | 
 
Kimberly McGuire 
 | 
 
Leave a comment

The AI-decks are back in stock! Also, last week we had our quarterly meeting, where we plan our focus for the next quarter. As it is also the start of the fiscal year, we also take this opportunity to update our 1 year and 3 year plans as well. We have a big plans coming up, but one of the important focuses that we will have this year, is to get the AI-deck out of early-access!

But what would be necessary for such a task? The AI-deck is one of the most complicated boards we have worked with, so do we have to evaluate its ‘out-of-readiness’ along the same standards than any of our other products.

Mega AIdeck Tutorial
--------------------

So one of our idea is to be able to achieve a state of the AIdeck in order to write a mega AIdeck tutorial series. This implies that we are able to show how somebody could go from a datasets all the way to a flying aideck-crazyflie combo. Such a series could consist of the following topics:

1. How to go from a dataset of images to a (Deep) Neural Network
2. Testing the DNN on the computer with the Image WiFi examples
3. Converting the neural network to Tensorflow Light (with basics on Edge AI and quantizing neural networks)
4. AIdeck basics (How to access the camera, how to add the network to the cluster, how to send commands)
5. Build and flashing the AIdeck and testing it out in the hand
6. Attach the AIdeck to the crazyflie, make an app-layer application to fly and react on the image input.

From the first look of it, this sounds like it should be easy to do right? Actually, there are still much to be done in order to make this tutorial possible.

Replumbing the Communication
----------------------------

One of the more challenging aspects of the AIdeck as it now is, is that users need to buy a JTAG-enabled programmer in order to flash the GAP8 and the NINA module of the AI-deck. That is the reason why currently the AIdeck has these 2 x 10 pin jtag connectors attached, but ideally we would want to get rid of it completely. This means is that we need to have over air flashing of the GAP8’s binary and that the intercommunication of the NINA and AIdeck will become even more important.

Moreover, the communication protocol from the GAP8 to the STM32 of the Crazyflie is currently very basic, as of right now, it is only possible to send single characters. It might work in some situations, but what if you would like to send an array of values back to the Crazyflie, like the collision probability & steering angle like in PULP platform’s implementation of Dronet? And, would we like to keep on using two UART serial ports or perhaps just relay both NINA and GAP8 communication all through one? The later will make it easier for us to maintain the crazyflie-aideck communication but can perhaps introduce communication delays.

These are just a slice of the type of re-plumbing work for the AIdeck before we can even start our dream tutorial series, but at least it will give you an idea of what we are dealing with :)

Rik the Intern
--------------

From this week we have the honor of hosting Rik Bouwmeester for a couple of months. He is currently doing his Master Thesis at the MAVlab from the faculty of Aerospace Engineering of the TU Delft. Since he has experience of working the AIdeck before, he will be able to provide us with some user perspective and help us with the above mentioned issues. You can expect a blogpost from him soon!

 
AI-deck, Frontpage, Random stuff