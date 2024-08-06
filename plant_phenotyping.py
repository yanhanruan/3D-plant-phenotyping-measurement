import trimesh
import numpy as np
import time
from concurrent.futures import ThreadPoolExecutor

# Load the OBJ file
mesh = trimesh.load('base.obj')

def time_cost_calculation(func, *args):
    start_time = time.time()
    result = func(*args)
    time_cost = time.time() - start_time
    return result, time_cost

def calculate_height(mesh):
    height = mesh.bounds[1][2] - mesh.bounds[0][2]
    return height

def calculate_surface_area(mesh):
    surface_area = mesh.area
    return surface_area

def calculate_volume(mesh):
    volume = mesh.volume
    return volume

def calculate_angle(mesh):
    normal_0 = mesh.face_normals[0]
    normal_1 = mesh.face_normals[1]
    angle = np.arccos(np.dot(normal_0, normal_1) / (np.linalg.norm(normal_0) * np.linalg.norm(normal_1)))
    angle_degrees = np.degrees(angle)
    return angle_degrees

# Use ThreadPoolExecutor to run calculations in parallel
with ThreadPoolExecutor() as executor:
    height_future = executor.submit(time_cost_calculation, calculate_height, mesh)
    surface_area_future = executor.submit(time_cost_calculation, calculate_surface_area, mesh)
    volume_future = executor.submit(time_cost_calculation, calculate_volume, mesh)
    angle_future = executor.submit(time_cost_calculation, calculate_angle, mesh)

    height, height_time = height_future.result()
    surface_area, surface_area_time = surface_area_future.result()
    volume, volume_time = volume_future.result()
    angle_degrees, angle_time = angle_future.result()

print(f"Height: {height} (calculated in {height_time:.6f} seconds)")
print(f"Surface Area: {surface_area} (calculated in {surface_area_time:.6f} seconds)")
print(f"Volume: {volume} (calculated in {volume_time:.6f} seconds)")
print(f"Angle between face 0 and face 1: {angle_degrees} degrees (calculated in {angle_time:.6f} seconds)")
