import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
from matplotlib.colors import ListedColormap
import math
from matplotlib.cm import hsv
import matplotlib.backends.backend_pdf

df_nat = pd.DataFrame(pd.read_excel("df_col.xlsx"))
df_sp = pd.DataFrame(pd.read_excel("df2_sp.xlsx"))

##Prepare Data for Pie Charts, Creating a Concatinated Species Name Removing total and Not-Plant Values
df_sp["LocSeason"] = df_sp["LocationID"] +", "+ df_sp["EventGroupName"] 
df_sp["Sp_Name"] = df_sp["genus"] + " " + df_sp["species"]
df_sp2 = df_sp
df_sp3 = (df_sp2[df_sp2["nativity"].isin(["zTOTAL"]) == False]).sort_values(["LocationID","EventGroupName"])
df_sp3 = (df_sp3[df_sp3["nativity"].isin(["NOTPLANT"]) == False]).sort_values(["LocationID","EventGroupName"])
df_sp_tot = (df_sp2).sort_values(["LocationID","EventGroupName"])

#print(df_sp3)

#Something I was using when I was trying to automate the generation of pie charts
NumOfLocSeasons = df_sp["LocSeason"].count()
pielabels = (df_sp["LocSeason"])
piedata = (df_sp["PercentOfTotalHits"])

###Giving Each LocSeason it's Own Number

LocSeasonNums = df_sp3["LocSeason"].unique()
d = {'LocSeason' : LocSeasonNums, 'LocSeasonIndex' : range(len(LocSeasonNums))}
df_LocSeason_Index_Table=pd.DataFrame(d)
df_merge = pd.merge(df_sp3,df_LocSeason_Index_Table, on="LocSeason")
df_merge.to_excel("merge.xlsx")


###Set up Colors

###example code from stackoverflow pt 1
#df=pd.DataFrame({'product': [0,0,1,1,1,1,1,2,2,2], 
 #                'market': [1,2,1,2,5,6,7,1,6,7], 
  #               'value': [500,300,100,200,400,100,200,100,300,900]})

###example code from stackoverflow pt 2, i edited this to try to use 

colors = ["#000000", "#FFFF00", "#1CE6FF", "#FF34FF", "#FF4A46", "#008941", "#006FA6", "#A30059",
"#FFDBE5", "#7A4900", "#0000A6", "#63FFAC", "#B79762", "#004D43", "#8FB0FF", "#997D87",
"#5A0007", "#809693", "#FEFFE6", "#1B4400", "#4FC601", "#3B5DFF", "#4A3B53", "#FF2F80",
"#61615A", "#BA0900", "#6B7900", "#00C2A0", "#FFAA92", "#FF90C9", "#B903AA", "#D16100",
"#DDEFFF", "#000035", "#7B4F4B", "#A1C299", "#300018", "#0AA6D8", "#013349", "#00846F",
"#372101", "#FFB500", "#C2FFED", "#A079BF", "#CC0744", "#C0B9B2", "#C2FF99", "#001E09",
"#00489C", "#6F0062", "#0CBD66", "#EEC3FF", "#456D75", "#B77B68", "#7A87A1", "#788D66",
"#885578", "#FAD09F", "#FF8A9A", "#D157A0", "#BEC459", "#456648", "#0086ED", "#886F4C",
"#34362D", "#B4A8BD", "#00A6AA", "#452C2C", "#636375", "#A3C8C9", "#FF913F", "#938A81",
"#575329", "#00FECF", "#B05B6F", "#8CD0FF", "#3B9700", "#04F757", "#C8A1A1", "#1E6E00",
"#7900D7", "#A77500", "#6367A9", "#A05837", "#6B002C", "#772600", "#D790FF", "#9B9700",
"#549E79", "#FFF69F", "#201625", "#72418F", "#BC23FF", "#99ADC0", "#3A2465", "#922329",
"#5B4534", "#FDE8DC", "#404E55", "#0089A3", "#CB7E98", "#A4E804", "#324E72", "#6A3A4C"]

cdict = dict(zip(np.unique(df_merge["Sp_Name"].values), colors))

my_colormap = ListedColormap(cdict)


### autogenerating code from stackoverflow pt 3 i don't understand, it perhaps won't work because i am filtering out based on season,
#but it might work if i assigned a number to each season as in the example

