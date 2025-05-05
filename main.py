from helpers import pokedex_gui as pg
from helpers import pokedex_config as pc
import tkinter as tk
from tkinter import ttk, font

class NameToStats:

    def __init__(self, root):

        window_color='lightblue'
        root.title("Mic's Pokedex")
        default_font = font.nametofont("TkDefaultFont")
        default_font.configure(family="Dubai Medium", size=20)
        root.configure(bg=window_color)

        self.sprite=tk.Label(root, bg=window_color)
        self.sprite.pack(side=tk.LEFT)

        self.pokename = tk.StringVar()
        poke_entry = tk.Entry(root, textvariable=self.pokename,font=default_font, justify='center')
        poke_entry.pack()
        tk.Button(root, text="Get Stats", command=self.calculate).pack()

        self.poketype=tk.Label(root,bg=window_color)
        self.poketype.pack()

        self.stat_labels =[]
        self.stats_to_show=[
            "hp",
            "attack",
            "defense",
            "special-attack",
            "special-defense",
            "speed",
            "base stat total"
            ]
        for i in self.stats_to_show:
            x = tk.Label(root, bg=window_color)
            x.pack()
            self.stat_labels.append(x)
        
        

        poke_entry.focus()
        root.bind("<Return>", self.calculate)
        
    def calculate(self, *args):
        root.geometry("")
        try:
            #get pokemon json data
            value = self.pokename.get().lower()
            x = pc.get_poke_json(value)

            #set type label text
            typetext=pc.poke_type(x)
            self.poketype.configure(text="type: "+typetext)

            #set stat label text
            y = pc.poke_stats_dict(x)
            for i, (k,v) in enumerate(y.items()):
                self.stat_labels[i].configure(text=k+": "+str(v))
            
            #set sprite image
            pokesprite= pc.poke_sprite_response(x)
            im=pg.Image.open(pg.BytesIO(pokesprite.content))
            im = im.resize((300,300),pg.Image.LANCZOS)
            final=pg.ImageTk.PhotoImage(im)
            self.sprite.configure(image=final)
            self.sprite.image=final
        except:
            reason='pokename not found'
            for i in self.stat_labels:
                i.configure(text=reason)
            self.poketype.configure(text=reason)
            self.sprite.configure(image=None)
            self.sprite.image=None

root = tk.Tk()
NameToStats(root)
root.mainloop()