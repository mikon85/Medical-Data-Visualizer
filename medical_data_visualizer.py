import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Task 1: Import the data from medical_examination.csv and assign it to the df variable
df = pd.read_csv('medical_examination.csv')

# Task 2: Create the overweight column in the df variable
df['overweight'] = (df['weight'] / ((df['height'] / 100) ** 2) > 25).astype(int)

# Task 3: Normalize data by making 0 always good and 1 always bad
df['cholesterol'] = (df['cholesterol'] > 1).astype(int)
df['gluc'] = (df['gluc'] > 1).astype(int)

# Task 4: Draw the Categorical Plot in the draw_cat_plot function
def draw_cat_plot():
    # Task 5: Create a DataFrame for the cat plot using pd.melt
    df_cat = pd.melt(df, id_vars=['cardio'], value_vars=['cholesterol', 'gluc', 'smoke', 'alco', 'active', 'overweight'])

    # Task 6: Group and reformat the data in df_cat to split it by cardio and rename one of the columns
    df_cat['total'] = 1
    df_cat = df_cat.groupby(['cardio', 'variable', 'value'], as_index=False).count()

    # Task 7: Convert the data into long format and create a chart using sns.catplot()
    fig = sns.catplot(data=df_cat, kind='bar', x='variable', y='total', hue='value', col='cardio').fig

    # Task 8: Get the figure for the output and store it in the fig variable
    return fig

# Task 9: Draw the Heat Map in the draw_heat_map function
def draw_heat_map():
    # Task 10: Clean the data in the df_heat variable
    df_heat = df[
        (df['ap_lo'] <= df['ap_hi']) &
        (df['height'] >= df['height'].quantile(0.025)) &
        (df['height'] <= df['height'].quantile(0.975)) &
        (df['weight'] >= df['weight'].quantile(0.025)) &
        (df['weight'] <= df['weight'].quantile(0.975))
    ]

    # Task 11: Calculate the correlation matrix
    corr = df_heat.corr()

    # Task 12: Generate a mask for the upper triangle
    mask = np.triu(np.ones_like(corr, dtype=bool))

    # Task 13: Set up the matplotlib figure
    fig, ax = plt.subplots(figsize=(11, 9))

    # Task 14: Plot the correlation matrix using sns.heatmap()
    sns.heatmap(corr, mask=mask, annot=True, fmt=".1f", vmax=.3, center=0, square=True, linewidths=.5, cbar_kws={"shrink": .5})

    # Task 15: Do not modify the next two lines
    plt.savefig('heatmap.png')
    return fig


    # Test the functions
draw_cat_plot()
draw_heat_map()
