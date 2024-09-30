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

### Installing ESP32 package in Arduino IDE
Refer this link:
https://randomnerdtutorials.com/installing-the-esp32-board-in-arduino-ide-windows-instructions/

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
   To run only Rviz:
   ```bash
   ros2 launch iir rviz.launch.py
   ```
   To run only Gazebo:
   ```bash
   ros2 launch iir gz.launch.py
   ```

7. **Using Teleop keys to control the simulated robot**
   ```bash
   ros2 run teleop_twist_keyboard teleop_twist_keyboard
   ```

## Simulation in a world

Open Terminal and run the below commands:

1. **Source our workspace**
   ```bash
   cd iir_ws
   source install/setup.bash
   ```

2. **Launch the world**
   ```bash
   ros2 launch iir factory.launch.py
   ```

3. **Now we spawn the robot in the world**
   ```bash
   ros2 launch iir robot.launch.py
   ```

4. **Using Teleop keys to control the simulated robot**
   ```bash
   ros2 run teleop_twist_keyboard teleop_twist_keyboard
   ```   

## Integrating ESP32 with ROS2 Humble

### Micro ROS Installation:

Open up terminal and run the following command:

1. Source the workspace:
   ```bash
   source /opt/ros/humble/setup.bash
   ```

2. Edit ~/.bashrc:
   ```bash
   gedit ~/.bashrc
   ```
   Add this line in the file:
   ```bash
   source /opt/ros/humble/setup.bash
   ```

3. Create a workspace:
   ```bash
   cd
   mkdir microros_ws
   cd microros_ws
   mkdir src
   ```

4. Clone Micro ROS from github:
   ```bash
   cd
   cd microros_ws/src
   git clone -b $ROS_DISTRO https://github.com/micro-ROS/micro_ros_setup.git src/micro_ros_setup
   ```

5. Install rosdep:
   ```bash
   cd
   sudo apt install python3-rosdep2
   ```

6. Update and Install other dependencies:
   ```bash
   sudo apt update && rosdep update
   rosdep install --from-paths src --ignore-src -y
   sudo apt-get install python3-pip
   ```

7. Build micro_ros tool and source them:
   ```bash
   cd microros_ws
   colcon build
   source install/setup.bash
   ```

8. Install Micro ROS agent:
   ```bash
   ros2 run micro_ros_setup create_agent_ws.sh
   # Build step
   ros2 run micro_ros_setup build_agent.sh
   ```

### Installing micro_ros for arduino ide:
Refer to this link:
https://github.com/micro-ROS/micro_ros_arduino/releases

### Running Micro ros agent on the ESP32:

Connect the esp32 to your device and run this command:
```bash
cd microros_ws
source install/setup.bash
ros2 run micro_ros_agent micro_ros_agent serial --dev /dev/ttyACM0
```
