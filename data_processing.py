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
# %%
import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv('data/FormattedUsaTemp.csv')
# %%
data['mean'] = data.mean(axis=1)
# %%
new_data = data['State']
# %%
curYear = 1901
tmp = pd.DataFrame()
for i in range(1, len(data.columns)):
    if data.columns[i][:4] == str(curYear):
        if tmp.empty:
            tmp = data[data.columns[i]]
        else: # tmp is not none
            tmp[data.columns[i]] = data[data.columns[i]]
    else:
        print(curYear)
        new_data[str(curYear)] = tmp.mean(axis=1)
        curYear = curYear + 1
        

new_data[str(curYear)] = tmp.mean(axis=0)

# %%
slice['year'] = slice['dt'].str[:4]
# %%
new_slice = slice.groupby(['State','year'])['AverageTemperature'].mean().reset_index()
# %%
new_slice['AverageTemperature'] = new_slice['AverageTemperature'].round(3)
# %%
new_slice_transpose = new_slice.pivot(index='State',columns='year', values='AverageTemperature')
# %%
new_slice_transpose.to_csv('data/FormattedUsaTempByYear.csv')







