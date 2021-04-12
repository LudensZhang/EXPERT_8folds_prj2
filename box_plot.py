import pandas as pd
from plotnine import *


df = pd.read_csv('compare_2.csv')
box_plot = (ggplot(df, aes(x = 'stage', y = 'AUC', fill = 'model'))
            +geom_boxplot(show_legend = 1)
            +theme(legend_position=(0.8, 0.8)))
print(box_plot)
