#%%
import pandas as pd
import numpy as np
import plotly.express as px
#%%
df = pd.read_json("flights_missing.json")
df
#%%
df['num_of_delays_late_aircraft'].value_counts()
# set -999 to nan with np.nan

#%%
df['num_of_delays_late_aircraft'].where(df>-999) # error


#%%
df.replace(-999) #doesn't work
#%%
df['num_of_delays_late_aircraft'].value_counts()
# %%
