"""
Spawn a falling object
"""

import pybullet as p 
import numpy as np 

# Sphere
def spawn_falling_sphere(radius=0.2, height=5):
    x, y = np.random.uniform(-2,2), np.random.uniform(-2,2)
    sphere_col = p.createCollisionShape(p.GEOM_SPHERE, radius=radius)
    sphere_vis = p.createVisualShape(p.GEOM_SPHERE, radius=radius, rgbaColor=[1,0,0,1])
    mass = 1

    sphere_id = p.createMultiBody(mass, sphere_col, sphere_vis, [x, y, height])

    # Random lateral velocity
    vx, vy = np.random.uniform(-1, 1), np.random.uniform(-1, 1)
    p.resetBaseVelocity(sphere_id, linearVelocity=[vx, vy, 0])
    return sphere_id
