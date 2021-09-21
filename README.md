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
4. Make sure you have only one Crazyflie turned on. (Unless you know what you're doing, and have configured things properly.)
5. In wisp.py, select the "exercise" you'd like to execute by commenting out the others in the script body. (It is possible to "chain" exercises.)
6. In wisp.py, if a BITalino-connected exercise is selected, make sure the line which establishes the connection (`bt_connect()`) is **not** commented out. Conversely, if a BITalino-connected exercise is **not** selected, make sure that the BITalino connection call is commented out.
7. Run wisp.py

The drone will execute the following phases after establishing a connection with the script:

2. **Pre-flight reset.** The LED ring will turn off.
3. **Lift-off warning.** The drone will be still, and the LED ring will pulsate green.
4. **Lift-off.** The drone will be still, mid-air, and the LED ring will pulsate green.
5. **The breathing exercise.** Inhale as the drone rises. Hold as the drone holds. Exhale as the drone exhales. The LED ring will pulsate blue to give count.
6. **Denouement.** The drone will be still, mid-air, and the LED ring will pulsate green.
7. **Landing.** The LED ring will turn off.

## Features, Settings, tips

### wisp.py

- **Settings > `cf_zMin` (m):** Minimum flight altitude.
- **Settings > `cf_zMax` (m):** Maximum flight altitude
- **Settings > `ts` (s):** "Time stretch" factor. Specifies how many seconds each "count" lasts, thus determining the pace of breathwork. The "global" time stretch factor `ts` that is adjusted in the script settings affects all drone actions outside of the breathing exercise. The exercise functions take `ts` as a keyword arguments with their own defaults. For optimal experience, we recommend setting `ts` in the settings and passing it to the exercise functions.

### exercises.py

Breathing exercises are performed to a count. Each breathing exercise provided in the script has a count and local time stretch factor (see above) specified via keyword arguments, hence they all have defaults while also being adjustable. Each exercise also has a `n` keyword argument which specifies how many cycles will be performed.

Example: `water_breathing(cf, mr, z_min, z_max, count=4.0, ts=3.0, n=3)` corresponds to 3 inhale/exhale cycles, each consisting of a 12-second inhale and 12-second exhale (4 counts of 3 seconds = 12 seconds).

*Exercises are under development, documentation TBC. Please see source and docstrings.*

![image](https://user-images.githubusercontent.com/1661078/133905716-d94cf82b-4945-4aab-a3fb-4b31a2e94cc7.png)

### helpers.py

*Documentation TBC. Please see source and docstrings.*

## Related Research Publications

Mafalda Gamboa, Mehmet Aydın Baytaş and Sara Ljungblad (2021). **Wisp: a Design Case for Temporality in Research through Design in Human-Robot Companionship**. Paper for the HRI '21 Workshop Research Through Design Approaches in Human-Robot Interaction (RTDxHRI). [\[PDF\]](https://www.baytas.net/research/pub/2021_HRI_Wisp.pdf)

Mafalda Gamboa, Mohammad Obaid, and Sara Ljungblad (2021). **Ritual Drones: Designing and Studying Critical Flying Companions**. Companion of the 2021 ACM/IEEE International Conference on Human-Robot Interaction. [\[ACM Digital Library\]](https://dl.acm.org/doi/abs/10.1145/3434074.3446363)

## Kind of Related Research Publications

Sara Ljungblad, Yemao Man, Mehmet Aydın Baytaş, Mafalda Samuelsson-Gamboa, Mohammad Obaid, & Morten Fjeld (2021). **What Matters in Professional Drone Pilots’ Practice? An Interview Study to Understand the Complexity of Their Work and Inform Human-Drone Interaction Research**. In Proceedings of the 2021 CHI Conference on Human Factors in Computing Systems (CHI ’21). [\[PDF\]](https://www.baytas.net/research/pub/2021_CHI?Professional.pdf)

Joseph La Delfa, Mehmet Aydın Baytaş, Nick Huppert, & Ian Peake, Leah Heiss (2020). **Using Pose Estimation for Cultivating Subtleties in Human-Drone Interaction**. Paper for the NordiCHI ‘20 workshop Programming for Moving Bodies. [\[PDF\]](https://www.baytas.net/research/pub/2020_NordiCHI_WS_HDI.pdf)

Mehmet Aydın Baytaş, Markus Funk, Sara Ljungblad, Jérémie Garcia, Joseph La Delfa, & Florian ‘Floyd’ Mueller (eds.) (2020). **Proceedings of the Interdisciplinary Workshop on Human-Drone Interaction**. [\[Proceedings\]](http://ceur-ws.org/Vol-2617/)

Joseph La Delfa, Mehmet Aydın Baytaş, Emma Luke, Ben Koder, & Florian ‘Floyd’ Mueller (2020). **Designing Drone Chi: Unpacking the Thinking and Making of Somaesthetic Human-Drone Interaction**. In Proceedings of the 2020 Conference on Designing Interactive Systems (DIS ‘20). [\[PDF\]](https://www.baytas.net/research/pub/2020_DIS_Drone_Chi.pdf)

Joseph La Delfa, Mehmet Aydın Baytaş, Rakesh Patibanda, Hazel Ngari, Rohit Ashok Khot, & Florian ‘Floyd’ Mueller (2020). **Drone Chi: Somaesthetic Human-Drone Interaction**. In Proceedings of the 2020 CHI Conference on Human Factors in Computing Systems (CHI ’20). **\[Honourable Mention Award\]**  
[\[PDF\]](https://www.baytas.net/research/pub/2020_CHI_Drone_Chi.pdf)

Mehmet Aydın Baytaş, Markus Funk, Sara Ljungblad, Jérémie Garcia, Joseph La Delfa, & Florian ‘Floyd’ Mueller (2020). **iHDI 2020: Interdisciplinary Workshop on Human-Drone Interaction**. In Extended Abstracts of the 2020 CHI Conference on Human Factors in Computing Systems (CHI EA ‘20). [\[PDF\]](https://www.baytas.net/research/pub/2020_CHI_EA_iHDI.pdf)

Mehmet Aydın Baytaş, Sara Ljungblad, Joseph La Delfa, & Morten Fjeld (2020). **Agent Archetypes for Human-Drone Interaction: Social Robots or Objects with Intent?**. In Proceedings of the Interdisciplinary Workshop on Human-Drone Interaction (iHDI 2020). [\[PDF\]](https://www.baytas.net/research/pub/2020_iHDI_Agent.pdf)

Mehmet Aydın Baytaş, Damla Çay, Yuchong Zhang, Mohammad Obaid, Asım Evren Yantaç, & Morten Fjeld (2019). **The Design of Social Drones: A Review of Studies on Autonomous Flyers in Inhabited Environments**. In Proceedings of the 2019 CHI Conference on Human Factors in Computing Systems (CHI ’19). [\[PDF\]](https://www.baytas.net/research/pub/2019_CHI_Drones.pdf)

Joseph La Delfa, Mehmet Aydın Baytaş, Olivia Wichtowski, Rohit Ashok Khot, & Florian ‘Floyd’ Mueller (2019). **Are Drones Meditative?**  
In Extended Abstracts of the 2019 CHI Conference on Human Factors in Computing Systems (CHI EA ‘19). [\[PDF\]](https://www.baytas.net/research/pub/2019_CHI_EA_Meditative.pdf)

Mehmet Aydın Baytaş, Mohammad Obaid, Joseph La Delfa, Asım Evren Yantaç, & Morten Fjeld (2019). **Integrated Apparatus for Empirical Studies with Embodied Autonomous Social Drones**. In Proceedings of the International Workshop on Human-Drone Interaction (iHDI). [\[PDF\]](https://www.baytas.net/research/pub/2019_CHI_WS_iHDI_Apparatus.pdf)
