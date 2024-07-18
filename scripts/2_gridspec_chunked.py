#%%[markdown]
## Matplotlib! (Lecture 2)
#
#### Debuggin and Gridspec
#### By: Andy Heroy (6/25/24)
# 
# 
# For our second talk regarding *matplotlib*, we'll dive into two very important
# aspects of developing and testing code in general.  First will the `native
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
# To launch the debugger, first you'll want to hit ``F5``
#
# If its the first time launching the your debugger, you'll get a prompt from
# VSCode `asking if you want to create a launch.json file.`  Why of course you
# do! Its really just a few lines to direct where the debugger needs to access
# the virtual environment you've hopefully stored in the root of your folder.  
# Otherwise you can paste in these parameters into a json file in your `.vscode`
# folder in your root directory.
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
# Our four main sections are:
#
# | Name | Function |
# | :---: | :--- |
# | Watch      | You can type in custom variables (and small functions) you want track!  Fun!|
# | Variables  | Shows you all the variables at a global and local scope|
# | Call Stack | Shows you how to back trace your function to where it was called|
# | Breakpoints| Shows you the location of all the breakpoints in any file in your root dir|
