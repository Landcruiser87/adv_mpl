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
import matplotlib.dates as mdates
import matplotlib.ticker as ticker
from datetime import timedelta
import support
from rich import inspect

#%%
#Load dataset into memory
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

fig = plt.figure(figsize = (12, 10))
gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 1])
#Far left axis
ax_one = fig.add_subplot(gs[:3, 0], label="stack_country")
#Top right axis
ax_two = fig.add_subplot(gs[0, 1], label="swim")
#mid right axis
ax_three = fig.add_subplot(gs[1:2, 1], label="bike")
#low right axis
ax_four = fig.add_subplot(gs[2:, 1], label="run")

plt.subplots_adjust(hspace=0.5)
 
##############################  stacked bar ##############################
#data wrangling
#Groupby function is malfunctioning so doing it manually.  One of the many
#reasons to hate pandas
ironman = opendb.data.copy()
ironman["Transitions"] = ironman["T1"] + ironman["T2"]
graphcols = ["Swim", "Bike", "Run", "Overall", "Transitions"]
iron_df = pd.DataFrame(
    data = np.zeros(shape=(len(opendb.target_dict),len(graphcols))),
    index = sorted(opendb.target_dict.keys()),
    columns=graphcols
)

#Calculate country wide means 
#NOTE Noticing that smaller count countries have lower means. 
#Might need to stipulate you have at least 10 people racing from a country
#In order to calculate an average
for col in graphcols:
    for country in iron_df.index:
        #Have at least 10 race participants for that country
        if ironman[ironman["Country"]==country].shape[0] > 10:
            countrymean = ironman[col][ironman["Country"]==country].mean()
            iron_df.loc[country, col] = round(countrymean, 1)
        else:
            iron_df.loc[country, col] = np.nan

#Drop the nan countries (countries with fewer than 10)
iron_df.dropna(inplace=True)

#sort em
iron_df.sort_values(by="Overall", axis=0, inplace=True, ascending=True)

#Get rid of that col because we don't want to graph it. 
iron_df.drop("Overall", axis=1, inplace=True)
graphcols.pop(graphcols.index("Overall"))

#rearrange the cols
iron_df = iron_df[["Swim", "Bike", "Run", "Transitions"]]

#subset t20
iron_df_s = iron_df.iloc[:20, :]
countries = list(iron_df_s.index)
colors = list(sns.color_palette(palette="tab10", n_colors=len(graphcols)))
#if you want to use mpl
# category_colors = plt.colormaps['RdYlGn'](np.linspace(0.15, 0.85, iron_df.shape[1])) 

for i, (co_name, co_color) in enumerate(zip(graphcols, colors)):
    widths = iron_df_s.iloc[:, i].astype("timedelta64[s]") / pd.Timedelta(1, "h")
    starts = (iron_df_s.iloc[:, :i+1].cumsum(axis=1).iloc[:, -1].astype("timedelta64[s]") / pd.Timedelta(1, "h")) - widths 
    rects = ax_one.barh(countries, widths, left=starts, height=0.5, label=co_name, color=co_color)
    r, g, b = co_color
    text_color = 'black' if r* g* b < 0.5 else 'darkgrey'
    if not "t" in co_name:
        f_labels = iron_df_s.iloc[:, i].apply(lambda x:support.convert_time_format(x))
        if co_name=="Swim":
            ax_one.bar_label(rects, labels=f_labels, label_type='center', color="white", fontsize=6)
        else:
            ax_one.bar_label(rects, labels=f_labels, label_type='center', color=text_color, fontsize=10)

#Alter X tick labels
# xtick_labels = ax_one.get_xticks().tolist()
# labelsformatted = [support.convert_time_format(x) for x in xtick_labels]
# ax_one.set_xticks(xtick_labels)
# ax_one.set_xticklabels(ax_one.get_xticklabels(), rotation=-20)
ax_one.set_xlabel("Hours")
ax_one.legend(ncols=len(graphcols), loc='upper left', fontsize='small') #bbox_to_anchor=(-0.06, 0.98)
ax_one.invert_yaxis()
ax_one.set_title("Average times By Country", color="black", size=16)

############################# violin swim #################################
# Distribution of top 5 countries M/F swim times?
#Grab top 5 Countries from iron_df we made earlier. 
#%%
im_df = ironman.copy()
for event_col, ax in zip(graphcols[:3], [ax_two, ax_three, ax_four]):
    #Subset any null values. 
    im_df = im_df[~im_df[event_col].isnull()]
    
    #Subset Country counts over 10 
    im_df = im_df[im_df['Country'].map(im_df['Country'].value_counts()) > 10]

    #Groupby Country and calc means
    im_gp = im_df.groupby(by="Country")
    swims = im_gp[event_col].mean().sort_values()

    #howmany do ya want
    howmany = 8
    top5 = swims.index[:howmany]

    POSITIONS = list(range(howmany))
    
    COLORS = list(sns.color_palette(palette="coolwarm", n_colors=len(POSITIONS)))
    sample = im_df[im_df["Country"].isin(top5)]
    sample.sort_values(by=event_col, ascending=True)
    
    #resample into hours.  Fixing the ticks is too hard. 
    ydata = [sample[sample["Country"]==country][event_col] for country in top5]
    ydata = [y.astype("timedelta64[s]") / pd.Timedelta(1, "h") for y in ydata]

    #Average swim times and voilin plot for M/F distribution
    violins = ax.violinplot(
        dataset=ydata,
        positions=POSITIONS,
        vert=True,
        bw_method="silverman",
        showmeans=True,
        showmedians=False,
        showextrema=False
    )

    for r, pc in enumerate(violins["bodies"]):
        pc.set_facecolor(COLORS[r])
        pc.set_edgecolor("black")
        pc.set_alpha(0.5)

    medianprops = dict(
        linewidth=2, 
        color="#747473",
        solid_capstyle="butt"
    )
    boxprops = dict(
        linewidth=1, 
        color="#747473"
    )
    #throw a boxplot on it to show quantiles
    ax.boxplot(
        ydata,
        positions=POSITIONS, 
        showfliers = False, # Do not show the outliers beyond the caps.
        showcaps = False,   # Do not show the caps
        medianprops = medianprops,
        whiskerprops = boxprops,
        boxprops = boxprops
    )

    #Adjust x ticks / labels
    ax.set_xticks(POSITIONS)
    labelsformatted = [f"{opendb.target_dict.get(label)}\n{ydata[idx].shape[0]}" for idx, label in enumerate(top5)]
    ax.set_xticklabels(labelsformatted, rotation=-25)

    #Adjust y ticks / labels
    ax.set_ylabel("Hours")

    #Add horizontal dash lines at the y labels
    HLINES = ytick_labels = ax.get_yticks().tolist()
    for h in HLINES:
        ax.axhline(h, color="#747473", ls=(0, (2, 2)), alpha=0.6, zorder=0)

    # Old code for adjusting tick labels.  Yielded wierdly formatted intervals
    # ytick_labels = ax.get_yticks().tolist()
    # labelsformatted = [support.convert_time_format(y) for y in ytick_labels]
    # ax.set_yticks(ytick_labels)
    # ax.set_yticklabels(labelsformatted, rotation=0)

    ax.set_title(f"Top {howmany} fastest {event_col} countries")

plt.suptitle("2019 Ironman Kona Results", y=0.95, ha="center", va="center", size=30)
plt.show()

#TODO - Update y axis on the  mini graphs to have even intervals.  not the time wierdness that it is. 
#TODO - Add dashed ahlines to highlight hours
