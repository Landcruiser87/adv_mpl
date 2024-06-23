#%%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.patches import ConnectionPatch
import support

#%%[markdown]
#
## Matplotlib!  (Part 1)

#### The only graphing library you'll ever need.
#### By Andy Heroy (6/25/24)
# 

# Given its age and maturity.  Matplotlib has been around for quite some time
# and provides over 70k lines of code supporting almost any graphing initiative
# that you may have and / or want to explore.  Its incredibly dense
# documentation, that is also somewhat outdated, is quite good once you
# understand how they structure their information.  As a reference, 
# many of the subjects / images from this talk come from this reference on
# [RealPython](https://realpython.com/python-matplotlib-guide/). They make
# excellent articles and are worth the subscription if you'd like to beef
# up your python skills quickly. 
#
#
# But~!  I digress, lets dive right in and examine the mentality one might adopt when 
# building up a matplotlib chart.  First, an inspirational link for you all. 
# [Look at this graph](https://youtu.be/sz2mmM-kN1I?si=oy-Dl0wIc6fENHHa)

### Plan

# 1. HAVE A PLAN. Or at least some idea of what you want to make.  My go to
#    reference for chart inspiration is [Python Graph
#    Gallery](https://python-graph-gallery.com/).  An excellent resource with
#    tons of really well made charts and supporting code.  Add it to your
#    bookmarks as its one reference I use daily. 
# 2. Use drawio or some other sketching tool to make an outline
# 3. Build each indvidual component (and its interactivity) piece by piece and
# layer them into one figure.  Just like ggplot, matplotlib works in an object
# oriented format.  At the base of every object is usually an `Axes` object.
# Those act as containers for whatever thing you want to layer into it.  
# 
#
# So!  Lets start with the basic outline of a plot. 
#
#
# ![Objects](https://realpython.com/cdn-cgi/image/width=385,format=auto/https://files.realpython.com/media/fig_map.bc8c7cabd823.png)

#
# As you can see, we've got the `figure` as the main container, with 
# an `Axes` object under that.  But then `two more Axes` objects beneath that
# to make up our X and Y Axis.  Everything in matplotlib is layered this way,
# in an `object oriented` fashion.

#%%[markdown]

## Anatomy
#
# Now within those Axes, there's certain properties of the chart that we also
# have access too.  Usually rooted in whatever `Axes` the object resides, there's always a 
# method to either access the current values.  Or set them. For an excellent anatomy of a plot. 
# please refer to the image below. 
#
# ![Anatomy](https://realpython.com/cdn-cgi/image/width=500,format=auto/https://files.realpython.com/media/anatomy.7d033ebbfbc8.png)
#
# As illustrated in the plot, you can see various objects that are layered 
# on top and tied to each axes object.  For example. 
# 1. `Y axis Label`, `Y Major tick label`, `Y Minor tick`, `Y Major tick`, are all connected to the `Y-Axis` object
# 2. The `Line plot`, `Markers`, and `Legend` are all tied to the main `Axes` object. 
#
# Each of these pairings exist in different levels of the chart, and the methods you have access to depend on where you are in that reference heirarchy. Which brings me to our next subject.
#%%[markdown]

## Figure Reference 
#
#### lazy reference vs object oriented. 
#
# In matplotlib, you have two ways to build up plots.  One, you can use the `matplotlib.pyplot` or `plt` to reference the `current chart` or `Axes` object.  
# Initially, this is how all learn to plot with matplotlib but leads to confusion down the road when you want to build more advanced visualizations.  
# These calls looks like. 

#%%
fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 8))
rand_arr = np.random.randint(low=5, high=10, size=(10,2))
plt.plot(rand_arr[:, 0], label="random 1")
plt.plot(rand_arr[:, 1], label="random 2")
plt.legend(loc="upper left")
plt.title("LOOK AT THIS GRAPH", fontsize=22)
plt.xlabel("Sometimes it really makes me laugh", fontsize=16)
plt.show()

#%%[markdown]
#  
# As you can see, that style of graphing is easy enough.  You can quickly build
# up charts, but one thing you have to remember is that building charts with
# `plt` as a reference is it `always references/ties you to the last chart
# object you created.` So while you have access to both the `fig` and `ax`
# objects / variables from the `plt.subplots` return, by referencing `plt` you
# are referencing the `last chart that you built` which is the look at this
# graph chart. This is maintainable for small scale charts, but as soon as 
# 
# ```you start layering items, you need a variable reference to them.```
#
# This is why `I highly suggest` you use `object oriented programming` to create
# a proper reference to the item you wish to manipulate.  Ultimately this gives
# you more control over each object, and lowers the computational requirement
# when matplotlib doesn't have to call mutiple methods to find whatever the last
# object you referenced was.  
# 
# 
#### NOW LETS GRAPH
#
# So for starters, lets begin with the suggested OO approach to creating a matplotlib chart. 
#
# `fig, ax = plt.subplots(ncols=1, nrows=1, figsize=(10, 8))`
#
# What this does is creates a plot with the flexibility to create different
# layouts depending on what you need to display. You'll wind up with two refences.  
#
# - `fig` -> which is the backbone of the plot and sits at the bottom of the stack.
# - `ax` -> which sits on top of fig, but is tied to it.  Meaning commands will cascade down to their intended object if referenced correctly
#
# Armed with that knowledge, we can now begin to assemble items in the manner we want.  
# So for a starter graph, #TODO 
# 
#%%
# 43008 uci heart
opendb = support.grab_dataset(43008)

