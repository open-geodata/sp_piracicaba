
import os
from pathlib import Path

data_path = os.path.join('..', 'src', 'sp_piracicaba', 'data')

input_path = os.path.join(data_path, 'input')
os.makedirs(input_path, exist_ok=True)

input_path_cad = os.path.join(input_path, 'cad')
os.makedirs(input_path_cad, exist_ok=True)

output_path = os.path.join(data_path, 'output')
os.makedirs(output_path, exist_ok=True)

output_path_map = os.path.join(output_path, 'maps')
os.makedirs(output_path_map, exist_ok=True)

output_path_shp = os.path.join(output_path, 'shp')
os.makedirs(output_path_shp, exist_ok=True)

output_path_geo = os.path.join(output_path, 'geo')
os.makedirs(output_path_geo, exist_ok=True)

output_path_zips = os.path.join(output_path, 'zips')
os.makedirs(output_path_zips, exist_ok=True)
