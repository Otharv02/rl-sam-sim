"""
Spawn a falling object
"""

import pybullet as p 
import numpy as np 

# Cylinder
def spawn_falling_cylinder(radius=0.2, length=7):
    x, y = np.random.uniform(-2,2), np.random.uniform(-2,2)
    cylinder_col = p.createCollisionShape(p.GEOM_CYLINDER, radius=radius)
    cylinder_vis = p.createVisualShape(p.GEOM_CYLINDER, radius=radius, rgbaColor=[1,0,0,1])
    mass = 1

    cylinder_id = p.createMultiBody(mass, cylinder_col, cylinder_vis, [x, y, length])

    # lateral velocity (ballistic path)
    vx, vy = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
    vz     = 20
    p.resetBaseVelocity(cylinder_id, linearVelocity=[vx, vy, vz])
    return cylinder_id

    # 
