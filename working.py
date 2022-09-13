import pandas as pd
import openpyxl

df = pd.read_csv('2022_A3.csv')

df_grouploc_sum = df.groupby(["EventGroupName","LocationID"]).sum().reset_index()
df_grouplocnat_sum = df.groupby(["EventGroupName","LocationID","nativity"]).sum().reset_index()


df_grouploc_sum.insert(3,"nativity","zTOTAL",True)
#df_grouplocnat_sum.loc[len(df_grouplocnat_sum.index)] = [df_grouploc_sum


df_append = df_grouplocnat_sum.append(df_grouploc_sum)
df_append = df_append.reset_index()
df_append = df_append.drop(['index'], axis=1)
df_append_sort = df_append.sort_values(["EventGroupName","LocationID","nativity"]).reset_index().drop(['index'], axis=1)
# something like the equation i want to build to, but i need to figure out the locs df_append_sort_col = df_grouploc_sum.insert(7,"percent",(loc.nativity/loc.['zTotal']),True)

a = df_append_sort.loc[df_append_sort.EventGroupName == "Spring_2020"]


print(a)
df_append_sort.to_excel("df_append_sort.xlsx")
