# Drone-simluation

Experimenting with reinforcement learning for drone control. 

KICAD schematics in drone_controller folder.
OpenAI gym environment in gym_multirotor folder.


## Installation

Install mujuco:
https://github.com/google-deepmind/mujoco (Download latest release and extract in ~/.mujoco/)


Install packages:
```
pip install -r requirements.txt
```
Run main to train the hovering agent.
```
python main.py
```


TODO simulation:
- [ ] Add sensor/reward information in Mujoco interface when rendering
- [ ] Add noise to sensor information
- [ ] Add noise (wind, etc.) to simulation
- [ ] Model GPS, IMU, Compass sensor in Env

TODO Drone:
- [ ] Route PCB
- [ ] Firmware