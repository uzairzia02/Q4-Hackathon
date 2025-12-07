# Tasks: Physical AI & Humanoid Robotics Course

**Input**: Design documents from `specs/002-create-tech-spec/`
**Prerequisites**: plan.md, spec.md, data-model.md, contracts/

---

## Phase 0: Project Setup and Infrastructure (Week 1)

**Purpose**: Establish a robust foundation for the project, including repository setup, Docusaurus initialization, and development environment configuration.

- [x] T001 Initialize GitHub repository with MIT license and a comprehensive README.md.
- [x] T002 Set up `.gitignore` for Node.js, Python, and OS-specific files.
- [x] T003 Create `CONTRIBUTING.md` with contribution guidelines and code of conduct.
- [ ] T004 Set up branch protection rules for the `main` branch.
- [x] T005 Configure GitHub Actions for CI/CD in `.github/workflows/deploy.yml`.
- [x] T006 Create issue and pull request templates in `.github/`.
- [x] T007 [P] Initialize Docusaurus v3 project with TypeScript in `frontend/`.
- [x] T008 [P] Configure `frontend/docusaurus.config.ts` with site metadata (title, tagline, URL).
- [x] T009 [P] Customize Docusaurus theme with dark mode support in `frontend/src/css/custom.css`.
- [x] T010 [P] Configure `frontend/sidebars.js` with the 4-module course structure.
- [x] T011 [P] Create initial landing page in `frontend/src/pages/index.mdx`.
- [x] T012 [P] Initialize FastAPI project in `backend/`.
- [x] T013 [P] Set up Docker Compose for Qdrant and Neon Postgres in `docker-compose.yml`.
- [x] T014 Document hardware requirements for workstations and Jetson kits in `frontend/docs/getting-started/hardware.mdx`.
- [x] T015 Document software setup (Ubuntu, ROS 2, Gazebo, Isaac Sim) in `frontend/docs/getting-started/software-setup.mdx`.
- [x] T016 Create a setup script (`scripts/setup_env.sh`) for automating environment configuration.

---

## Phase 1: Module 1 - ROS 2 Fundamentals (Weeks 2-5) [US1]

**Goal**: Cover ROS 2 foundations, architecture, topics, services, actions, and URDF for humanoid robots.
**Independent Test**: A student can build and run a complete publisher-subscriber system and visualize a humanoid robot model in RViz2.

- [x] T017 [US1] Write Chapter 1: Introduction to Physical AI in `frontend/docs/module1/intro-physical-ai.mdx`.
- [x] T018 [US1] Create 3-5 diagrams for Chapter 1 illustrating core concepts. # MANUAL_TASK
- [x] T019 [US1] Write Chapter 2: ROS 2 Architecture in `frontend/docs/module1/ros2-architecture.mdx`.
- [x] T020 [US1] [P] Create Python examples for ROS 2 nodes and topics in `code_examples/ros2/module1/`.
- [x] T021 [US1] Write Chapter 3: ROS 2 Services & Actions in `frontend/docs/module1/ros2-services-actions.mdx`.
- [x] T022 [US1] [P] Create Python examples for ROS 2 services and actions in `code_examples/ros2/module1/`.
- [x] T023 [US1] Write Chapter 4: URDF for Humanoid Robots in `frontend/docs/module1/urdf-for-humanoids.mdx`.
- [x] T024 [US1] [P] Create a sample humanoid URDF file in `code_examples/ros2/module1/`.
- [x] T025 [US1] Implement `colcon` tests for all ROS 2 example packages in `code_examples/ros2/module1/tests/`.

---

## Phase 2: Module 2 - Digital Twin Simulation (Weeks 6-7) [US2]

**Goal**: Cover simulation in Gazebo and sensor simulation.
**Independent Test**: A student can build a custom Gazebo environment and spawn a humanoid robot with simulated sensors.

- [x] T026 [US2] Write Chapter 5: Gazebo Simulation Environment in `frontend/docs/module2/gazebo-simulation.mdx`.
- [x] T027 [US2] [P] Create Gazebo world and model examples in `code_examples/gazebo/module2/`.
- [x] T028 [US2] Write Chapter 6: Sensor Simulation in Gazebo in `frontend/docs/module2/sensor-simulation.mdx`.
- [x] T029 [US2] [P] Create examples for simulating LiDAR, depth cameras, and IMUs in `code_examples/gazebo/module2/`.

---

