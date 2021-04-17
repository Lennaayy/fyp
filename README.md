# Q-Learning Crossblock Solver

Welcome to my Final Year Project, Reinforcement Learning on Puzzle Games

## Installation Guide

### Game

Crossblock is a flash game which is no longer supported by browser, instead it can be downloaded for free along with many flash games through Project Flashpoint.

Download the [Flashpoint Infinity 9.0 exe](https://bluemaxima.org/flashpoint/downloads/), and extract it into a folder of your choosing.

In the newly extracted Flashpoint Infinity 9.0 folder, you may start the application either through the shortcut, or by going into Launcher/Flashpoint. 

From here, Crossblock can be found by selecting games in the menu bar and searching "Crossblock".

Click on the search result for Crossblock and launch the game by pressing the green "Play" button on the right. 

### Environment

My python environment can be recreated exactly using the [Conda package manager.](https://www.anaconda.com/products/individual#Downloads)

Follow the installation guide, making sure to tick **"Add Anaconda3 to my PATH environment variable"** in Advanced Options, otherwise it will need to be added manually.

Once completed, open up cmd.exe (may require a restart first for PATH to update) and navigate to the fyp directory where the *environment.yml* is stored.

```bash
cd C:\Users\User\Path-to-fyp\
conda activate 
conda env create -f environment.yml
```

The environment is now installed, you can ensure it matches the *environment.yml* file by comparing it with the output of:

```bash
conda activate fyp 
conda list
```

## Usage

After the installation of the game and environment, I'd recommend using the [Visual Studio Code IDE](https://code.visualstudio.com/) to run this program.

First, open the project folder in VSC.

Second, select the *fyp* python environment by pressing **Ctrl+Shift+P**, Python: Select Interpreter, and pressing the *fyp* conda environment.

Thirdly, open the game through the Flashpoint application, and press the "play" button to start puzzle 1/50. You may turn off the music here in the top-left if you like.

Finally, to run the program open VSC, ensure both the game and VSC are on the same screen, navigate to *src/main.py* and click the run button in the top-right corner.

If you wish to terminate the program at any time, hold the **q** key, though this cannot interrupt the computer vision library pipeline at the start of each level which can take 1-5 seconds. 

### Each level will start automatically, and is terminated upon completion of the game (10-15 minutes total).
