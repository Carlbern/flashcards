import os
clear = lambda: os.system('clear')

def trySelection(selection):
    try:
        selection = int(selection)
        return selection
    except:
        clear()
        hold = input("Invalid input, press enter to continue.. ")