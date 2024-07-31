# %%
#Import your libs!
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.patches import ConnectionPatch
from matplotlib.lines import Line2D
import support
from rich import inspect

#%%[markdown]
## Matplotlib! (Lecture 2)
#
#### Debuggin and Gridspec
#### By: Andy Heroy (6/25/24)
# 
# 
# For our second talk regarding *matplotlib*, we'll dive into two very important
# aspects of developing super cool plots.  First will be the `native debugger`
# that's built into your IDE.  We'll be specifically going over VSCode's
# debugger although the methodology for other IDE's should be similar. Then, we
# will dive into `GridSpec` object in matplotlib. Which utilizing some of our
# knowledge from the last lecture, will make sense in how the object defines its
# layouts for visualizations.  
# 
#
# As an overview, our talk tonight will be sectioned into 3 main parts. 
#
### 1. Debugger
### 2. GridSpec
### 3. Example 1


#%%[markdown]

### Debugger
#
# So!  First up is our trusty friend the debugger who allows us to run code and
# stop it in certain places.  There are other options such as `pdb.settrace` but
# we'll address that option later in the talk.  
# 
# To launch the debugger, you'll want to hit ``F5``
#
# If its the first time launching the your debugger, you'll get a prompt from
# VSCode `asking if you want to create a launch.json file.`  Why of course you
# do! Its really just a few lines to direct where the debugger needs to access
# the virtual environment you've hopefully stored in the root of your folder.  
# Otherwise you can paste in these parameters into a json file in your `.vscode`
# folder in your root directory.  (Copy from the source py file for indentation)
#
#For detailed documentation on the debugger, check out [this link](https://code.visualstudio.com/docs/editor/debugging)
#%%[markdown]
#
#     {	"version": "0.2.0",
#     "configurations": [
#         {"name": "Python: Current File",
#          "type": "python",
#          "request": "launch",
#          "program": "${file}",
#          "console": "integratedTerminal",
#          "python.formatting.provider": "black",
#          "python.linting.enabled": true,
#          "files.autoSave": "afterDelay",
#          "files.autoSaveDelay": 10000,
#         }
#     ]
#     } 
#
#%%[markdown]
# They really don't change much and you can put whatever file linters or type
# checking devices in there to run whenever you launch the debugger.  
# So! We've launched the debugger but now how do we stop it at a certain 
# line in our code???

#%%[markdown]

#### Breakpoints

# These fun little whackadoodles look like little stop signs you can put to the
# left of the line number in your code.  What these do is `stop the code` when
# it reaches, you guessed it, that stop sign!  This is extremely useful because
# once you've stopped code, you can inspect variables, trace errors. Investigate
# a bug, test code that may not be working yet, and so much more. It is VERY
# useful in developing graphs because often the object methods you want or
# difficult to track and / or use depending on how complex your graphing
# structure has grown.  
#
#
# ![breakpoints](./results/lecture_2/images/breakpoints.png)
#
#

#%%[markdown]
#
#### Navigation and debugging utilities

# Now that we've got the ability to stop our code at some point in the process, 
# now we need to figure out how to operate the debugger to perform certain actions
# when inspecting our code.  First off, The debugger tab can be located here.  
#
# ![debugger icon](./results/lecture_2/images/debugger_icon.png)
#
# We've set breakpoints, we launch the debugger by hitting F5. This will launch
# the debugger and run our code until it hits said breakpoint.  (If there
# weren't any breakpoints set, the code would just run and shutdown if there
# weren't any errors).  Once we hit that breakpoint, the program will pause and
# give you these main tabs as well as a new navigation bar to run the debugger
# with your mouse.  I prefer to run them with my keyboard. Here's what it all
# should look like after you hit a breakpoint
#
# ![debugger](./results/lecture_2/images/debug_nav.png)
#
# Now for navigation.  You have 6 different options. (from left to right in the above image)
# | Methods | Keyboard | Description |
# | :--- | :---: | :--- |
# | Play        | (F5)            | Launches debugger, also runs code until next breakpoint
# | Step Over   | (F10)           | This will step over a line of code if it isn't working correctly so you can continue to run partially broken code
# | Step Into   | (F11)           | This means you step line by line or into a function (slowest but sometimes necessary)
# | Step Out    | (Shift+F11)     | This will step you out of a function
# | Restart     | (Ctrl+Shift+F5) | Reloads the debugger
# | Stop        | (Shift + F5)    | Stops the debugger. 
#
# All of these functions have their various purposes but the ones you will
# probably use the most are F5 and F11.  These are the main operations if you set
# decent breakpoints in your code and will utlimately be what you use to
# navigate your code quickly and efficiently.  
# 

