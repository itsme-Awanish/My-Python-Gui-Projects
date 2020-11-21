import tkinter as tk

class Example(tk.Frame):
    
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):

        self.master.title("Submenu")

        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        menubar.config(bg = 'lightblue',fg ='black')
        place_to_visit = tk.Menu(menubar, tearoff =0)
        place_to_visit.config(bg = 'lightblue',fg = 'black')
        relegiousmenu = tk.Menu(place_to_visit,tearoff = 0)
        relegiousmenu.config(bg = 'lightblue', fg = 'black')
        relegiousmenu.add_command(label="Pahari Mandir")
        relegiousmenu.add_command(label="Jagnath Mandir")
        relegiousmenu.add_command(label="Dewri Mandir")
        relegiousmenu.add_command(label="Sun Temple")
        place_to_visit.add_cascade(label='relegious', menu=relegiousmenu, underline=0)

        parkmenu = tk.Menu(place_to_visit,tearoff = 0)
        parkmenu.config(bg = 'lightblue', fg = 'black')
        parkmenu.add_command(label="Oramanjhi Park")
        parkmenu.add_command(label="Rock Garden")
        parkmenu.add_command(label="Oxygen Park")
        place_to_visit.add_cascade(label='Parks', menu=parkmenu, underline=0)

        fallmenu = tk.Menu(place_to_visit,tearoff = 0)
        fallmenu.config(bg = 'lightblue', fg = 'black')
        fallmenu.add_command(label="Dassam Fall")
        fallmenu.add_command(label="Hundru Fall")
        fallmenu.add_command(label="Jonha Fall")
        fallmenu.add_command(label="Panch Gagh Fall")
        place_to_visit.add_cascade(label='Fall\'s', menu=fallmenu, underline=0)

        damsmenu = tk.Menu(place_to_visit,tearoff = 0)
        damsmenu.config(bg = 'lightblue', fg = 'black')
        damsmenu.add_command(label="Kanke Dam")
        damsmenu.add_command(label="Dhruwa Dam")
        place_to_visit.add_cascade(label='Dam\'s', menu=damsmenu, underline=0)

        museammenu = tk.Menu(place_to_visit,tearoff = 0)
        museammenu.config(bg = 'lightblue', fg = 'black')
        museammenu.add_command(label="State Museam")
        museammenu.add_command(label="Tribal Museam")
        place_to_visit.add_cascade(label='Museam', menu=museammenu, underline=0)

        eyemenu = tk.Menu(place_to_visit,tearoff = 0)
        eyemenu.config(bg = 'lightblue', fg = 'black')
        eyemenu.add_command(label="Patratu valley")
        eyemenu.add_command(label="Tagore Hill")
        place_to_visit.add_cascade(label='Place To See', menu=eyemenu, underline=0)

        place_to_visit.add_separator()

        place_to_visit.add_command(label="Exit", underline=0, command=self.onExit)
        place_to_visit.add_separator()
        menubar.add_cascade(label="Place To Visit", underline=0, menu=place_to_visit)

        hotel = tk.Menu(menubar, tearoff = 0, background = 'lightblue', foreground = 'black')
        hotel.add_separator()
        hotel.add_command(label = "Hotel Accommodation")
        menubar.add_cascade(label = "Hotel's", menu = hotel)
        hotel.add_separator()

        form = tk.Menu(menubar, tearoff = 0, background = 'lightblue', foreground = 'black')
        form.add_separator()
        form.add_command(label ="Register now ", command = min.form)
        form.add_separator()
        menubar.add_cascade(label = "Register Now", menu = form)

        about = tk.Menu(menubar, tearoff = 0, background = 'lightblue', foreground = 'black')
        about.add_separator()
        about.add_command(label = "About the software")
        about.add_command(label = "About the developer")
        about.add_separator()
        menubar.add_cascade(label = "About", menu = about)
    def onExit(self):
        self.quit()


    
root = tk.Tk()
root.geometry("250x150+300+300")
app = Example()
root.mainloop()
