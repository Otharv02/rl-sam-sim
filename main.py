import numpy as np 
import pybullet as p 
import pybullet_data
import time

from simulator import world, target

# Simulation Setup
p.connect(p.GUI) # /p.DIRECT
p.setAdditionalSearchPath(pybullet_data.getDataPath())
p.setRealTimeSimulation(0)
p.resetSimulation()


# Init World
world.init_world()


# Toggle rendering off while loading (optional)
world.toggle_rendering(False)

# Load ground
p.loadURDF("plane.urdf")

# Spawn target
target.spawn_falling_cylinder()

# Toggle rendering on after load
world.toggle_rendering(True)


# Simulation loop
for _ in range(1000):
    world.step_simulation()
    time.sleep(1./240.)