#%%[markdown]

#### Debugger Functions
#
# Now that we've discovered navigation, lets go over some of the tools we have
# at our disposal . In the image below you'll see the layout of a normal
# debugging session.  Each of the main sections/tools are circled.
#
# ![debugger](./results/lecture_2/images/debug_funcs.png)
#
#

#%%[markdown]
#
### VSCode Debugging Panels/Tabs
#
# Our four tabs / functions at our disposal are:
#
# | Name | Description |
# | :---: | :--- |
# | Watch      | You can type in custom variables (and small functions) you want track!  Fun!|
# | Variables  | Shows you all the variables at a global and local scope|
# | Call Stack | Shows you how to back trace your function to where it was called from|
# | Breakpoints| Shows you the location of all the breakpoints in any file in your root dir|
# 
# Each of these tabs has a specific purpose.  Sometimes you'd want to track
# specific variables, so you navigate to the `watch` tab, hit the little plus
# sign to `add an expression`, then see them populate as you pass their
# reference in the code.  Other times you can monitor your `global` or `local`
# variables depending on what scope you're in, so in that case you'd use the
# `variables` tab.  As a reminder.  Global variables will be available to the
# entire program as it runs, (increasing overhead if you have too many) and
# `local` variables are only available at the current function level. Which is
# also good to know because it can sometimes be confusing to track which
# variables are available to what part of the program.  These you can trace with
# the `call stack` tab and click your way back to where you started.  The `call
# stack` and `breakpoints` tabs you probably won't use as much.  But the
# breakpoints tab can be useful sometimes to deselect certain breakpoints from
# stopping if you don't want to keep going back to set and unset them each time
# with the stop sign. To temporarily disable a breakpoint just uncheck the blue
# box and it will just be an greyed out circle as opposed to a red circle. 
# 
# Ok!  Now that we've established navigation and functions.  We can to begin to
# inspect our variables at runtime.  Say I'm working on the `support.py` file
# and I want to inspect the object after its created.  How do i do that???
# First, set a breakpoint where you want the code to stop, and then hit F5!! But
# hit F5 while you're in this `2_gridspec_chunked_file.py`.  The cool thing
# about having all your support files in the same directory of scripts, as that
# you can directly import their functionalities into your code.  Professsional
# developers do this all the time, and its honestly a much easier way to
# maintain a codebase, rather than one gimungus py file that can also double as
# a space telescope its got so much code in it.  Break up your code. You'll
# thank yourself later when you're debug tracing and you only have to scan 3
# lines of code vs. 3000
# 


#%%
#Load dataset into memory
opendb = support.grab_dataset(43482)

# Use rich to inspect the object
inspect(opendb)
# Use dir to inspect object components
dir(opendb)
#Look at the object variables we created 
list(dir(opendb))[-6:]

#List out our available columns and types
support.view_allcols(opendb.data)

#%%[markdown]
#
# You can see now that the program has stopped at line 139 and is awaiting our
# next instruction.  Since we want to look at the head of our dataframe
# to ensure its been imported correctly.  

# ![Stopped program](./results/lecture_2/images/debug_139.png)
#
# Now, we can click through each of those objects in the `locals` or `globals` scale and 
# be able to inspect each of the objects we have available.  
# ![DF Columns](./results/lecture_2/images/debug_140.png)
#
# This is a great way to start to get know the variables you have at both
# viewpoints within your program.  Feel free to click and break as much as you
# want because the program is in a paused state.  But say you want to run a
# small function or test some code with all those variables loaded?  Why.  Look
# no further than your `Debug Console~!`.  This little beauty is a subroutine
# that has an active python interpreter for you to toy with whatever you want
# too.  Test some code, you'll get the same errors. You can think of it as
# `REPL` on steriods. Its honestly the best way to go for development in general
# because you have all your tools at the exact time in the program you need to
# change something.  You can view a variable as you change it on the `variables`
# or `watch` panel at the left. Its full control over the program with as much
# or as little as you want to do at the moment. 
#
# So for example, if we advanced our previously paused program to this point, we
# could test the opendb object we created at runtime to import our dataset and
# other features.  Another useful shortcut you should consider is mapping a
# shortcut to set your focus to the Debug Console.  I've mapped my IDE to
# `CTRL+ALT+C`for this.  It will help in the long run when you don't want to
# have to take your ahnds off the keyboard to run a small function. (Yes we get
# that lazy.  Lol)  To do this hit, `CTRL+SHIFT+P` to launch the command
# pallette and type in `Open Keyboard Shortcuts`.  Then type in `Debug: Focus
# on` and select the first option that should say `Debug: Focus on Debug
# Console`.  From there enter in your key mapping and you're good to go!
# 
#
#%%
print("I'm here to pause your code")

