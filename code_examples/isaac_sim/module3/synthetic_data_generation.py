from omni.isaac.kit import SimulationApp

# Configuration for the simulation
config = {
    "width": 1280,
    "height": 720,
    "headless": True, # Run in headless mode for data generation
}

# Create a simulation app
simulation_app = SimulationApp(config)

from omni.isaac.core import World
from omni.isaac.core.objects import cuboid
from omni.isaac.synthetic_utils import SyntheticDataHelper
import numpy as np
import carb

# Create a world
world = World()
world.scene.add_default_ground_plane()

# Add objects to the scene
cube1 = world.scene.add(
    cuboid.FixedCuboid(
        prim_path="/World/cube1",
        position=np.array([0.5, 0.5, 0.25]),
        scale=np.array([0.5, 0.5, 0.5]),
        color=np.array([1.0, 0, 0]),
    )
)
cube2 = world.scene.add(
    cuboid.FixedCuboid(
        prim_path="/World/cube2",
        position=np.array([-0.5, -0.5, 0.25]),
        scale=np.array([0.5, 0.5, 0.5]),
        color=np.array([0, 1.0, 0]),
    )
)

world.reset()

# Initialize SyntheticDataHelper
sd_helper = SyntheticDataHelper()
viewport_interface = omni.kit.viewport_legacy.get_viewport_interface()
viewport_window = viewport_interface.get_active_viewport_window()

# Configure and enable render products
# Requires a camera in the scene, add one if not present
# For simplicity, assuming a camera exists or can be added
# sd_helper.initialize(
#     sensor_names=["rgb", "depth", "instanceSegmentation"],
#     viewport=viewport_window
# )
# sd_helper.add_ground_plane(prim_path="/World/groundPlane")

# Example of how to generate data (simplified, full implementation would involve more setup)
num_frames = 10
print(f"Generating {num_frames} frames of synthetic data...")
for i in range(num_frames):
    # Randomize object positions slightly (example)
    cube1.set_world_pose(position=np.array([np.random.rand() - 0.5, np.random.rand() - 0.5, 0.25]))
    world.step(render=True) # Step the world and render a frame

    # Save data (requires render products setup which is more complex in a script)
    # sd_helper.get_ground_truth(["rgb", "depth", "instanceSegmentation"])
    # print(f"Frame {i} generated.")

print("Synthetic data generation example complete. Data would typically be saved here.")

simulation_app.close()
