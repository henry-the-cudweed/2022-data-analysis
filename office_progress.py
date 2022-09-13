# %% [markdown]
# testing area

# %%
#testing area
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import pandasql as pdsql
import pathlib 
import openpyxl


from pandasql import sqldf
pysqldf = lambda q: sqldf(q, globals())

#piecemeal approach to getting table sums
df = pd.read_csv('csv2022_A3.csv')
df_hwy_2022 = df.loc[(df['EventGroupName']=="Spring_2022") & (df['LocationID']=="MGP_01_HWY")]
df_hwy_2021 = df.loc[(df['EventGroupName']=="Spring_2021") & (df['LocationID']=="MGP_01_HWY")]
df_hwy_2020 = df.loc[(df['EventGroupName']=="Spring_2020") & (df['LocationID']=="MGP_01_HWY")]


df_hwy_2022_hits_sum = df_hwy_2022.groupby(['nativity']).sum()
df_hwy_2021_hits_sum = df_hwy_2021.groupby(['nativity']).sum()
df_hwy_2020_hits_sum = df_hwy_2020.groupby(['nativity']).sum()

#faster approach to getting number of hits in quadrat sums, to compare with excel sheet from last year's analysis, so i can see if i did an average
#or something else
df_grass = df.loc[(df['EventGroupName'] != "VC_CapeIvy_2022")]
df_hwy_allyears_hits_sum = df_grass.groupby(['EventGroupName','LocationID','nativity',]).sum()
df_loc_season_sum = df_grass.groupby(['EventGroupName','LocationID']).sum()
#print(df_hwy_2022_hits_sum)
#print(df_hwy_2021_hits_sum)
#print(df_hwy_2020_hits_sum)

#print(df_hwy_allyears_hits_sum)


def divide3(x):
    return round(x/3)

df_math = df_hwy_allyears_hits_sum['HitsInQuadrat'].apply(divide3)
df_group = df_math.groupby('LocationID') 
#df_sort=df_math.sort_values('LocationID',ascending=False)

#print(df_loc_season_sum)
#print(df_grass)

#i want to make the hitsinquadrat sum from df_loc_season_sum to be listed as a nativity total in df_grass

df_grass_test = df_grass.groupby(['EventGroupName','LocationID','nativity'])['HitsInQuadrat'].transform('sum')
df_grass["nativity_hits"] = df_grass.groupby(['EventGroupName','LocationID','nativity'])['HitsInQuadrat'].transform('sum')
# this gives percent of hits, to the category the hits are in df_grass["Percent_of_Hits"] = df_grass["HitsInQuadrat"] / df_grass["TotalHits"]



print(df_grass)
df_grass.to_excel("df_grass2.xlsx")


# %% [markdown]
# #creates an excel sheet with rounded averages for the number of hits per nativity for each year/plot 
# 

# %%
#creates an excel sheet with rounded averages for the number of hits per quadrat for each year/plot 
import pandas as pd
import openpyxl


df = pd.read_csv('csv2022_A3.csv')

df_grass = df.loc[(df['EventGroupName'] != "VC_CapeIvy_2022")]

df_hwy_allyears_hits_sum = df_grass.groupby(['EventGroupName','LocationID','nativity',]).sum()

def divide3(x):
    return round(x/3)

df_math= df_hwy_allyears_hits_sum['HitsInQuadrat'].apply(divide3)
df_group = df_math.groupby('LocationID') 

print(df_math)
df_math.to_excel("df_math2.xlsx")


# %%
#how do i add a sum total, all hits per plot/season?
import pandas as pd
import openpyxl


df = pd.read_csv('csv2022_A3.csv')

df_grass = df.loc[(df['EventGroupName'] != "VC_CapeIvy_2022")]

df_math = df_grass.groupby(['EventGroupName','LocationID','nativity',]).sum()
df_math2 = df_grass.groupby(['EventGroupName','LocationID',]).sum()
def divide3(x):
    return round(x/3)

df_math['AvgHitsPerNativity'] = df_math['HitsInQuadrat'].apply(divide3)
df_math2['AvgHitsPerPlot'] = df_math2['HitsInQuadrat'].apply(divide3)

df_group = df_math.groupby('LocationID') 


# copy pasted from test area df_grass_test = df_grass.groupby(['EventGroupName','LocationID','nativity'])['HitsInQuadrat'].transform('sum')

df_merge = pd.merge(left=df_math, right=df_math2, how='left', on=['EventGroupName', 'LocationID','Dead','Unrooted','nativity'],
      )

df_head = df_merge.head()
print(df_merge)

df_merge.to_excel("df_merge.xlsx")
#df_math2.to_excel("df_math2.xlsx")

#df_math['sum'] = df_math.sum()
#print(df_math)
#how do i add a sum total?