#Check columns
opendb.data.columns.to_list()
#number or object

numcols = opendb.data.select_dtypes("number").columns.tolist()

#Loop through and print individual plots 
for col in numcols:
    fig, ax = plt.subplots(ncols = 1, nrows = 1)
    ax.hist(opendb.data[col])
    ax.set_title(f"{col}")    
    plt.show()

support.sum_stats("number", "Number Stuff", opendb.data)


#%%[markdown]

# Now , that's a nice way to loop individual columns to take a look at
# histograms.  What if we tried to put it all on a grid? How would i reference
# each axis then? Luckily, matplotlib has an intelligent way it maps out how
# each axis is controlled.   There's a few different ways to do this and i'll
# show you them all!
#
#### 1st way. Direct axis reference. 
#
# This is honestly the way I go most of the time when wanting to have a direct 
# variable for the axes.  Say, we wanted to look at a 3 x 2 grid to assign 
# values for plots.  You can either create multiple axis at the start of a plot
# `fig, (ax1, ax2, ax3) = plt.subplots(ncols=3,ncols=2)`

#%%
fig, (ax1, ax2, ax3) = plt.subplots(
    nrows=3, 
    ncols=2, 
    figsize = (10, 8),
    height_ratios=[1, 3, 2],# Adjust the height ratios of the rows on the grid
    # layout = "constrained" #adjusts hspace and wspace automatically.  Done
    # below manually because constrained layout doesn't play well with the
    # ConnectionPatch according to their docs.  
)
plt.subplots_adjust(wspace=0.1, hspace = 0.7)
idx, ax_count = 0, 0
for ax in [ax1, ax2, ax3]:
    ax[0].hist(opendb.data[numcols[idx]], label=numcols[idx])
    ax[0].set_xlabel(numcols[idx])
    ax[0].set_title(f"Ax[{idx}]")
    ax[0].legend(loc="upper left")
    idx += 1
    ax[1].hist(opendb.data[numcols[idx]], label=numcols[idx])
    ax[1].set_xlabel(numcols[idx])
    ax[1].set_title(f"Ax[{idx}]")
    ax[1].legend(loc="lower left")
    idx += 1

    #Calculate the midpoint of each pair of side by side graphs.
    # Do so by accessing the get_xlim, and get_ylim methods

    x_midA = sum(list(ax[0].get_xlim())) // 2
    y_midA = sum(list(ax[0].get_ylim())) // 2
    x_midB = sum(list(ax[1].get_xlim())) / 2
    y_midB = sum(list(ax[1].get_ylim())) / 2
    s_coordsA = (x_midA, y_midA)
    s_coordsB = (x_midB, y_midB)

    #Create the arrow patch
    special_arrow = ConnectionPatch(
        xyA=s_coordsA,
        xyB=s_coordsB,
        coordsA=ax[0].transData,
        coordsB=ax[1].transData,
        arrowstyle="-|>",
        color="magenta",
        mutation_scale=50,
        linewidth=5,
    )
    #apply it to the figure
    fig.patches.append(special_arrow)
    #Little counter for the axis we're on
    ax_count += 1
    #Maka da text annotation!
    ax[1].annotate(
        text = f"Ax{ax_count} variable",
        xy=(0.5, 0.7), 
        textcoords="axes fraction",
        xytext=(0.65, 0.4),
        color = "green",
        ha='center',
        fontweight="bold",
        annotation_clip=False
    )
    

plt.suptitle("Numerical Variable Exploration", size=20)
plt.show()

#%%[markdown]
# For every row you create, that's the entire axis that it
# spans across.  So if its a 3 x 2 grid.  if you're lookpi
####Eventual Heatmap finisher

    # cols = [ "avg_spo2", "sleep_score", "sleep_deep", "sleep_efficiency",
    #   "sleep_latency", "sleep_rem", "sleep_restfulness", "sleep_timing",
    #   "sleep_total", "read_score", "read_tempdev", "read_tempdev_trend",
    #   "read_act_bal", "read_body_temp", "read_hrv_bal", "read_prev_day_act",
    #   "read_prev_night", "read_recover_idx", "read_resting_hr",
    #   "read_sleep_bal", "act_score", "act_active_cal", "act_avg_met_min",
    #   "act_eq_walk_dist", "act_non_wear_time", "act_resting_time",
    #   "act_sed_time", "act_sed_met_min", "act_steps", "act_target_calories",
    #   "act_total_calories"]

    # #Make correlation chart
    # fig, ax = plt.subplots(figsize=(16, 12))
    # mask = np.triu(np.ones_like(oura_dt['data'].corr(), dtype=bool))
    # heatmap = sns.heatmap(
    #     data = oura_dt['data'].corr(),
    #     ax = ax,
    #     mask=mask,
    #     vmin=-1, 
    #     vmax=1,
    #     annot=True, 
    #     annot_kws={
    #         'fontsize':6,
    #     },
    #     xticklabels=cols,
    #     yticklabels=cols,
    #     fmt='.1f',
    #     cmap='RdYlGn')

    # heatmap.set_title('Correlation Heatmap', fontdict={'fontsize':40})
    # plt.xticks(size=8, rotation=-90)
    # plt.yticks(size=8,)
    # plt.show()'