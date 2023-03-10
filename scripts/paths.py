"""
Pastas do Projeto
mar.2023
"""


from pathlib import Path


# Project Path
project_path = Path(__file__).parents[1]

# Package Path
package_path = project_path / 'sp_piracicaba'

# Data
data_path = package_path / 'data'
data_path.mkdir(exist_ok=True)

# Input
input_path = data_path / 'input'
input_path.mkdir(exist_ok=True)

input_path_cad = input_path / 'cad'
input_path_cad.mkdir(exist_ok=True)

# Output
output_path = data_path / 'output'
output_path.mkdir(exist_ok=True)

output_path_geojson = output_path / 'geojson'
output_path_geojson.mkdir(exist_ok=True)

output_path_gpkg = output_path / 'gpkg'
output_path_gpkg.mkdir(exist_ok=True)

output_path_geo = output_path / 'geo'
output_path_geo.mkdir(exist_ok=True)

output_path_map = output_path / 'map'
output_path_map.mkdir(exist_ok=True)

output_path_shp = output_path / 'shp'
output_path_shp.mkdir(exist_ok=True)


# scrapy_path = project_path / 'scrapy'
# scrapy_path.mkdir(exist_ok=True)

# logs_path = scrapy_path / 'logs'
# logs_path.mkdir(exist_ok=True)

# adds_path = scrapy_path / 'adds'
# adds_path.mkdir(exist_ok=True)

if __name__ == '__main__':
    print(project_path)
