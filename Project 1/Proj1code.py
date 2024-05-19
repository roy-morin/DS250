#%%
# import packages
import pandas as pd
import plotly.express as px

#%%
df = pd.read_csv('names_year.csv')

#%%
df

#%%
fig = px.line(
    df,
    x='year',
    y='Total'
)
fig.show()

#%%
# How does your name at your birth year compare to its use historically?

#%%
roydf = df[df['name'] == 'Roy']
roydf

#%%
fig = px.line(roydf, x='year', y='Total', title='Roy over the years')
fig



