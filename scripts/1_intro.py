import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


#%%[markdown]
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
# building up a matplotlib chart.  

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

# ![Anatomy](https://realpython.com/cdn-cgi/image/width=500,format=auto/https://files.realpython.com/media/anatomy.7d033ebbfbc8.png)
#
# As illustrated in the plot, you can see various objects that are layered 
# on top and tied to each axes object.  For example. 
# 1. `Y axis Label` + `Y Major tick label`, `Y minor tick`, `Y Major tick`, are all connected to the `Y-Axis` object
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
rand_arr = np.random.randint(low=5, high=10, size=(10,2)) + np.random.random((10,2))
plt.plot(rand_arr[:, 0], label="random 1")
plt.plot(rand_arr[:, 1], label="random 2")
plt.legend()
plt.title("LOOK AT THIS GRAPH", fontsize=22)
plt.xlabel("Sometimes it really makes me laugh", fontsize=16)
plt.show()

#%%[markdown]
#  
# As you can see, that style of graphing is easy enough.  You can quickly build
# up charts, but one thing you have to remember is that building charts with
# `plt` as a reference is it `always references you to the last chart object you
# created` you called to create. So while you have access to both the `fig` and
# `ax` objects / variables from the `plt.subplots` return, by referencing `plt`
# you are referencing the `last chart that you built` which is the look at this
# graph chart. 