[x for x in opendb.data.columns]
im_gp = opendb.data.groupby(by="Country")
swims = im_gp["Run"].mean().sort_values()
fullnames = list(zip(swims.index.map(opendb.target_dict), swims))
[name for name in fullnames]
[f'{name[0]:_<18} Time:-> {support.convert_time_format(int(name[1]))}' for name in fullnames]


#%%[markdown]
#
# If you want to lean more about f strings, Here is a good resource.
#
# [fstring help](https://fstring.help/)
#
#
# ![DF Columns](./results/lecture_2/images/debug_141.png)
#
# Now you can start typing in functions and begin to inspect your objects at
# runtime.  Here we're looking at the dataclass I've created with different types
# of objects for different purposes within this analysis.  Trust me this is a
# very powerful technique that will always be helpful.  Because half the time
# your code breaks and you need a way to diagnose it.  This is the best way I've
# found. There are other options you can explore with the library `pdb` (Which
# ships with python)
#
# [pdb docs](https://docs.python.org/3/library/pdb.html)
#
# The premise of usage with this library is mostly the same, except instead of
# using the IDE to configure breakpoints and set them.  You do it manually
# (writing code) within the code to stop and inspect various objects.  This is
# very useful if say you're debugging code that's sitting up in a server that
# you may not be able to connect your IDE too. So as always, its good to know
# all ways of how to do things!  Alot of people still use this method! (Dr.
# Santerre included), but I've found that VSCode's native debugger has more
# capabilities and options that help me develop faster / write cleaner code.  So
# as with any new tool that we may include in our stack.  Try both!  See which
# one fits your coding style more and use it going forward.  Being able to
# pause and inspect your code is a vital skill, one that will help you
# understand whats happening in your routines at all times. 
#
#
#%%[markdown]
# ![Questions?](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNGgzbTNoMmd0bTJwaXh4Y2ExanphOGQ5c3JjNjRuaTk2d2dwd2RxaiZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/xT5LMB2WiOdjpB7K4o/giphy.gif)
#
#
#%%[markdown]
#
### Gridspec 
#
# In our previous lesson, we were using `plt.subplots` to generate different
# size and style of layouts.  We had used the `ax` objects we created for each
# axis to design and draw our plots but what if I want to have subplots that
# span across different sections to make interesting, eye catching layouts?  Is
# there such an object we can use for that???? YES~!!!  I'm very excited to
# tell you about on the wonders of `Gridspec` object. 
# 
# - [Gridspec Docs](https://matplotlib.org/stable/api/_as_gen/matplotlib.gridspec.GridSpec.html)
# - [Basic Example](https://matplotlib.org/stable/gallery/subplots_axes_and_figures/gridspec_multicolumn.html#sphx-glr-gallery-subplots-axes-and-figures-gridspec-multicolumn-py)
#
# Think of the Gridspec object like a more refined way to label and access the
# axis of what you want to graph.  Say for instance we wanted to take our
# ironman dataset and create a graph of the top 20 teams total times on the left
# in one column as a stacked bar chart. Then we could make smaller, individual
# violin plots of the top countries for each individual sport of the triathlon.
# This would help us visualize and answer not only which countries were fastest
# overall, but also which country's excel at which sport. We'll also include the
# counts for each country in the x labels.  To create this layout with the
# gridspec object, its as easy as selecting the right slices of the graph that
# you want to create.  So to create this object, we'll use the same inputs as we
# would for `plt.subplots`.  But call them into the gridspec object. So our
# chart will be
#
# - nrows = 3
# - ncols = 2
# - height_ratios = [1, 1, 1]
# - hspace = 0.5
#
# `height_ratio` controls the relative height of each subplot.  This also
# depends on how many rows you have in your chart.  So if mapping allows, it
# will adjust the height of the individual row to match the scale of how much
# difference you want in the height of your subplots. [1, 1, 1] would all be the
# same height.  [0.5, 1, 1.5] would be (from top down) half the relative height
# all the way up to 1 and a half the relative height.   
#
# `hspace` gives you way way to increase the relative spacing in between each of
# the plots. Lets start with the basic layout and build it up from there. to add
# a chart to a Gridspec object, we'll use the `fig.add_subplot` method. The
# inputs for which are the sliced ranges of how each chart should span the Total
# plot.  So for the leftmost column chart, we want all of the first column, We
# know its got a total of 3 rows, so, that would look like. 
#
# - `gs[:3, 0]`  Up to the third row, in the first column.
#
# For the bottom right subplot,  It would be the last row, last column, 
# which knowing we have 2 columns would look like. 
# - `gs[2:, 1]` or `gs[2, 1]`
# 
# `You can directly index, or slice your selections for how you want 
# your layouts to look.` 
# 
#%%

