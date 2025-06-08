"""
Set up simulation environment
"""

import pybullet as p 

def init_world(gravity=(0,0,-9.8), time_step=1./204.):
    p.setGravity(*gravity)
    p.setTimeStep(time_step)

def step_simulation():
    p.stepSimulation()

def toggle_rendering(enable=True):
    p.configureDebugVisualizer(p.COV_ENABLE_RENDERING,int(enable))

