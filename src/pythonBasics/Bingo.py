#!/usr/bin/python3
import sys, os
sys.path.append(os.getcwd()+'/bingo/')

import UserInterface

def run():
    # Create a UI object and run it
    ui = UserInterface.UserInterface()
    ui.run()