#Create fig container
fig = plt.figure(figsize = (12, 10))

#Create gridspec object
gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 1], hspace=0.5)

#Far left axis
ax_one = fig.add_subplot(gs[:3, 0], label="stack_country")
# ax_temp = fig.add_subplot(gs[2:3, 0], label="stack_country_temp")

#Top right axis
ax_two = fig.add_subplot(gs[:1, 1], label="swim")

#mid right axis
ax_three = fig.add_subplot(gs[1:2, 1], label="bike")

#low right axis
ax_four = fig.add_subplot(gs[2:, 1], label="run")

#Can also adjust horizontal spacing of subplots at the global plt level with code below.
plt.subplots_adjust(hspace=0.1)
# 

#%%[markdown]
# Now that we've got our basic structure up.  We can begin to build each chart
# because we have direct reference to each the axes objects underneath the
# subplots. So.  First we will start with stacked barchart on the left. To begin
# this section, first we need to do a little house cleaning with the data. Due
# to some countries having less participants than others.  
# 
# Lets put a lower limit on countries that have more than 10 people representing
# their country. That way we can be somewhat confident we don't have any smaller
# countries with very fast individuals that might influence the results in their
# favor.  We will also combine the two transition times for a total transition
# time.  This is because when viewing much longer times for each of the
# individual sports, you won't be able to see either transition time beecause
# they are relatively much smaller than the sport time.
# 
#%%

#Create fig container
fig = plt.figure(figsize = (12, 10))

#Create gridspec object
gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 1], hspace=0.5)

#Far left axis
ax_one = fig.add_subplot(gs[:3, 0], label="stack_country")
# ax_temp = fig.add_subplot(gs[2:3, 0], label="stack_country_temp")

#Top right axis
ax_two = fig.add_subplot(gs[0, 1], label="swim")

#mid right axis
ax_three = fig.add_subplot(gs[1, 1], label="bike")

#low right axis
ax_four = fig.add_subplot(gs[2, 1], label="run")

#Copy the dataset and begin data cleaning
ironman = opendb.data.copy()
ironman["Transitions"] = ironman["T1"] + ironman["T2"]
graphcols = ["Swim", "Bike", "Run", "Overall", "Transitions"]

# Make an empty dataframe to fill
iron_df = pd.DataFrame(
    data = np.zeros(shape=(len(opendb.target_dict),len(graphcols))),
    index = sorted(opendb.target_dict.keys()),
    columns=graphcols
)
##############################  stacked bar ##############################

# Create means for each country over 10 participants
# Set the minimim amount of records we need for an average
# Have to manually calculate averages because groupby was being a PITA if some
# countries have null values.

min_records = 10
for col in graphcols:
    for country in iron_df.index:
        #Have at least 10 race participants for that country
        if ironman[ironman["Country"]==country].shape[0] > min_records:
            countrymean = ironman[col][ironman["Country"]==country].mean()
            iron_df.loc[country, col] = round(countrymean, 1)
        else:
            iron_df.loc[country, col] = np.nan

#Drop the nan countries (countries with fewer than 10)
iron_df.dropna(inplace=True)

#sort em by overall time
iron_df.sort_values(by="Overall", axis=0, inplace=True, ascending=True)

#Get rid of that col because we don't want to graph it. 
iron_df.drop("Overall", axis=1, inplace=True)
graphcols.pop(graphcols.index("Overall"))

#rearrange the cols
iron_df = iron_df[["Swim", "Bike", "Run", "Transitions"]]

#subset t20 countries overall
iron_df_s = iron_df.iloc[:20, :]

#Make a list of them
countries = list(iron_df_s.index)

