**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2020/05/latest-update-on-the-ai-deck/](https://www.bitcraze.io/2020/05/latest-update-on-the-ai-deck/)**

2020-05-25 
 | 
 
Kimberly McGuire 
 | 
 
2 Comments

It has been a while since we have updated you all on the AI deck. The last full blogpost was in October, with some small updates here and there. It is not that we have not focused on it at all; on the contrary… this has been a high priority project for a while now. It is just quite a complex board with a lot of bells and whistles, which can be challenging to work with sometimes so early in development, something that our previous intern can definitely agree on. So therefore we rather wanted to wait until we were able to make sufficient progress before we gave you an update… and so we have!

A Crazyflie 2.1 with the AI deck

Together with Greenwaves technologies we have been trying to get the SDK of the GAP8 chip on the AI deck stable enough for an early release. The latest release of the SDK (version 3.4) has proved itself to work with relative ease on the AI deck after extensive testing. Currently it is possible to use OpenOCD for flashing and debugging, and it supports most commonly available debuggers with a jtag connector. In the upcoming weeks both of Bitcraze and Greenwaves will test and try out all examples of the SDK on the AI deck to make sure that everything is still compatible. Also the documentation will be extended as well. As there is so much to document, it might be difficult to catch all of it. However, if you notify us and Greenwaves on anything that is missing once the AIdeck is out, that will help us out to catch the knowledge gaps.

The AI deck also contains the ESP-based NINA module for establishing a WiFi connection. This enables the users to stream the video stream of the AI deck onto their computers, which will be quite an essential tool if they would like to generate their own image database for training the CNNs for the GAP8 (and it happens to also be quite practical for debugging by the way!). Currently it is required to set credentials of your local WiFi network and reflash the AI-deck to be able to connect and streaming the images, but we are working on turning the Nina into an access-point instead so no reflashing would be required. We hope that we will be able to implement this before the release.

Top view of the AI deck

We are also trying out to adjust applications to make suitable of the AI deck. For instance, we have adapted Greenwaves’ face-detector example to use the image streamer instead of the display available on the GAPuino boards. You can see a video of the result here underneath. Beware that this face-detector is not based on a CNN but on HOG descriptors, so it only works in good conditions where the face is well lit. However, it is possible to train a CNN to detect faces in Tensorflow and flash this on the AI deck with the GAPflow framework as developed by Greenwaves. At Bitcraze we haven’t managed to try that out ourselves ( we are close to that though!) but at least this example is a nice demonstration of the AI deck’s abilities together with the WiFi-streamer. This example and more testing code can be found in our experimental repo here. For examples of GAPflow, please check out the *examples/NNtool* section of the GAP8 SDK.

*For some reason WordPress has difficulty embedding the video that was supposed to be here, so please check https://youtu.be/0sHh2V6Cq-Q*

Seeing how the development has been progressing, we will be comfortable to say that the AI deck could be ready for early release somewhere in the next month, so please keep an eye out on our website! We will continue to test the GAP SDK’s stability and we are very thankful for Greenwaves Technologies with their help so far. We will also work on getting-started guides in order to get acquainted with the AI deck, supplementing the already existing documentation about the GAP8 chip.

Even-though the AI deck will soon be ready for early release, this piece of hardware is not for the faint-hearted and embedded programming experience is a **must**. But keep in mind that the possibilities with the AI deck are huge, as it will be mean that super-edge-computing on a 30 gram flying platform will be available for anyone. It will all be worth it when you have your Crazyflie flying autonomously while being able to recognize its surroundings :)

 
AI-deck, Crazyflie, Electronic, Frontpage, Random stuff, Software, Video