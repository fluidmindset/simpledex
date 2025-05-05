
import tkinter as tk #initialize a GUI
from tkinter import *
from tkinter import ttk 
from helpers import pokedex_config as pc

from PIL import Image, ImageTk #python open images
from io import BytesIO #not sure what this does yet

"""
this file is for maintaning the widgets
that are used in main
"""
global pokename, stat
def button_process():
    global pokename, stat, root
    try:
        sd = pc.get_poke_json(pokename.get())
        sd1 = sd['id']
        stat.set(sd1)

    except ValueError:
        pass

#create window
def create_root():
    root = Tk()
    return root

def create_vars():
    pokename = StringVar()
    stat = StringVar()
    return pokename, stat

#create name to search in pokebase
def search_entry(root):
    entry = ttk.Entry(root,textvariable=pokename)
    entry.pack()

def stat_label(root):
    label = ttk.Label(root,text=stat.get())
    label.pack()

def search_button(root):
    button = ttk.Button(root,text='submit', command=button_process)
    button.pack()



# #pokename is the input stringvar to send to api
# #output vars is api response key-value pairs

# #split mainframe into x rows and y columns in grid
# def divide_grid(mainframe, x,y):
#     for i in range(x):
#         mainframe.rowconfigure(i, weight=1)

#     for j in range(y):
#         mainframe.columnconfigure(j,weight=1)

# #create a dictionary of StringVars that will be set
# #using the response of the API Calls. These stringvars
# #are to be assigned to the appropriate cells in the grid
# def create_cell_vars():
#     name_vars = {}
#     for i in range(1,7):
#         for j in range(0,2):
#             name_vars.update({(i,j):StringVar()})
#     return name_vars

# #populates the rows an cols of the grid
# #where the data from the API response will be
# #displayed. the texvariable assigned is from the 
# #output_vars dictionary created in main
# def pop_grid(mainframe,x,y):
#         output_vars = create_cell_vars()
#         for i in range(x):
#             for j in range(y):
#                 if (i > 0, j < 2):
#                     label = ttk.Entry(mainframe,width=7,textvariable=output_vars.get((i,j)))
#                     label.grid(row=i,column=j, padx=10,pady=10,sticky='nsew')

# #places a Entry widget at top center of
# #mainframe window and assigned textvariable
# #to pokename, which will be passed into API call
# def create_namesearch(mainframe, width=7):
#     pokename = StringVar()
#     x = ttk.Entry(mainframe, width=width,textvariable=pokename)
#     x.grid(column=1,row=0,sticky='nsew')  
#     x.focus()  

# #create a button that will be used to send the 
# #stringvar data in pokename to the API 
# #the command function is what starts the API call
# #and sets the StringVar entries of output_vars
# #to reflect the data from API response
# def create_button(mainframe):
#     x = ttk.Button(mainframe,text="Search Pokedex",command=button_process)
#     x.grid(row=0,column=2,sticky='nsew')

# def button_process(*args):
#     global pokename, output_vars,root
#     try:
#         sd = pop_stat_dict(load_pokejson(pokename))
#         for i, (k,v) in enumerate(sd.items()):
#             output_vars.get(i+1,0).set(k)
#             root.update()
#             output_vars.get(i+1,1).set(v)
#             root.update()
            
#     except:
#         pass

# def load_pokejson(pokename):
#     x = pc.get_poke_json(pokename.get())
#     return x

# def pop_stat_dict(pokejson):
#     return pc.poke_stats_dict(pokejson)


# def standard_root(root):
#     root.bind("<Return>", button_process)
#     root.columnconfigure(0,weight=1)
#     root.rowconfigure(0,weight=1)
#     root.title("Pokedex")

# def create_mainframe(root):
#     mainframe = ttk.Frame(root,padding="3 3 12 12" )

# def create_grid(mainframe):
#     mainframe.grid(column=0, row=0, sticky='nsew')



# def pop_stat_labels(mainframe, sd):
#     stat_labels=sd.keys()
#     for i in stat_labels:
#         label = ttk.Label(mainframe,text=i)
#         label.grid(row =sd.index(i)+1,column=0, sticky='nsew')

# def pop_stat_values(mainframe,sd):
#     stat_vals=sd.values()
#     for i in stat_vals:
#         label = ttk.Label(mainframe,text = i)
#         label.grid(row=sd.index(i)+1, column=1, sticky='nsew')


