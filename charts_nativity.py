import pandas as pd
import openpyxl
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

df_nat = pd.DataFrame(pd.read_excel("df_col.xlsx"))
df_sp = pd.DataFrame(pd.read_excel("df2_sp.xlsx"))

df_nat["LocSeason"] = df_nat["LocationID"] +", "+ df_nat["EventGroupName"] 
df_nat2 = df_nat
df_nat3 = (df_nat2[df_nat2["nativity"].isin(["zTOTAL"]) == False]).sort_values(["LocationID","EventGroupName"])
df_nat_tot = (df_nat2).sort_values(["LocationID","EventGroupName"])


NumOfLocSeasons = df_nat["LocSeason"].count()


pielabels = (df_nat["LocSeason"])
piedata = (df_nat["PercentOfTotalHits"])


fig, axes = plt.subplots(3,3)

#LINE 1
axes[0,0].pie(((df_nat3['PercentOfTotalHits']).where(df_nat3["LocSeason"] == "MGP_01_HWY, Spring_2020").dropna()),
labels=df_nat3["nativity"].where(df_nat3["LocSeason"] == "MGP_01_HWY, Spring_2020").dropna(),
autopct='%1.1f%%')
axes[0,0].set_title('MGP_01_HWY, Spring_2020', fontsize = 25)


axes[0,1].pie(((df_nat3['PercentOfTotalHits']).where(df_nat3["LocSeason"] == "MGP_01_HWY, Spring_2021").dropna()),
labels=df_nat3["nativity"].where(df_nat3["LocSeason"] == "MGP_01_HWY, Spring_2021").dropna(),
autopct='%1.1f%%')
axes[0,1].set_title('MGP_01_HWY, Spring_2021', fontsize = 25)


axes[0,2].pie(((df_nat3['PercentOfTotalHits']).where(df_nat3["LocSeason"] == "MGP_01_HWY, Spring_2022").dropna()),
labels=df_nat3["nativity"].where(df_nat3["LocSeason"] == "MGP_01_HWY, Spring_2022").dropna(),
autopct='%1.1f%%')
axes[0,2].set_title('MGP_01_HWY, Spring_2022', fontsize = 25)

#LINE 2
axes[1,0].pie(((df_nat3['PercentOfTotalHits']).where(df_nat3["LocSeason"] == "MGP_02_OLH, Spring_2020").dropna()),
labels=df_nat3["nativity"].where(df_nat3["LocSeason"] == "MGP_02_OLH, Spring_2020").dropna(),
autopct='%1.1f%%')
axes[1,0].set_title('MGP_02_OLH, Spring_2020', fontsize = 25)


axes[1,1].pie(((df_nat3['PercentOfTotalHits']).where(df_nat3["LocSeason"] == "MGP_02_OLH, Spring_2021").dropna()),
labels=df_nat3["nativity"].where(df_nat3["LocSeason"] == "MGP_02_OLH, Spring_2021").dropna(),
autopct='%1.1f%%')
axes[1,1].set_title('MGP_02_OLH, Spring_2021', fontsize = 25)


axes[1,2].pie(((df_nat3['PercentOfTotalHits']).where(df_nat3["LocSeason"] == "MGP_02_OLH, Spring_2022").dropna()),
labels=df_nat3["nativity"].where(df_nat3["LocSeason"] == "MGP_02_OLH, Spring_2022").dropna(),
autopct='%1.1f%%')
axes[1,2].set_title('MGP_02_OLH, Spring_2022', fontsize = 25)

#LINE 3
axes[2,0].pie(((df_nat3['PercentOfTotalHits']).where(df_nat3["LocSeason"] == "MGP_03_POL, Spring_2020").dropna()),
labels=df_nat3["nativity"].where(df_nat3["LocSeason"] == "MGP_03_POL, Spring_2020").dropna(),
autopct='%1.1f%%')
axes[2,0].set_title('MGP_03_POL, Spring_2020', fontsize = 25)


axes[2,1].pie(((df_nat3['PercentOfTotalHits']).where(df_nat3["LocSeason"] == "MGP_03_POL, Spring_2021").dropna()),
labels=df_nat3["nativity"].where(df_nat3["LocSeason"] == "MGP_03_POL, Spring_2021").dropna(),
autopct='%1.1f%%')
axes[2,1].set_title('MGP_03_POL, Spring_2021', fontsize = 25)


axes[2,2].pie(((df_nat3['PercentOfTotalHits']).where(df_nat3["LocSeason"] == "MGP_03_POL, Spring_2022").dropna()),
labels=df_nat3["nativity"].where(df_nat3["LocSeason"] == "MGP_03_POL, Spring_2022").dropna(),
autopct='%1.1f%%')
axes[2,2].set_title('MGP_03_POL, Spring_2022', fontsize = 25)

#def pw(x) :
 #    np.piecewise(x, [x >=0, ((x > 2) & (x <= 5)), x > 5 ], 
  #  [lambda x : np.ceil(((x-2)/4)), lambda x : np.ceil((x-1)/4), lambda x : np.ceil(x/4)])

#xVal = df_nat3['PercentOfTotalHits'].where(df_nat3["LocSeason"] == "MGP_03_POL, Spring_2020").dropna()
#labelsVal = df_nat3["nativity"].where(df_nat3["LocSeason"] == "MGP_03_POL, Spring_2020").dropna()

#fig, axes = plt.subplots(3,3)

#for i in range(0,9):
   # axes[0,i].pie(xVal, labels=labelsVal, autopct='%1.1f%%')
    #axes[0,i].set_title('MGP_03_POL, Spring_2020', fontsize = 25)
    #print(i)
    #if i > 2:
    #    break 
    #axes[1,(i-3)].pie(xVal, labels=labelsVal, autopct='%1.1f%%')
    #axes[1,(i-3)].set_title('MGP_03_POL, Spring_2020', fontsize = 25)
    #print(i)
    #if i > 5 :
    #   break
    #axes[2,i].pie(xVal, labels=labelsVal, autopct='%1.1f%%')
    #axes[2,i].set_title('MGP_03_POL, Spring_2020', fontsize = 25)
    
plt.show()