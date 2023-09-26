import geopandas as geo
import matplotlib.pyplot as plt
from geobr import read_state
import pandas as pd

caminho_arquivo = r'C:\Users\henri\CODE\python\PRO\VWM\VWM_AREAS_CONTAMINADAS_GEODADOS_CETESB_PTOPoint.shp'
data_cont = geo.read_file(caminho_arquivo)

#Passos para plotar o mapa
#1. definir o tamanho da figura
#2. definir os dados que serão usados (coluna, legenda, tamanho, cor)
#3. titulo
#4. plotar o mapa

sp = read_state(code_state = 'SP', year = 2020)#importa o mapa de SP

fig, ax = plt.subplots(figsize = (12, 10))
sp.plot(ax = ax, color = 'none', edgecolor = 'black', linewidth = 1.5)#cria o mapa de SP
data_cont.plot(column = 'Classifica', ax = ax, legend = True, markersize = 2, legend_kwds = {'loc': 'upper left', 'bbox_to_anchor': (1,1)})
plt.title("Mapa de Áreas Contaminadas por Classificação de SP")
plt.show()

#mapa de densidade
import folium
from folium import plugins
#from folium.plugins import MarkerCluster

map = folium.Map(location=[-23.5505, -46.6333], tiles="Cartodb dark_matter", zoom_start=5)
heat_data = [[point.xy[1][0], point.xy[0][0]] for point in data_cont.geometry]
heat_data
plugins.HeatMap(heat_data).add_to(map)
map.save("heatmap.html")

## Passo para criar o mapa interativo
#1. importar as biliotecas
#2. definir a localização inicial e o zoom
#3. criar o cluster
#4. fazer os marcadores utilizando o for
#5. salvar (exportar) o mapa

base_map = folium.Map(location=[-23.5505, -46.6333], tiles="Cartodb dark_matter", zoom_start=5)
map = plugins.MarkerCluster().add_to(base_map)

for i, point in data_cont.geometry.items():
    lat, lon = point.y, point.x
    folium.Marker(location = [lat, lon], popup = f"Classificação: {data_cont.at[i, 'Classifica']} \nAtividade: {data_cont.at[i, 'Atividade']}").add_to(map)

base_map
base_map.save('Mapbase.html')