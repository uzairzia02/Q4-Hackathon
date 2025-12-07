# Feature Specification: Physical AI & Humanoid Robotics Course

**Feature Branch**: `002-create-tech-spec`
**Created**: 2025-12-07
**Status**: Draft
**Input**: User description: "Focus and Theme: AI Systems in the Physical World..."

## Clarifications

### Session 2025-12-07
- Q: Which specific Large Language Model (LLM) should be prioritized for the Vision-Language-Action (VLA) module and capstone project? → A: GPT-4
- Q: What is the defined learning path for a student who does not have access to the required "Digital Twin" RTX workstation? → A: Cloud-Based Access: Provide detailed instructions and configuration files for setting up equivalent environments on cloud platforms (e.g., AWS RoboMaker, NVIDIA Omniverse Cloud).
- Q: Should the project plan prioritize a cloud-based (High OpEx) or on-premise (High CapEx) lab infrastructure as the default recommendation for the shared lab robots? → A: Cloud-Based (High OpEx): Prioritize cloud-based instances for running simulations and virtual robots, with physical edge devices for deployment phase.

## 1. Core Focus: Embodied Intelligence

This project is a 13-week capstone course on **Physical AI**, guiding students from foundational AI concepts to controlling simulated and real-world humanoid robots. The primary goal is to bridge the gap between digital AI and physical embodiment.

**Learning Outcomes**:
- Master ROS 2 for robotic control.
- Simulate complex robots in Gazebo and NVIDIA Isaac Sim.
- Integrate voice commands and LLMs for cognitive planning (Vision-Language-Action).
- Deploy AI models to physical hardware (NVIDIA Jetson).

---

## 2. User Scenarios & Learning Modules *(mandatory)*

### User Story 1: Learning the Robotic Nervous System (Weeks 3-5)

A student learns the fundamentals of ROS 2 by creating nodes, topics, and services to control a simulated robot. They learn to bridge Python-based AI logic to robot controllers.

**Why this priority**: ROS 2 is the foundational middleware for the entire course.

**Independent Test**: A student can successfully launch a ROS 2 package they created, which moves a simple robot in a simulation.

**Acceptance Scenarios**:
1. **Given** a clean Ubuntu 22.04 environment, **When** a student follows the setup guide, **Then** they have a working ROS 2 Humble installation.
2. **Given** a simulated robot, **When** a student runs their ROS 2 node, **Then** the robot moves as programmed.

---

### User Story 2: Building a Digital Twin (Weeks 6-7)

A student learns to create and manipulate a simulated environment in Gazebo. They will load a humanoid robot's URDF file and test its physical properties.

**Why this priority**: Simulation is a critical step before deploying to expensive physical hardware.

**Independent Test**: A student can load a humanoid robot model into a custom Gazebo world where gravity and collisions are active.

**Acceptance Scenarios**:
1. **Given** the Gazebo simulator, **When** a student imports a humanoid URDF, **Then** the robot model appears correctly and is subject to physics.
2. **Given** a simulated environment, **When** a student applies a force to the robot, **Then** it reacts realistically (e.g., falls over).

---

### User Story 3: Training the AI Brain (Weeks 8-10)

A student uses NVIDIA Isaac Sim to generate synthetic data for training a perception model. They learn to use hardware-accelerated tools for SLAM and navigation.

**Why this priority**: This module connects AI model training directly to robotics.

**Independent Test**: A student can run a Nav2 simulation for a bipedal humanoid to navigate a simple maze.

**Acceptance Scenarios**:
1. **Given** Isaac Sim, **When** a student sets up a scene with a robot and objects, **Then** they can generate synthetic image data with labels.
2. **Given** a pre-trained model, **When** a student runs the Isaac ROS VSLAM node, **Then** the robot can map its environment.

---

### User Story 4: The Autonomous Humanoid Capstone (Weeks 11-13)

A student integrates all previous modules to complete the capstone project. They use voice commands to instruct a simulated humanoid to find and manipulate an object.

**Why this priority**: This is the culmination of the course, demonstrating mastery of all learning outcomes.

**Independent Test**: A student can say "get the red ball", and the simulated robot will navigate to the ball, pick it up, and bring it back.

**Acceptance Scenarios**:
1. **Given** a running simulation with the full environment, **When** a student speaks a valid command, **Then** OpenAI Whisper transcribes the command to text.
2. **Given** a text command, **When** the LLM planner receives the text, **Then** it generates a sequence of ROS 2 actions.
3. **Given** a sequence of actions, **When** the robot executes them, **Then** it successfully navigates, identifies the object, and manipulates it.

---

## 3. Hardware & Software Requirements *(mandatory)*

### 3.1. Student Workstation (Digital Twin Rig)
- **GPU**: NVIDIA RTX 4070 Ti (12GB VRAM) or higher.
- **CPU**: Intel Core i7 (13th Gen+) or AMD Ryzen 9.
- **RAM**: 64 GB DDR5.
- **OS**: Ubuntu 22.04 LTS (native or dual-boot).

### 3.1.1. Cloud-Based Alternative
For students without access to the required RTX workstation, the course MUST provide detailed instructions and configuration files for setting up equivalent environments on cloud platforms (e.g., AWS RoboMaker, NVIDIA Omniverse Cloud).

### 3.2. Student Edge AI Kit (Physical Brain)
- **Compute**: NVIDIA Jetson Orin Nano (8GB) or Orin NX (16GB).
- **Vision**: Intel RealSense D435i or D455.
- **Audio**: ReSpeaker USB Mic Array v2.0.

### 3.3. Lab Robot Hardware (Shared)
- **Primary**: Unitree Go2 Edu (as a proxy for humanoid locomotion).
- **Secondary**: Hiwonder TonyPi Pro (for bipedal kinematics exercises).
- **Stretch Goal**: Unitree G1 Humanoid (for direct capstone deployment).

### 3.3.1 Lab Infrastructure Default
The default recommendation for shared lab robot infrastructure is a **Cloud-Based (High OpEx)** approach. This prioritizes cloud-based instances for running simulations and virtual robots, with physical edge devices reserved for the final deployment phase.

### 3.4. Software Stack
- **Simulation**: Gazebo, NVIDIA Isaac Sim (Omniverse).
- **Robotics Middleware**: ROS 2 (Humble/Iron).
- **AI/ML**: PyTorch, NVIDIA TAO Toolkit.
- **VLA**: OpenAI Whisper, GPT-4.
- **Course Platform**: Docusaurus.
- **Backend Services**: FastAPI, Qdrant, Neon Postgres.
- **Authentication**: JWT-based authentication.

---

## 4. Supporting Features & Success Criteria

### 4.1. Learning Support System
- **FR-SUP-001**: The Docusaurus site MUST provide an embedded RAG chatbot trained on the course materials.
- **FR-SUP-002**: A suite of Gemini CLI agents MUST be available to assist with content creation, code examples, and translation to Urdu.
- **FR-SUP-003**: Student accounts (via JWT-based authentication) MUST be available to track progress and personalize examples based on the student's declared hardware profile.

### 4.2. Measurable Outcomes
- **SC-001**: At least 80% of students successfully complete the ROS 2 package development project.
- **SC-002**: At least 75% of students can successfully load and simulate a humanoid robot in Gazebo or Isaac Sim.
- **SC-003**: At least 70% of students successfully complete the final capstone project in simulation.
- **SC-004**: The supporting RAG chatbot correctly answers 85%+ of factual questions drawn from the course content.
- **SC-005**: All course content is available in both English and Urdu.
