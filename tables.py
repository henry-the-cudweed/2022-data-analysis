#This codeblock creates tables on a per nativity and per species basis, of the average number of hits
# per quad in a plot-season, percentage of total hits per plot per plot-season

#to-do 
#   replace append with concat

import pandas as pd
import numpy as np
import openpyxl

df = pd.read_csv('2022_A3.csv')

df_grouploc_sum = df.groupby(["EventGroupName","LocationID"]).sum().reset_index()
df_grouplocnat_sum = df.groupby(["EventGroupName","LocationID","nativity"]).sum().reset_index()

#setting up a species based analysis
df_species = df.groupby(["EventGroupName","LocationID","genus","species","nativity"]).sum().reset_index()

#creates a new dataframe with sums for each season-loc stored in rows where nativity = zTotal
df_grouploc_sum.insert(3,"nativity","zTOTAL",True)

df_grouploc_sum_sp = df_grouploc_sum.copy()
df_grouploc_sum_sp['genus'] = ""
df_grouploc_sum_sp['species'] = ""


#adds the values from the new dataframe, where I created the zTOTAL rows, 
#to the previous dataframe df_grouploc_sum which has sums per nativity per season-loc 
#cleans up the table so that there is one clear index
df_append = df_grouplocnat_sum.append(df_grouploc_sum)
df_append = df_append.reset_index()
df_append = df_append.drop(['index'], axis=1)
df_append_sort = df_append.sort_values(["EventGroupName","LocationID","nativity"]).reset_index().drop(['index'], axis=1)
df2 = df_append_sort

df_append_sp = df_species.append(df_grouploc_sum_sp)
df_append_sp = df_append_sp.reset_index()
df_append_sp = df_append_sp.drop(['index'], axis=1)
df_append_sort_sp = df_append_sp.sort_values(["EventGroupName","LocationID","nativity"]).reset_index().drop(['index'], axis=1)
df2_sp = df_append_sort_sp


#creates the Total Column, AvgHitsInQuadrat Column showing the Average Hits per quadrat in each season-plot
#and a PercentofTotalHits column showing the percent by nativity of hits in a quadrat
df2['Total'] = df2['HitsInQuadrat'].where((df2['nativity'] == 'zTOTAL')).bfill()
df2['AvgHitsInQuadrat'] = round((df2['HitsInQuadrat'] / 3),1)
df2['PercentOfTotalHits'] = round((df2['HitsInQuadrat'] / df2['Total'])* 100,2)

df2_sp['Total'] = df2_sp['HitsInQuadrat'].where((df2_sp['nativity'] == 'zTOTAL')).bfill()
df2_sp['AvgHitsInQuadrat'] = round((df2_sp['HitsInQuadrat'] / 3),1)
df2_sp['PercentOfTotalHits'] = round((df2_sp['HitsInQuadrat'] / df2_sp['Total'])* 100,2)



### Column Organization ###
df_col = df2.reindex(columns=['EventGroupName','LocationID','nativity','Dead','Unrooted','HitsInQuadrat','AvgHitsInQuadrat','Total','PercentOfTotalHits'])
df_col_sp = df2_sp.reindex(columns=['EventGroupName','LocationID','genus','species','nativity','Dead','Unrooted','HitsInQuadrat','AvgHitsInQuadrat','Total','PercentOfTotalHits'])

### Printing, Excel Sheet Creation ###

df_col_sp.to_excel('df2_sp.xlsx')
#print(df_species)
#df_species.to_excel("df_species.xlsx")
#df_col.to_excel("df_col.xlsx")
#df.to_excel("2022_A3.xlsx")
#print(df_col)
#df_append_sort.to_excel("df_append_sort.xlsx")
