<h1 align="center">
  <b>Advanced Matplotlib Techniques</b><br>
</h1>

<p align="center">
      <a href="https://www.python.org/">
        <img src="https://img.shields.io/badge/Python-3.8-ff69b4.svg" /></a>    
</p>

## Requirements
- Python >= 3.8

## Cloning and setting up environment.
Launch VSCode if that is IDE of choice.

```
`CTRL + SHIFT + ~` will open a terminal
Navigate to the directory where you want to clone the repo. 

$ git clone https://github.com/
$ cd adv_mpl
$ python -m venv .mp_venv
(Or replace .mp_venv with whatever you want to call your environment)	

On Windows
$ .mp_venv\Scripts\activate.bat

On Mac
$ source .mp_venv/bin/activate
```

Before next step, ensure you see the environment name to the left 
of your command prompt.  If you see it and the path file to your current directory, then the environment is activated.   If you don't activate it, and start installing things.  You'll install all the `requirements.txt` libraries into your `base python environment.` Which will lead to dependency problems down the road.  I promise. After that has been activated, go to your terminal and type `pip list` to check your base python libraries.  Now is probably a good time to copy whatever upgrade command you have for upgrading that version of pip. (Good practice) 

Next install the required libraries with the below pip command!

```
$ pip install -r requirements.txt
```

Order of operations of above terminal commands. 
- Open Terminal
- Clone repo
- Change directories
- Create venv
- Activate venv
- Upgrade pip (because reasons)
- Install libraries

## File Setup
While in root directory run commands below
```
$ mkdir data
$ mkdir scripts
```

Copy data to data directory

## Main Outline

#### Intro

1. [x] General overview of how to plot
   - https://realpython.com/python-matplotlib-guide/
#### Gridspec
2. Layering multiple plots on a GridSpec
3. Use of debugger in plotting.  The best trial and error and object exploration
#### All the rest
4. objects
5. Embed ML routines
6. Plot animation
7. Python - graph - gallery