## Phase 3: Module 3 - NVIDIA Isaac Platform (Weeks 8-10) [US3]

**Goal**: Cover Isaac Sim, Isaac ROS for perception, and Nav2 for bipedal navigation.
**Independent Test**: A student can deploy VSLAM on a Jetson Orin and navigate a simulated robot in Isaac Sim.

- [x] T030 [US3] Write Chapter 7: NVIDIA Isaac Sim Fundamentals in `frontend/docs/module3/isaac-sim-fundamentals.mdx`.
- [x] T031 [US3] [P] Create Isaac Sim examples for synthetic data generation in `code_examples/isaac_sim/module3/`.
- [x] T032 [US3] Write Chapter 8: Isaac ROS for Perception in `frontend/docs/module3/isaac-ros-perception.mdx`.
- [x] T033 [US3] [P] Create Isaac ROS examples for VSLAM and object detection in `code_examples/isaac_ros/module3/`.
- [x] T034 [US3] Write Chapter 9: Nav2 for Bipedal Navigation in `frontend/docs/module3/nav2-bipedal.mdx`.
- [x] T035 [US3] [P] Create Nav2 configuration and code examples in `code_examples/nav2/module3/`.

---

## Phase 4: Module 4 & Capstone (Weeks 11-13) [US4]

**Goal**: Cover VLA, cognitive planning, and integrate all concepts into a final capstone project.
**Independent Test**: A student can issue a voice command and see the simulated robot execute a multi-step task.

- [x] T036 [US4] Write Chapter 10: Voice Commands with OpenAI Whisper in `frontend/docs/module4/voice-commands-whisper.mdx`.
- [x] T037 [US4] [P] Create Python examples for Whisper API integration in `code_examples/openai/module4/`.
- [x] T038 [US4] Write Chapter 11: Cognitive Planning with GPT-4 in `frontend/docs/module4/cognitive-planning-gpt4.mdx`.
- [x] T039 [US4] [P] Create Python examples for GPT-4 API integration for cognitive planning in `code_examples/openai/module4/`.
- [x] T040 [US4] Write Chapter 12: Capstone Project - Autonomous Humanoid in `frontend/docs/capstone/`.
- [x] T041 [US4] [P] Provide complete, commented source code for the capstone project in `code_examples/capstone/`.
- [x] T042 [US4] Create a video demonstration of the working capstone project. # MANUAL_TASK

---

## Phase 5: Supporting Features & QA (Parallel Weeks)

**Purpose**: Develop supporting features and perform ongoing quality assurance.

- [x] T043 [P] [SUPPORT] Implement RAG chatbot service and API endpoint in `backend/src/services/rag.py` and `backend/src/api/chat.py`.
- [x] T044 [P] [SUPPORT] Create and integrate the Chatbot UI component in `frontend/src/components/Chatbot.tsx`.
- [x] T045 [P] [SUPPORT] Implement JWT-based authentication service in `backend/src/services/auth.py`.
- [x] T046 [P] [SUPPORT] Implement user profile API endpoints in `backend/src/api/users.py`.
- [x] T047 [P] [SUPPORT] Create User Profile UI and progress tracking components in `frontend/src/components/`.
- [x] T048 [P] [SUPPORT] Develop Gemini CLI agents for content generation and translation in `.gemini/agents/`.
- [x] T049 [P] [SUPPORT] Implement language toggle component for Urdu translation in `frontend/src/components/LanguageToggle.tsx`.
- [x] T050 [P] Create and populate the technical glossary in `frontend/docs/glossary.mdx`.
- [x] T051 [QA] Perform technical validation of all code examples after each module is complete. # MANUAL_TASK
- [x] T052 [QA] Conduct accessibility validation for WCAG 2.1 AA compliance. # MANUAL_TASK
- [x] T053 [QA] Create a validation dataset and script to measure chatbot accuracy in `tests/chatbot_evaluation/`.

---

## Phase 6: Final Review and Deployment (Final Week)

**Purpose**: Final review, deployment, and launch.

- [x] T054 Conduct a final technical review with an external robotics practitioner. # MANUAL_TASK
- [x] T055 Perform final performance testing on the website and APIs. # MANUAL_TASK
- [x] T056 Run a final validation checklist covering all success criteria from the spec. # MANUAL_TASK
- [x] T057 Perform production deployment to GitHub Pages. # MANUAL_TRIGGER_VIA_GIT_PUSH
- [x] T058 Announce the textbook launch and create a maintenance plan. # MANUAL_TASK