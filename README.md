# Introduction_to_Integrated_Robotics_slot_18
A repository containing all the materials for the PESU IO course Introduction to Integrated Robotics

## Dual Booting System with Ubuntu 22.04

To dual boot your systems please refer to this youtube link:
https://www.youtube.com/watch?v=UmPL54WKlaU&ab_channel=Buzz2dayTech

Ubuntu 22.04 iso download link:
https://releases.ubuntu.com/jammy/

## Installation

### Arduino IDE 2
Refer this link:
https://www.arduino.cc/en/software
Please download the zip file and extarct it on your ubuntu desktop.

### ROS2 Humble
Refer this link:
https://docs.ros.org/en/humble/Installation.html

### Gazebo 
Open terminal and run:
```bash
sudo apt-get install gazebo11
```
Check the installation:
```bash
gazebo
```

### Rviz
Usualy installed with ROS2 packages, run the command below to check:
```bash
rviz2
```

## Robot Simulation

Open Terminal and run the below commands:

1. **Creating your workspace**
   ```bash
   mkdir -p ~/iir_ws/src
   ```
   
2. **Cloning this Repository**
   ```bash
   cd ~/iir_ws/src
   git clone https://github.com/Varchasvin10/Introduction_to_Integrated_Robotics_slot_18.git
   ```
   FOLLOW THE STEPS TOLD BY SME'S HERE!!

3. **Building your workspace**
   ```bash
   cd
   cd ~/iir_ws
   colcon build
   ```

   Usually there wont be robot localization node downloaded.
   We can download it using this command
   ```bash
   sudo apt-get install ros-humble-robot-localization
   ```

5. **Running Rviz and Gazebo Simulation**
   First we have to source our workspace:
   ```bash
   source install/setup.bash
   ```
   Launching the Simulation in Rviz and Gazebo:
   ```bash
   ros2 launch iir display.launch.py
   ```
   To run only Gazebo:
   ```bash
   ros2 launch iir gz.launch.py
   ```

6. **Using Teleop keys to control the simulated robot**
   ```bash
   ros2 run teleop_twist_keyboard teleop_twist_keyboard
   ```

