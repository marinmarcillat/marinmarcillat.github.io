import geopandas as gpd
import folium

traj_path = [r"map/planned_1.shp"]

map = folium.Map(
    tiles='https://server.arcgisonline.com/ArcGIS/rest/services/Ocean/World_Ocean_Base/MapServer/tile/{z}/{y}/{x}',
    attr='Esri',
    zoom_start=12
)
for p in traj_path:
    traj = gpd.read_file(p)
    folium.GeoJson(traj).add_to(map)

#'https://tiles.openseamap.org/seamark/{z}/{x}/{y}.png'
map.save(r"map.html")