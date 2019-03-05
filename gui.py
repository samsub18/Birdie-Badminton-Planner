from PIL import ImageTk, Image
import tkinter as tk

#----------------------Full Screen--------------------------#


class FullScreenApp(object):
    def __init__(self, master, **kwargs):
        self.master = master
        pad = 3
        self._geom = '200x200+0+0'
        master.geometry("{0}x{1}+0+0".format(
            master.winfo_screenwidth()-pad, master.winfo_screenheight()-pad))
        master.bind('<Escape>', self.toggle_geom)

    def toggle_geom(self, event):
        geom = self.master.winfo_geometry()
        print(geom, self._geom)
        self.master.geometry(self._geom)
        self._geom = geom

#-------------------------------------------------------------#


root = tk.Toplevel()  # Starting point of the program


img = ImageTk.PhotoImage(Image.open('Birdie_logo.jpg'))
birdie = tk.Label(root, image=img)
birdie.pack(side="top", ipadx=600, ipady=0)


app = FullScreenApp(root)
root.mainloop()
