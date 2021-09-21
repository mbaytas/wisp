# Wisp

*Drone-guided breathwork*

![image](https://user-images.githubusercontent.com/1661078/133905635-a8c8c75d-d044-445e-a5ed-cc29f1b67bbf.png)

Wisp is an experience design prototype built on a [Bitcraze Crazyflie 2.1](https://www.bitcraze.io/) micro-quadcopter drone and a [PLUX/BITalino respiration sensor](https://plux.info/).

By synchronizing its movements and lights the user's with breathing patterns, the drone can both lead and follow\* the breath in order to encourage, teach, guide, and augment breathwork. 

*\* Work in progress.*

The experience design is inspired and informed by how breathwork teachers work with children.

## Hardware

Drone parts from [Bitcraze](https://www.bitcraze.io/):

- Crazyfile 2.1
- Crazyradio PA
- LED Ring Deck
- Multi-ranger Deck
- Flow Deck v2
- Extra-long headers

Sensors from [PLUX](https://plux.info/content/9-about-us):

- biosignalsplux PZT respiration sensor
- BITalino (r)evolution Board

## Instructions

1. Drill a hole through the LED Ring Deck, as described in [this tutorial](https://www.hackster.io/krichardsson/light-paint-with-a-drone-d050af), in order to make it work with the Flow Deck. Assemble the drone.
2. Set up the Bitcraze and BITalino Python packages. (The Bitcraze GUI client is not needed.)
    - https://github.com/bitcraze/crazyflie-lib-python
    - https://github.com/BITalinoWorld/revolution-python-api
3. Place the drone on a flat surface and leave it still.
4. If you are going with the default settings, make sure you have only one Crazyflie turned on. 
5. Run: wisp.py

The drone will execute the following phases after establishing a connection with the script:

1. **Pre-flight reset.** The LED ring will turn off.
2. **Lift-off warning.** The drone will be still, and the LED ring will pulsate green.
3. **Lift-off.** The drone will be still, mid-air, and the LED ring will pulsate green.
4. **The breathing exercise.** Inhale as the drone rises. Hold as the drone holds. Exhale as the drone exhales. The LED ring will pulsate blue to give count.
5. **Denouement.** The drone will be still, mid-air, and the LED ring will pulsate green.
6. **Landing.** The LED ring will turn off.

![image](https://user-images.githubusercontent.com/1661078/133905716-d94cf82b-4945-4aab-a3fb-4b31a2e94cc7.png)

## Related Research Publications

Mafalda Gamboa, Mehmet Aydın Baytaş and Sara Ljungblad (2021). **Wisp: a Design Case for Temporality in Research through Design in Human-Robot Companionship**. Paper for the HRI '21 Workshop Research Through Design Approaches in Human-Robot Interaction (RTDxHRI). [\[PDF\]](https://www.baytas.net/research/pub/2021_HRI_Wisp.pdf)

Mafalda Gamboa, Mohammad Obaid, and Sara Ljungblad (2021). **Ritual Drones: Designing and Studying Critical Flying Companions**. Companion of the 2021 ACM/IEEE International Conference on Human-Robot Interaction. [\[ACM Digital Library\]](https://dl.acm.org/doi/abs/10.1145/3434074.3446363)
