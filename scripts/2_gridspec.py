############################THOUGHTS$%#####################
# Thinking ahead.  
# For the gridspec example.  Wondering what types of data would be interesting
# to view for this. 

#IDEA's
# 1. Debugger Deep Dive
    # pdb.set_trace    
    # - launch.json
        #Go over basic setup and talk about where to put the launch.json
    # Breakpoints
    # Commands
        # Play
        # Stepping
        
    # pics that show the different functions.
    # resource article?  someone has to have written about this in a non-doc fashion

# 2. time series that i deconstruct with wavelets or FFT on the other side. 
    # - Could build that into the dashboard example too. 
    #MITDB maybe?  .. hmm. nah. 
    #multimodal datset?  
        # this might be best.  
        # but won't be able to read it into memory. 
        # Could use the German multimodal dataset I found for Tom
        # He also suggested another one.. can't remember
    #Daily bikes?
        #45103
        #this one coudl be fun.  Lots of good weather data
    #electric cars?  Sure?!
        #45948
        #ehhh i waited for like a minute.  data still hadn't come down yet,
        #so maybe we'll come back to this one. 
    #2019 Ironman? 
        # 43482
        # Say whaaaaat.   This could be very cool
        # Coud ook at the old cherry blossom modeling!  
    #New york bike dataset
        #more complex, but could be better
        #viz available.


#Will need a new dataset. 


#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import seaborn as sns
import support
from rich import inspect

#%%

#This one might not work as the features have already been scaled. 
#Which .. makes plotting a little harder. 
opendb = support.grab_dataset(43482)

inspect(opendb)
#Select numeric columns
numcols = opendb.data.select_dtypes("number").columns.tolist()
support.view_allcols(opendb.data)
support.sum_stats("number", "Numeric Variable Summary", opendb.data)



#%%
#  Gridspec plot ideas
# 

#Fancy pd time series resampling to look at weekly/monthly trends.
#Workday vs not.
#Tornado chart of windspeeds? Ironic AND fun.
#3 x 3 ridgeline ?
#by mean monthly temp
#by mean monthly humidity
#by mean monthly windspeed

#!Which country produces the fastest Ironman competitors.  Male or female.

iron_df = opendb.data.copy() #monthly resample by country
time_cols = ["Bike", "Swim", "Run", "Overall"]

iron_df['mnth'] = iron_df['mnth'].map(opendb.month_dict)

pal = list(sns.color_palette(palette="coolwarm", n_colors=iron_df.shape[0]))
iron_df["HR_rank"] = iron_df["average_heartrate"].rank(axis=0, method="average", ascending=False).astype(int)
iron_df["color"] = [pal[::-1][x-1] for x in iron_df["HR_rank"]]

fig, ax = plt.subplots(
    nrows=iron_df.shape[0], 
    ncols=1,
    figsize = (10, 10),
    sharex=True
)
# iterating the index with a counter because I need iloc and loc functions
# to the same row as well as axis reference
for df_cntr, idx in enumerate(iron_df.index):
    sns.kdeplot(
        data = iron_df.loc[idx, "hr_arr"], color=iron_df.loc[idx, "color"],
        ax = ax[df_cntr], bw_adjust=1, fill=True, 
        alpha=1, linewidth=1.5) #clip_on=False
    sns.kdeplot(
        data = iron_df.loc[idx, "hr_arr"], color="w",
        ax = ax[df_cntr], bw_adjust=1, linewidth=3)
    # ax[idx].set_xlim([min_a, max_a])
    workout_date = iron_df.loc[idx, "start_date"]
    ax[df_cntr].annotate(
        text = f"{workout_date:%m-%d-%Y}",
        xy=(0.25, 0.5), 
        textcoords="axes fraction",
        xytext=(0.1, 0.25),
        color = iron_df.loc[idx, "color"],
        ha='center',
        fontweight="bold",
        annotation_clip=False)

    # if covid_dates:
    #     for cdate in covid_dates:
    #         if cdate < workout_date:
    #             ax[df_cntr].annotate(
    #             text = f"Got Covid!! {cdate:%m-%d-%Y}",
    #             xy=(0.25, 0.5), 
    #             textcoords="axes fraction",
    #             xytext=(0.3, 0.25),
    #             color = iron_df.loc[idx, "color"],
    #             ha='center',
    #             fontweight="bold",
    #             annotation_clip=False)
    #             covid_dates.pop(0)    

    ax[df_cntr].set_yticks([])
    ax[df_cntr].set_ylabel("")
    ax[df_cntr].spines["left"].set_visible(False)
    ax[df_cntr].spines["bottom"].set_visible(False)
    ax[df_cntr].spines["top"].set_visible(False)
    ax[df_cntr].spines["right"].set_visible(False)

fig.subplots_adjust(hspace=0.1)
ax[-1].spines["bottom"].set_visible(True)
plt.xlabel("Heart rate (bpm)", fontweight="bold", fontsize=13)
plt.suptitle(f"KDE of HR over time for workout\n\n{activity}", ha="center", fontsize=20)
plt.show()