#Generate a color pallette equivalent number of columns
#we want to graph
colors = list(sns.color_palette(palette="tab10", n_colors=len(graphcols)))
#if you want to use mpl
# category_colors = plt.colormaps['RdYlGn'](np.linspace(0.15, 0.85, iron_df.shape[1])) 

#Loop through a zip of graphcols and colors 
for i, (co_name, co_color) in enumerate(zip(graphcols, colors)):
    #Set the base of the stacked bar
    widths = iron_df_s.iloc[:, i].astype("timedelta64[s]") / pd.Timedelta(1, "h")
    #Generate the starts for each country and sport as the cumulative sum to that point
    starts = (iron_df_s.iloc[:, :i+1].cumsum(axis=1).iloc[:, -1].astype("timedelta64[s]") / pd.Timedelta(1, "h")) - widths 
    #Generate the horizontal barchart (barh) 
    rects = ax_one.barh(countries, widths, left=starts, height=0.5, label=co_name, color=co_color)
    # Grab the RGB of the sports color
    r, g, b = co_color
    #Set the color of the text.  If its less than 0.5 
    #Note, not sure I need this. 
    # text_color = 'black' if r* g* b < 0.5 else 'white'
    text_color = 'black' 

    #subset any column that's not a Transition. 
    if not "T" in co_name:
        #Custom function for label conversion from seconds to hours:min:seconds
        f_labels = iron_df_s.iloc[:, i].apply(lambda x:support.convert_time_format(x))
        #If its the swim, use white text so you can see it against the blue backdrop. Otherwise make it black
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
plt.show()

#%%[markdown]
# As you can there's alot that goes that one chart in order to get it into a
# formatted clean version.  Namely, we had to calulate a cumulative start points
# of each countries times for each sport.  Assign bar labels and a bunch of other things, 
# but since we have access to these gridspec objects for our axis.  Its just like
# building any individual chart on its own, you just do it 3 more times for the sub graphs
# to get the information you want.  Or make a for loop!
#
#Here's how the rest of the plot is built. 

#%%
#Create fig container
fig = plt.figure(figsize = (12, 10))

#Create gridspec object
gs = gridspec.GridSpec(nrows=3, ncols=2, height_ratios=[1, 1, 1], hspace=0.5)

#Far left axis
ax_one = fig.add_subplot(gs[:3, 0], label="stack_country")
# ax_temp = fig.add_subplot(gs[2:3, 0], label="stack_country_temp")

#Top right axis
ax_two = fig.add_subplot(gs[0, 1], label="swim")

#mid right axis
ax_three = fig.add_subplot(gs[1, 1], label="bike")

#low right axis
ax_four = fig.add_subplot(gs[2, 1], label="run")
#Copy the dataset and begin data cleaning
ironman = opendb.data.copy()
ironman["Transitions"] = ironman["T1"] + ironman["T2"]
graphcols = ["Swim", "Bike", "Run", "Overall", "Transitions"]
iron_df = pd.DataFrame(
    data = np.zeros(shape=(len(opendb.target_dict),len(graphcols))),
    index = sorted(opendb.target_dict.keys()),
    columns=graphcols
)

##############################  stacked bar ##############################
# Create means for each country over 10 participants
# Set the minimim amount of records we need for an average
min_records = 10
for col in graphcols:
    for country in iron_df.index:
        #Have at least 10 race participants for that country
        if ironman[ironman["Country"]==country].shape[0] > min_records:
            countrymean = ironman[col][ironman["Country"]==country].mean()
            iron_df.loc[country, col] = round(countrymean, 1)
        else:
            iron_df.loc[country, col] = np.nan

#Drop the nan countries (countries with fewer than 10)
iron_df.dropna(inplace=True)

#sort em by overall time
iron_df.sort_values(by="Overall", axis=0, inplace=True, ascending=True)

#Get rid of that col because we don't want to graph it. 
iron_df.drop("Overall", axis=1, inplace=True)
graphcols.pop(graphcols.index("Overall"))

#rearrange the cols
iron_df = iron_df[["Swim", "Bike", "Run", "Transitions"]]

#subset t20 countries overall
iron_df_s = iron_df.iloc[:20, :]

#Make a list of them
countries = list(iron_df_s.index)

#Generate a color pallette equivalent number of columns
#we want to graph
colors = list(sns.color_palette(palette="tab10", n_colors=len(graphcols)))
#if you want to use mpl
# category_colors = plt.colormaps['RdYlGn'](np.linspace(0.15, 0.85, iron_df.shape[1])) 

