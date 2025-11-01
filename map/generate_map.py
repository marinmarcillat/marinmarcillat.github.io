import geopandas as gpd
import folium
import matplotlib.pyplot as plt
import geopy.distance as geo

traj_points_path = r"map/planned_trajectory.shp"

map = folium.Map(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/{z}/{y}/{x}',
    attr='Esri',
    zoom_start = 1,
    location = [-6.45,-113.72]
)

traj_points = gpd.read_file(traj_points_path)
pts_coords = traj_points.get_coordinates()

trajectory = []
distances = []
for i in range(len(pts_coords)-1):
    start = pts_coords.iloc[i][['y','x']].to_list()
    end = pts_coords.iloc[i+1][['y','x']].to_list()
    for j in [start,end]:
        if j[1] > 100:
            j[1] = - 360 + j[1]
    distances.append(str(int(geo.great_circle(start, end).nautical))+' nm')
    trajectory.append([start, end])


for i, l in enumerate(trajectory):
    folium.PolyLine(
        locations=l,
        tooltip=distances[i]
    ).add_to(map)

#'https://tiles.openseamap.org/seamark/{z}/{x}/{y}.png'
map.save(r"map.html")