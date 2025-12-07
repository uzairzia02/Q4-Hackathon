#!/bin/bash

# This script automates the setup of the development environment.
# It is intended for use on Ubuntu 22.04 LTS.

# Update package lists
sudo apt update
sudo apt upgrade -y

# Install ROS 2 Humble
echo "Installing ROS 2 Humble..."
sudo apt install -y software-properties-common
sudo add-apt-repository universe
sudo apt update && sudo apt install curl -y
sudo curl -sSL https://raw.githubusercontent.com/ros/rosdistro/master/ros.key -o /usr/share/keyrings/ros-archive-keyring.gpg
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/ros-archive-keyring.gpg] http://packages.ros.org/ros2/ubuntu $(. /etc/os-release && echo $UBUNTU_CODENAME) main" | sudo tee /etc/apt/sources.list.d/ros2.list > /dev/null
sudo apt update
sudo apt upgrade -y
sudo apt install -y ros-humble-desktop

# Install Gazebo
echo "Installing Gazebo..."
sudo apt-get install -y ignition-fortress

# Install Python tools
echo "Installing Python tools..."
sudo apt install -y python3-pip python3-venv

echo "Setup complete. Please source ROS 2 setup file:"
echo "source /opt/ros/humble/setup.bash"
