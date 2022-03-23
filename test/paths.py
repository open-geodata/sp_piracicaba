
import os

input_path = os.path.join('..', 'data', 'input')
input_path_cad = os.path.join(input_path, 'cad')

os.makedirs(input_path_cad, exist_ok=True)

output_path = os.path.join('..', 'data', 'output')
output_path_maps = os.path.join(output_path, 'maps')
output_path_shps = os.path.join(output_path, 'shp')
output_path_geo = os.path.join(output_path, 'geo')

os.makedirs(output_path_shps, exist_ok=True)
os.makedirs(output_path_geo, exist_ok=True)
os.makedirs(output_path_maps, exist_ok=True)