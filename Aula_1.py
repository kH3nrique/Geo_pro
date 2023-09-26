import geopandas as gpd
import matplotlib.pyplot as plt
caminho_arquivo = r'C:\Users\henri\CODE\python\PRO\VWM\VWM_AREAS_CONTAMINADAS_GEODADOS_CETESB_PTOPoint.shp'
dados_cont = gpd.read_file(caminho_arquivo)
dados_cont

classif_cont = dados_cont['Classifica'].value_counts()
classif_cont

plt.figure(figsize = (10,6))
classif_cont.plot(kind = 'bar')
plt.xlabel('Classificação')
plt.ylabel('Contagem')
plt.title('Contagem de Ocorrências por Classificação de Áreas Contaminadas')
plt.xticks(rotation = 45, ha = 'right')
plt.show()

contam = dados_cont['Contaminan'].value_counts()
contam

plt.figure(figsize = (10,6))
contam.plot(kind = 'bar')
plt.xlabel('Contaminante')
plt.ylabel('Contagem')
plt.title('Contagem de Ocorrências por Contaminantes')
plt.xticks(rotation = 45, ha = 'right')
plt.show()

# análise por município

campinas = dados_cont[dados_cont['Municipio'] == 'CAMPINAS']
campinas

classif_camp = campinas['Classifica'].value_counts()
plt.figure(figsize = (10,6))
classif_camp.plot(kind = 'bar')
plt.xlabel('Classificação')
plt.ylabel('Contagem')
plt.title('Contagem de Ocorrências por Classificação de Áreas Contaminadas de Campinas')
plt.xticks(rotation = 45, ha = 'right')
plt.show()

import plotly.express as px

classif_camp = campinas['Classifica'].value_counts()

df = classif_camp.reset_index()

df.columns = ['Classificação', 'Contagem']

fig = px.bar(df, x="Classificação", y="Contagem", color="Classificação")
fig.show()

# Análise dos dados para todos os município

municipios = dados_cont['Municipio'].unique()


for municipio in municipios:

    todos_mun = dados_cont[dados_cont['Municipio'] == municipio]

    classif_mun = todos_mun['Classifica'].value_counts().reset_index()

    classif_mun.columns = ['Classificação', 'Contagem']

    fig = px.bar(classif_mun, x="Classificação", y="Contagem", color="Classificação")

    fig.update_layout(title = f'Contagem de Ocorrências por Classificação de Áreas Contaminadas em {municipio}')

    fig.show()