**This is a placeholder for the original blogpost to be found here: [https://www.bitcraze.io/2021/05/lighthouse-positioning-accuracy/](https://www.bitcraze.io/2021/05/lighthouse-positioning-accuracy/)**

2021-05-17 
 | 
 
Kimberly McGuire 
 | 
 
Leave a comment

Now that the Lighthouse deck is out of early access and we have made it easier to setup a lighthouse positioning system, we are currently at the next stage: showing how awesome it is! We feel that there are not enough people out there that know about the Lighthouse positioning system and sometimes confuse it even with the Loco position system (to be honest, the abbreviation *LPS* makes it challenging). But we are confident that the Lighthouse system is a good alternative for those that want to do drone research but are on a tight budget.

The area of the data collection. from the paper

Lighthouse Dataset
------------------

During Wolfgang Hönig‘s time here at Bitcraze, one of the bigger projects we worked together on was to generate a dataset comparing the positioning quality of the Lighthouse system with a Motion Capture (MoCap) system. You could imagine that would be a difficult task, since as the lighthouse basestations transmit infrared light sweeps and MoCap cameras by default also emit IR light which are reflected back by markers. However, with the Active marker deck for the Qualysis system, we were able to use the MoCap and Lighthouse positioning without too much interference.

Moreover, Wolfgang also helped out with improving the logging quality on the Micro-SD-card deck which also enabled us to get as much data real-time as possible. He wrote a blogpost about event-based logging a few weeks ago which is a new approach to record data on the Crazyflie at a fast pace. With the Active Marker Deck, the Micro-SD-card deck and of course the Lighthouse deck, … the Crazyflie turn into a full-blown positioning data-collection machine!

The configuration of the Crazyflie with the Micro-SD-card deck, the Lighthouse-deck from the lighthouse dataset paper

Paper
-----

About this whole process, we wrote the following paper:   
 Lighthouse Positioning System: Dataset, Accuracy, and Precision for UAV Research,   
 *A.Taffanel, B. Rousselot, J. Danielsson, K. McGuire, K. Richardsson, M. Eliasson, T. Antonsson, W. Hönig, ICRA Workshop on Robot Swarms in the Real World*, Arxiv *2021*

This paper contains an short explanation of the lighthouse system, how we set up the data collection and an analysis of the results, where we compared both Lighthouse V1 and V2 with the Crossing beam (C.B.) method and the extended Kalman filter. In all cases, the mean and median Euclidean error of the Lighthouse positioning system are about 2-4 centimeters compared to our MoCap system as ground truth.

Check out the lighthouse dataset paper to read all the details of the experiments!

The Euclidean Error of both LH1 and LH2 with Mocap as ground-truth taken from the dataset paper.

ICRA Swarm Workshop
-------------------

Our paper is selected for a poster presentation at the ICRA 2021 Workshop: Robot Swarms in the Real World. So if you have any questions about the paper, please join and ask us in person! The workshop will be held on the **4th of June**.

Moreover, we also are sponsoring the event by giving away a Lighthouse Swarm Bundle to whomever wins the best video-demonstration award! So to all the participants, the best of luck! We are super curious to what you’ll have to show us.

 
Crazyflie, Electronic, Frontpage, Lighthouse, Random stuff