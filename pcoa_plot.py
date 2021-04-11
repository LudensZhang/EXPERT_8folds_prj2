import pandas as pd
from skbio.diversity import beta_diversity
from skbio.stats.ordination import *
from plotnine import *


df_abundance = pd.read_csv('abundance.csv').T
df_map = pd.read_csv('mapper.csv')
df_map.index = df_map['SampleID']
Env = []


df_abundance.columns = df_abundance.iloc[0]
df_abundance = df_abundance.drop('samples',axis=0)

for i in df_abundance.index:
    Env.append(df_map.loc[i, 'Env'])

bc_dm = beta_diversity("braycurtis", df_abundance, df_abundance.index)
bc_pc = pd.DataFrame(pcoa(bc_dm, number_of_dimensions = 2).samples.values.tolist(),df_abundance.index, columns = ['PC1', 'PC2'])
df_abundance['Env'] = Env
print(bc_pc)

fig = (ggplot(bc_pc,aes(x = 'PC1', y = 'PC2',color ='Env'))
       + geom_point(size=1)
       + theme(figure_size= (10,10))
       + theme(panel_grid_major = element_blank(), panel_grid_minor = element_blank(), panel_background = element_blank())
       + theme(axis_line = element_line(color="gray", size = 5))
       + theme(legend_key_size = 5)
       + theme(legend_position = (0.9,0.9d))
       + stat_ellipse()
       + xlab('PC1')
       + ylab('PC2')
       )
print(fig)


