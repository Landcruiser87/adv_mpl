import numpy as np
import pandas as pd
import sklearn


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
# have access too.  Usually rooted in whatever axes the object resides, there's always a 
# method to either access the current values.  Or set them. For an excellent anatomy of a plot. 
# please refer to the image below. 

# ![Anatomy](https://realpython.com/cdn-cgi/image/width=500,format=auto/https://files.realpython.com/media/anatomy.7d033ebbfbc8.png)