#fig, axes = plt.subplots(nrows=1, ncols=3)
#for m in range(3):
#    data = df.loc[df['product']==m]
#    data.plot(ax=axes[m], kind='pie', y='value', figsize=(15,5), 
 #           colors=[cdict[v] for v in data["market"]])

# print(cdict)
# print ("D  D  D  D")
# print(df_LocSeason_Index_Table)

fig, axes = plt.subplots(nrows=1, ncols=3)
for m in range(0,3):
  
    data = df_merge.loc[df_merge['LocSeasonIndex']==m]
    title = df_LocSeason_Index_Table['LocSeason'].values[m]
    data.plot(ax=axes[m], kind='pie', y='PercentOfTotalHits', 
    labels=data["Sp_Name"],
    legend=None,
    figsize=(30,30),
    colors=[cdict[v] for v in data["Sp_Name"]]).set_title(f"{title}")   
plt.show()


fig, axes2 = plt.subplots(nrows=1, ncols=3)
for m in range(0,3):
    data = df_merge.loc[df_merge['LocSeasonIndex']==(m+2)]
    title = df_LocSeason_Index_Table['LocSeason'].values[m]
    data.plot(ax=axes2[m], kind='pie', y='PercentOfTotalHits', 
    labels=data["Sp_Name"],
    figsize=(30,30),
    legend=None,
    colors=[cdict[v] for v in data["Sp_Name"]]).set_title(f"{title}")



fig, axes3 = plt.subplots(nrows=1, ncols=3)
for m in range(0,3):
    data = df_merge.loc[df_merge['LocSeasonIndex']==(m+5)]
    title = df_LocSeason_Index_Table['LocSeason'].values[m]
    data.plot(ax=axes3[m], kind='pie', y='PercentOfTotalHits', 
    labels=data["Sp_Name"],
    legend=None,
    figsize=(30,30),
    colors=[cdict[v] for v in data["Sp_Name"]]).set_title(f"{title}")

plt.show()

### Create a table that has each species as a column, percentages as values, and seasons as row indexes
df_pivot = df_merge.pivot_table(values='PercentOfTotalHits', index="LocSeasonIndex", columns='Sp_Name', aggfunc= 'first')
df_merge_pivot = pd.merge(df_pivot,df_LocSeason_Index_Table, on="LocSeasonIndex")
column_to_move = df_merge_pivot.pop("LocSeason")
df_merge_pivot.insert(1, "LocSeason", column_to_move)
df_merge_pivot.to_excel("pivot_merge2.xlsx")
df_species_seasons = df_merge_pivot.drop(columns=['LocSeasonIndex'])

### Create Species lists from each year, to be used to make the legends smaller 
df_sp_hwy01_pre = df_merge_pivot[(df_merge_pivot["LocSeasonIndex"]==0)|(df_merge_pivot["LocSeasonIndex"]==1)| (df_merge_pivot["LocSeasonIndex"]==2)]
df_sp_hwy01 = df_sp_hwy01_pre.drop(columns=['LocSeasonIndex']).dropna(how='all', axis=1)
### Made a list of species for the year, not sure I actually need this but, if I do later:
#df_sp_hwy01_list = list(df_sp_hwy01.columns.values)
#del df_sp_hwy01_list[0]

df_sp_olh02_pre = df_merge_pivot[(df_merge_pivot["LocSeasonIndex"]==3)|(df_merge_pivot["LocSeasonIndex"]==4)| (df_merge_pivot["LocSeasonIndex"]==5)]
df_sp_olh02 = df_sp_olh02_pre.drop(columns=['LocSeasonIndex']).dropna(how='all', axis=1)

df_sp_pol03_pre = df_merge_pivot[(df_merge_pivot["LocSeasonIndex"]==6)|(df_merge_pivot["LocSeasonIndex"]==7)| (df_merge_pivot["LocSeasonIndex"]==8)]
df_sp_pol03 = df_sp_pol03_pre.drop(columns=['LocSeasonIndex']).dropna(how='all', axis=1)


####Create Stacked Area Plot
df_sp_hwy01.plot.area(x='LocSeason',  figsize=(12,6), color=cdict)
plt.legend(loc=(1.5,0))
plt.show()

df_sp_olh02.plot.area(x='LocSeason', figsize=(12,6), color=cdict)
plt.legend(loc=(1.5,0))
plt.show()

df_sp_pol03.plot.area(x='LocSeason', figsize=(12,6), color=cdict)
plt.legend(loc=(1.5,0))
# show the graph
plt.show()

