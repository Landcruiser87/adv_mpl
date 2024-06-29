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

opendb = support.grab_dataset(45103)

inspect(opendb)
#Select numeric columns
numcols = opendb.data.select_dtypes("number").columns.tolist()
support.view_allcols(opendb.data)
support.sum_stats("number", "Numeric Variable Summary", opendb.data)

#  Gridspec

#%%


