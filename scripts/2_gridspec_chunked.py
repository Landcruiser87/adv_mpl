#%%[markdown]
## Matplotlib! (Lecture 2)
#
#### Debuggin and Gridspec
#### By: Andy Heroy (6/25/24)
# 
# 
# For our second talk regarding *matplotlib*, we'll dive into two very important
# aspects of developing and testing code in general.  First will be the `native
# debugger` that's built into your IDE.  We'll be specifically going over
# VSCode's debugger although the methodology for other IDE's should be similar.
# Then, we will dive into the ever confusing `GridSpec` object in matplotlib.
# Which utilizing some of our knowledge from the last lecture, will make sense
# in how the object defines its layouts for visualizations.  
# 
#
# As an overview, our talk tonight will be sectioned into 4 main parts. 
#
#### 1. Debugger
#### 2. GridSpec
#### 3. Example 1
#### 4. Example 2

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
# {	"version": "0.2.0",
# 	"configurations": [
# 		{
# 			"name": "Python: Current File",
# 			"type": "python",
# 			"request": "launch",
# 			"program": "${file}",
# 			"console": "integratedTerminal",
# 			"python.formatting.provider": "black",
# 			"python.linting.enabled": true,
# 			"files.autoSave": "afterDelay",
# 			"files.autoSaveDelay": 10000,
# 			"python.linting.lintOnSave": true,
# 			// "justMyCode": false,

# 		}
# 	]
# }
#
#%%

# They really don't change much and you can put whatever file linters or type
# checking devices in there to run whenever you launch the debugger.  
# So! We've launched the debugger but now how do we stop it.  

### Breakpoints

# These fun little whackadoodles look like little stop signs you can put to
# the left of the line number in your code.  What these do is `stop the
# code` when it reaches, you guessed it, that stop sign!  This is extremely
# useful because once you've stopped code, you can inspect variables.
# Investigate a bug, test code that may not be working yet, and so much more.
# It is VERY useful in developing graphs because often the object methods you
# want or difficult to track and / or use depending on how complex your graphing
# structure has grown.  
#
#
# ![breakpoints](./results/lecture_2/images/breakpoints.png)
#
#

#%%[markdown]

### Navigation and debugging utilities

# Now that we've got the ability to stop our code at some point in the process, 
# Next we need to figure out how to operate the debugger to perform certain actions
# when inspecting our code.  First off, The debugger tab can be located here.  
#
# ![debugger icon](./results/lecture_2/images/debugger_icon.png)
#
# So now that we've set breakpoints, we launch the debugger by hitting F5. 
# This will run our code until it hits said breakpoint.  (If there weren't any
# breakpoints set, the code would just run and shutdown if there weren't any
# errors).  Once we hit that breakpoint, the program will pause and give you
# these main tabs as well as a new navigation bar to run the debugger with your mouse.  
# I prefer to run them with my keyboard. Here's what it all should look like after you hit a breakpoint
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

### Debugger Functions
#
# Now that we've discovered navigation, lets go over some of the tools we have
# at our disposal . In the image below you'll see the layout of a normal
# debugging session.  Each of the main sections/tools are circled.
#
# ![debugger](./results/lecture_2/images/debug_funcs.png)
#
#

#%%[markdown]
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
# variables are available to what part of the program.  The `call stack` and
# `breakpoints` tabs you probably won't use as much.  But the breakpoints tab
# can be useful sometimes to deselect certain breakpoints from stopping if you
# don't want to keep going back to set and unset them each time with the stop
# sign. To temporarily disable a breakpoint just uncheck the blue box and it
# will just be an greyed out circle as opposed to a red circle. 
# 
# Ok!  Now that we've established navigation and functions.  We can to begin to
# inspect our variables at runtime.  Say I'm working in the `support.py` file and I want
# make sure I've got even spacing for my table structure.  How do i inspect that?
# First, set a breakpoint where you want the code to stop, and then hit F5!!
# 
# ![breakpoints](./results/lecture_2/images/breakpoints.png)

# %%

import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
from matplotlib.lines import Line2D
import support
from rich import inspect

#%%
#Load dataset into memory
opendb = support.grab_dataset(43482)

# Use rich to inspect the object
# inspect(opendb)
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
#%%[markdown]
# ![DF Columns](./results/lecture_2/images/debug_141.png)
#
# Now you can start typing in functions and begin to inspect your objects at
# runtime.  Here we're looking at my dataclass I've created with different types
# of objects for different purposes within this analysis.  Trust me this is a
# very powerful techinque that everyone needs to know.  Because half the time
# your code breaks and you need a way to diagnose it.  
#%%