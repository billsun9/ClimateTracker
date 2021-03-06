# %%
# data is collected from https://www.kaggle.com/berkeleyearth/climate-change-earth-surface-temperature-data
# %%
import pandas as pd
import matplotlib.pyplot as plt
# %%
data_state = pd.read_csv('GlobalLandTemperaturesByState.csv')
print(data_state.shape)
print(data_state.columns)
# %%
data_usa = data_state.loc[data_state['Country']=='United States']
# %%
data_usa_not_null = data_usa.loc[data_usa.AverageTemperature.notnull()]
# %%
data_georgia = data_usa_not_null.loc[data_usa_not_null['State']=='Georgia (State)']
data_florida = data_usa_not_null.loc[data_usa_not_null['State']=='Florida']
# %%
# After 1900
data_georgia_f = data_georgia.loc[data_georgia['dt'] > '1900-12-01']
# %%
energy_use = pd.read_csv('TotalEnergyConsumption.csv')
l = energy_use.loc[energy_use['State']=='AK']
# %%
co2 = pd.read_csv('CarbonEmissionsUnadjusted.csv')
biomass = pd.read_csv('RenewBiomass.csv')
# %%
# %%
import pandas as pd
import matplotlib.pyplot as plt

data_state = pd.read_csv('data/GlobalLandTemperaturesByState.csv')
# %%
data_usa = data_state.loc[data_state['Country']=='United States']
# %%
data_usa_not_null = data_usa.loc[data_usa.AverageTemperature.notnull()]
# %%
data_usa_since_1900 = data_usa_not_null.loc[data_usa_not_null['dt'] > '1900-12-01']
# %%
al = data_usa_since_1900.loc[data_usa_since_1900['State']=='Alabama']
ct = data_usa_since_1900.loc[data_usa_since_1900['State']=='Connecticut']
# %%
fl = data_usa_since_1900.loc[data_usa_since_1900['State']=='Florida']
la = data_usa_since_1900.loc[data_usa_since_1900['State']=='Louisiana']
# %%
data_usa_since_1900.State.value_counts()
# %%
slice = data_usa_since_1900[['State','dt','AverageTemperature']]
# %%
slice['AverageTemperature'] = slice['AverageTemperature'].round(3)
# %%
slice_transpose = slice.pivot(index='State',columns='dt', values='AverageTemperature')
# %%
slice_transpose.to_csv('data/FormattedUsaTemp.csv')