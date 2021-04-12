import pandas as pd
import numpy as np
from plotnine import *


df = pd.read_csv('distance.csv', header=0).T
print('reading data')
df = df.drop('Unnamed: 0', axis=0)
df_map = pd.read_csv('mapper.csv')
df_map.index = df_map['SampleID']
map = []
print('mapping')

for i in df.index:
    map.append(df_map.loc[i, 'Env'])
df.insert(0, 'Env', map)

print('sorting')
df_plot = pd.DataFrame([['root:0-2month', 'root:0-2month'],
                        ['root:0-2month', 'root:2-6month'],
                        ['root:0-2month', 'root:6-12month'],
                        ['root:2-6month', 'root:0-2month'],
                        ['root:2-6month', 'root:2-6month'],
                        ['root:2-6month', 'root:6-12month'],
                        ['root:6-12month', 'root:0-2month'],
                        ['root:6-12month', 'root:2-6month'],
                        ['root:6-12month', 'root:6-12month']],
                       columns=['x', 'y']
                       )

distance_stage_1_1 = []
distance_stage_1_2 = []
distance_stage_1_3 = []
distance_stage_2_1 = []
distance_stage_2_2 = []
distance_stage_2_3 = []
distance_stage_3_1 = []
distance_stage_3_2 = []
distance_stage_3_3 = []

print(df)
for i in df.index:
    if df.loc[i,'Env'] == 'root:0-2month':
        for j in range(360):
            distance_stage_1_1.append(df.loc[i,j])
            distance_stage_1_2.append(df.loc[i,j+360])
            distance_stage_1_3.append(df.loc[i,j+720])
    if df.loc[i,'Env'] == 'root:2-6month':
        for j in range(360):
            distance_stage_2_1.append(df.loc[i,j])
            distance_stage_2_2.append(df.loc[i,j+360])
            distance_stage_2_3.append(df.loc[i,j+720])
    if df.loc[i,'Env'] == 'root:6-12month':
        for j in range(360):
            distance_stage_3_1.append(df.loc[i,j])
            distance_stage_3_2.append(df.loc[i,j+360])
            distance_stage_3_3.append(df.loc[i,j+720])

distance_value = [np.mean(distance_stage_1_1),
                  np.mean(distance_stage_1_2),
                  np.mean(distance_stage_1_3),
                  np.mean(distance_stage_2_1),
                  np.mean(distance_stage_2_2),
                  np.mean(distance_stage_2_3),
                  np.mean(distance_stage_3_1),
                  np.mean(distance_stage_3_2),
                  np.mean(distance_stage_3_3),
                  ]
df_plot.insert(2, 'value', distance_value)
print('sorting successfully, result below')
print(df_plot)

print('plotting')
fig = (ggplot(df_plot, aes(x = 'x', y = 'y', fill = 'value',))
       +geom_tile()
       +scale_fill_gradient(low='white', high='red')
       +xlab('')
       +ylab('')
       +theme(figure_size=(10,8))
       )
print(fig)
