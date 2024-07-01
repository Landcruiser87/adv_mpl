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
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import support
from rich import inspect

#%%

#This one might not work as the features have already been scaled. 
#Which .. makes plotting a little harder. 
opendb = support.grab_dataset(43482)

# Use rich to inspect the object
inspect(opendb)
support.view_allcols(opendb.data)


#%%
#!Which country produces the fastest Ironman competitors.  Male or female.
# Col descriptions
# [('col_idx', 'col_name'),
#  (0, 'BIB'),              (int)
#  (1, 'Name'),             (str)
#  (2, 'Country'),          (str)
#  (3, 'Gender'),           (str)
#  (4, 'Division'),         (str)
#  (5, 'Swim'),             (timedelta)
#  (6, 'Bike'),             (timedelta)
#  (7, 'Run'),              (timedelta)
#  (8, 'Overall'),          (int)
#  (9, 'Division_Rank'),    (int)
#  (10, 'Gender_Rank'),     (int)
#  (11, 'Overall_Rank'),    (int)
#  (12, 'T1'),              transition times (timedelta)
#  (13, 'T2')]              transition times (timedelta)

#idea links
#https://medium.com/@larushkalmy/the-nerds-guide-to-triathlon-25e1daa90571

#2 col 3 row (on the right) Grid spec of ....  
# 1. (entire left col) stacked bar h on the left of countrys times 
    #Color each stack in the stacked bar chart with a pallette for its given color
    # Giving you a feel for fastest countries swim , run, bike , t times. 
# 2. (upper right) barh of times by country. 
    #? Annotate each countries section average at the bottom of the bar.  That'll look cool
# 3. (middle right) tornado of male/female times
# 4. (bottom right) Distribution by country and activity
# Swim -> Bike -> Run


# iron_df['country'] = iron_df['Country'].map(opendb.country_codes)


# Lets limit it to the top 20 countries
# pal = list(sns.color_palette(palette="coolwarm", n_colors=20))

#1.  Build the gridspec we want to build.  in our case.  cols = 2, rows = 3 You
#can use the underscore to not return a particular portion of a method return.
#Here i'm using it to not confuse the ax object with the gridspec object.  As
#we'll use the gridspec object to manipularte various axes

fig = plt.figure(figsize = (10, 10))
gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 1])
ax_one = fig.add_subplot(gs[:3, 0], label="stack_country")
ax_two = fig.add_subplot(gs[0, 1], label="time_country")
ax_three = fig.add_subplot(gs[1:2, 1], label="tornado_mf")
ax_four = fig.add_subplot(gs[2:, 1], label="dist_mf")
plt.subplots_adjust(hspace=0.20)
ironman = opendb.data.copy() 

##############################  stacked bar ##############################
#data wrangling
#Groupby function is malfunctioning so doing it manually.  One of the many
#reasons to hate pandas

_graphcols = ["Swim", "T1", "Bike", "T2", "Run", "Overall"]
iron_df = pd.DataFrame(
    data = np.zeros(shape=(len(opendb.country_codes),len(_graphcols))),
    index = sorted(opendb.country_codes.keys()),
    columns=_graphcols
    )
#Calculate country wide means
for col in _graphcols:
    for country in iron_df.index:
        countrymean = ironman[col][ironman["Country"]==country].mean()
        iron_df.loc[country, col] = round(countrymean, 1)
#sort em
iron_df.sort_values(by="Overall", axis=0, inplace=True, ascending=True)
iron_df_s = iron_df.iloc[:20, :]
countries = list(iron_df_s.index)
colors = list(sns.color_palette(palette="coolwarm", n_colors=iron_df_s.shape[0]))

for i, (co_name, co_color) in enumerate(zip(countries, colors)):
    zipdata = zip(iron_df_s["Swim"], iron_df_s["T1"], iron_df_s["Bike"], iron_df_s["T2"], iron_df_s["Run"]) 
    total_time = [a + b + c + d for a, b, c, d, _ in zipdata]
    swims = [x / y * 100 for x, y in zip(iron_df_s["Swim"], total_time)]
    tr_one = [x / y * 100 for x, y in zip(iron_df_s["T1"], total_time)]
    bikes = [x / y * 100 for x, y in zip(iron_df_s["Bike"], total_time)]
    tr_two = [x / y * 100 for x, y in zip(iron_df_s["T2"], total_time)]
    runs = [x / y * 100 for x, y in zip(iron_df_s["Run"], total_time)]

    ax_one.barh(swims, color="lightblue")
    ax_one.barh(tr_one, color="white")
    ax_one.barh(bikes, color="yellow")
    ax_one.barh(tr_two, color="white")
    ax_one.barh(runs, color="lightred")


############################# times barh #################################


############################# tornado ####################################


############################# violin #####################################


# iterating the index with a counter because I need iloc and loc functions
# to the same row as well as axis reference
# for df_cntr, idx in enumerate(iron_df.index):
#     sns.kdeplot(
#         data = iron_df.loc[idx, "hr_arr"], color=iron_df.loc[idx, "color"],
#         ax = ax[df_cntr], bw_adjust=1, fill=True, 
#         alpha=1, linewidth=1.5) #clip_on=False
#     sns.kdeplot(
#         data = iron_df.loc[idx, "hr_arr"], color="w",
#         ax = ax[df_cntr], bw_adjust=1, linewidth=3)
#     # ax[idx].set_xlim([min_a, max_a])
#     workout_date = iron_df.loc[idx, "start_date"]
#     ax[df_cntr].annotate(
#         text = f"{workout_date:%m-%d-%Y}",
#         xy=(0.25, 0.5), 
#         textcoords="axes fraction",
#         xytext=(0.1, 0.25),
#         color = iron_df.loc[idx, "color"],
#         ha='center',
#         fontweight="bold",
#         annotation_clip=False)

#     # if covid_dates:
#     #     for cdate in covid_dates:
#     #         if cdate < workout_date:
#     #             ax[df_cntr].annotate(
#     #             text = f"Got Covid!! {cdate:%m-%d-%Y}",
#     #             xy=(0.25, 0.5), 
#     #             textcoords="axes fraction",
#     #             xytext=(0.3, 0.25),
#     #             color = iron_df.loc[idx, "color"],
#     #             ha='center',
#     #             fontweight="bold",
#     #             annotation_clip=False)
#     #             covid_dates.pop(0)    

#     ax[df_cntr].set_yticks([])
#     ax[df_cntr].set_ylabel("")
#     ax[df_cntr].spines["left"].set_visible(False)
#     ax[df_cntr].spines["bottom"].set_visible(False)
#     ax[df_cntr].spines["top"].set_visible(False)
#     ax[df_cntr].spines["right"].set_visible(False)

# fig.subplots_adjust(hspace=0.1)
# ax[-1].spines["bottom"].set_visible(True)
# plt.xlabel("Heart rate (bpm)", fontweight="bold", fontsize=13)
# plt.suptitle(f"KDE of HR over time for workout\n\n{activity}", ha="center", fontsize=20)
# plt.show()