#Loop through a zip of graphcols and colors 
for i, (co_name, co_color) in enumerate(zip(graphcols, colors)):
    #Set the base of the stacked bar
    widths = iron_df_s.iloc[:, i].astype("timedelta64[s]") / pd.Timedelta(1, "h")
    #Generate the starts for each country and sport as the cumulative sum to that point
    starts = (iron_df_s.iloc[:, :i+1].cumsum(axis=1).iloc[:, -1].astype("timedelta64[s]") / pd.Timedelta(1, "h")) - widths 
    #Generate the horizontal barchart (barh) 
    rects = ax_one.barh(countries, widths, left=starts, height=0.5, label=co_name, color=co_color)
    # Grab the RGB of the sports color
    r, g, b = co_color
    #Set the color of the text.  If its less than 0.5 
    #Note, not sure I need this. 
    # text_color = 'black' if r* g* b < 0.5 else 'white'
    text_color = 'black' 

    #subset any column that's not a Transition. 
    if not "T" in co_name:
        #Custom function for label conversion from seconds to hours:min:seconds
        f_labels = iron_df_s.iloc[:, i].apply(lambda x:support.convert_time_format(x))
        #If its the swim, use white text so you can see it against the blue backdrop. Otherwise make it black
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

############################# violin swim, bike, run #################################
#Subchart data wrangling and plotting
im_df = ironman.copy()

#Iterate in a zipped for loop of the Swim, Bike, Run and its respective axis
for event_col, ax in zip(graphcols[:3], [ax_two, ax_three, ax_four]):
    
    #Filter out any null values for event in question
    im_df = im_df[~im_df[event_col].isnull()]
    
    #Subset Country counts over 10 
    im_df = im_df[im_df['Country'].map(im_df['Country'].value_counts()) > min_records] #over 60 shows USA

    #Groupby Country and calc means
    im_gp = im_df.groupby(by="Country")
    event = im_gp[event_col].mean().sort_values()

    #Subset top number of teams to look at
    howmany = 8
    top_x = event.index[:howmany]

    #Set the positions for each country
    POSITIONS = list(range(howmany))
    #Generate a color from blue to red of fastest to slowest of top X countries
    COLORS = list(sns.color_palette(palette="coolwarm", n_colors=len(POSITIONS)))
    
    #Pull out individual Country data
    sample = im_df[im_df["Country"].isin(top_x)]
    sample.sort_values(by=event_col, ascending=True)
    
    
    #Also reshape into a list of arrays for each countries participant
    ydata = [sample[sample["Country"]==country][event_col] for country in top_x]
    #Resample from seconds to hours.  
    ydata = [y.astype("timedelta64[s]") / pd.Timedelta(1, "h") for y in ydata]

    #Average swim times and voilin plot for distribution
    violins = ax.violinplot(
        dataset=ydata,
        positions=POSITIONS,
        vert=True,
        bw_method="silverman",
        showmeans=True,
        showmedians=False,
        showextrema=False
    )
    #Loop over each of the violins and set their respective color
    for r, pc in enumerate(violins["bodies"]):
        pc.set_facecolor(COLORS[r])
        pc.set_edgecolor("black")
        pc.set_alpha(0.5)
    #Set Median props
    medianprops = dict(
        linewidth=2, 
        color="#747473",
        solid_capstyle="butt"
    )
    #Set boxplot probs
    boxprops = dict(
        linewidth=1, 
        color="#747473"
    )

    #throw a boxplot on it to show quartiles
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
    #Add counts for each country beneath the name
    ax.set_xticks(POSITIONS)
    labelsformatted = [f"{opendb.target_dict.get(label)}\n{ydata[idx].shape[0]}" for idx, label in enumerate(top_x)]
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
    #Create custom Legend
    legend_elements = []
    legend_elements.append(Line2D([0], [0], color="royalblue", alpha=0.8))
    legend_elements.append(Line2D([0], [0], linewidth=2, color="#747473", alpha=0.8))
    labels = ["mean", "median"]
    ax.legend(handles=legend_elements, labels=labels, loc='upper right')

plt.suptitle("2019 Ironman Kona Results", y=0.95, ha="center", va="center", size=30)
plt.show()

#%%

# That is about it!  
# Thank you all for coming and please ask me any questions.  
#
# ![Thank you!](https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExZnpra3phNXBybmM2N2JqOXBoM2Q1MGo3ODhzaW9wY3g3YTgxZmtrcCZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9Zw/Jk4Sucdz1oGd2/giphy.gif)
