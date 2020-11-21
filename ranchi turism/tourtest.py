# importing the required module 
import tkinter as tk
from tkinter import ttk
from PIL import ImageTk , Image
import imageio
import threading
# import the menu
from mnu import min
#marquee class
class Marquee(tk.Canvas):
    def __init__(self, parent, text, margin=2, borderwidth=1, relief='flat', fps=30,bg = 'white'):
        tk.Canvas.__init__(self, parent, borderwidth=borderwidth, relief=relief,bg = bg)
        self.fps = fps
        # start by drawing the text off screen, then asking the canvas
        # how much space we need. Use that to compute the initial size
        # of the canvas. 
        text = self.create_text(0, -1000, text=text, anchor="w", tags=("text",))
        (x0, y0, x1, y1) = self.bbox("text")
        width = (x1 - x0) + (2*margin) + (2*borderwidth)
        height = (y1 - y0) + (2*margin) + (2*borderwidth)
        self.configure(width=width, height=height)
        # start the animation
        self.animate()
    def animate(self):
        (x0, y0, x1, y1) = self.bbox("text")
        if x1 < 0 or y0 < 0:
            # everything is off the screen; reset the X
            # to be just past the right margin
            x0 = self.winfo_width()
            y0 = int(self.winfo_height()/2)
            self.coords("text", x0, y0)
        else:
            self.move("text", -1, 0)
        # do again in a few milliseconds
        self.after_id = self.after(int(1000/self.fps), self.animate)
#video of selected place of ranchi
video_name = "./res/intro1.mp4" #This is your video file path
video = imageio.get_reader(video_name)
def stream(label):

    for image in video.iter_data():
        frame_image = ImageTk.PhotoImage(Image.fromarray(image))
        label.config(image=frame_image,height = 450, width = 590 )
        label.image = frame_image
# This is the menu bar 
class Manu(tk.Frame):
    
    def __init__(self):
        super().__init__()

        self.initUI()


    def initUI(self):
        menubar = tk.Menu(self.master)
        self.master.config(menu=menubar)
        menubar.config(bg = 'lightblue',fg ='black')
        place_to_visit = tk.Menu(menubar, tearoff =0)
        place_to_visit.config(bg = 'lightblue',fg = 'black')
        relegiousmenu = tk.Menu(place_to_visit,tearoff = 0)
        relegiousmenu.config(bg = 'lightblue', fg = 'black')
        relegiousmenu.add_command(label="Pahari Mandir", command = min.pahari)
        relegiousmenu.add_command(label="Jagnath Mandir", command = min.jagnath)
        relegiousmenu.add_command(label="Dewri Mandir", command = min.dewri)
        relegiousmenu.add_command(label="Sun Temple", command = min.sun)
        place_to_visit.add_cascade(label='relegious', menu=relegiousmenu, underline=0)

        parkmenu = tk.Menu(place_to_visit,tearoff = 0)
        parkmenu.config(bg = 'lightblue', fg = 'black')
        parkmenu.add_command(label="Oramanjhi Park", command = min.oramanghi)
        parkmenu.add_command(label="Rock Garden", command = min.rock)
        parkmenu.add_command(label="Oxygen Park", command = min.oxygen)
        place_to_visit.add_cascade(label='Parks', menu=parkmenu, underline=0)

        fallmenu = tk.Menu(place_to_visit,tearoff = 0)
        fallmenu.config(bg = 'lightblue', fg = 'black')
        fallmenu.add_command(label="Dassam Fall", command = min.dassam)
        fallmenu.add_command(label="Hundru Fall", command = min.hundru)
        fallmenu.add_command(label="Jonha Fall", command = min.jonha)
        fallmenu.add_command(label="Panch Gagh Fall", command = min.panch)
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

        form = tk.Menu(menubar, tearoff = 0, background = 'lightblue', foreground = 'black')
        form.add_separator()
        form.add_command(label ="Register now ", command = min.form)
        form.add_separator()
        menubar.add_cascade(label = "Register Now", menu = form)

        about = tk.Menu(menubar, tearoff = 0, background = 'lightblue', foreground = 'black')
        about.add_separator()
        about.add_command(label = "About the software",command = min.abs)
        about.add_command(label = "About the developer", command = min.abd)
        about.add_separator()
        menubar.add_cascade(label = "About", menu = about)
    def onExit(self):
        self.quit()
# Main window is Hear  
root = tk.Tk()
root.geometry("400x400")
root.state('zoomed')
root.configure(bg = "black")
root.title("Ranchi Tourism")
#Frames of the window 
f1 = tk.Frame(root, borderwidth = 3,  bg = "black",relief = "ridge")
f2 = tk.Frame(root, borderwidth = 0, bg ="grey",relief = "ridge")
f3 = tk.Frame(root, borderwidth = 0, bg = "black",relief = "flat")
f4 = tk.Frame(root, borderwidth = 0, bg ="black",relief = "ridge")
f2_1 = tk.Frame(f2, borderwidth = 0, bg ="black",relief = "flat")
f2_2 = tk.Frame(f2, borderwidth = 0, bg ="lightblue",relief = "flat")
f2_3 = tk.Frame(f2, borderwidth = 0, bg ="black",relief = "flat")
f2_4 = tk.Frame(f2, borderwidth = 0, bg ="black",relief = "flat")
f5 = tk.Frame(root, borderwidth = 0, bg = "black",relief = "sunken")
f6 = tk.Frame(root, borderwidth = 0, bg = "black",relief = "sunken")


f1.pack(side = "left", fill ="y" )
f2.pack(side = "bottom", fill ="x")
f3.pack(side = "top", fill = "x")
f4.pack(side = "right", fill ="y")
f2_1.pack(side = "right", fill ="y")
f2_2.pack(side = "top", fill ="x")
f2_3.pack(side = "left", fill ="y")
f2_4.pack(side = "right", fill ="y")
f5.pack(side = "bottom", fill ="x")
f6.pack(side = "top", fill ="x")

#this part is the heading of the windows frame 3
tk.Label(f3,  text = " welcome to ranchi tourism", font = "times 20 bold", bg = "black", fg = "yellow").pack(pady = 10)

# new line for managing frame2
tk.Label(f2, text = "\n \n \n", bg = "black", fg = "red", font= "times 20 bold").pack()

# content of frame 1
tk.Label(f1, text = "Gallery :-                 ",
font = "times 15 bold",bg = "black", fg = "red",relief = "sunken").pack(side = "top", anchor = "nw", fill ="x")
tk.Label(f1,text = "Tagore hill:",
font = "times 12 bold italic underline", bg = "black", fg = "lightblue").pack(side = "top", anchor = "nw")
img = ImageTk.PhotoImage(Image.open("./res/tagore.jpg"))
tk.Label(f1, image = img).pack(expand = "yes",side = "top", anchor = "nw")

tk.Label(f1,text = "Hundru Fall:",
font = "times 12 bold italic underline", bg = "black", fg = "lightblue").pack(anchor = "nw")
img1 = ImageTk.PhotoImage(Image.open("./res/hundru fall.jpg"))
tk.Label(f1, image = img1).pack(expand = "yes",side = "top", anchor = "nw")

tk.Label(f1,text = "patratu Valley:",
font = "times 12 bold italic underline", bg = "black", fg = "lightblue").pack(anchor = "nw")
img2 = ImageTk.PhotoImage(Image.open("./res/patratu-valley.jpg"))
tk.Label(f1, image = img2,bg = "black").pack(expand = "yes",side = "top", anchor = "nw")
#marquee section of the window injected from class marquee frame 3
marquee = Marquee(f3, text="This Application is developed by Awanish Kumar for those who really intrested to explore the new Horizons of Ranchi the heart of Jharkhand", borderwidth=1, relief="sunken")
marquee.pack(side="top", fill="x", pady=0)

#sub heading of frame 4 
tk.Label(f4, text = "Video of some selected place of Ranchi:                   ",
font = "times 18 bold italic",bg = "black", fg = "lime",justify = "left").pack(side = "top")

#design of frame 2

#content of right frame 1 of frame 2
tk.Label(f2_1, text = "contact us:-                                               ",
font = "times 15 bold italic",bg = "black", fg = "red", padx = "20",relief = "sunken").pack(anchor = "nw")
tk.Label(f2_1,text="NAME = Awanish kumar",
font = "times 12 bold italic",bg = "black", fg = "red",justify = "left",padx = "20").pack(side = "top", anchor = "nw")
tk.Label(f2_1,text="E-mail = kawanish387@gmail.com",
font = "times 12 bold italic",bg = "black", fg = "red",justify = "left",padx = "20").pack(side = "top", anchor = "nw")
tk.Label(f2_1,text="contact = 6299717898",
font = "times 12 bold italic",bg = "black", fg = "red",justify = "left", padx = "20").pack(side = "top", anchor = "nw")
#content of left frame 2 of frame 2
marquee = Marquee(f2_2, text="ONGOING OFFERS OF OUR COMPANY WILL BE SHOWN HEAR",
borderwidth=0, relief="flat",bg = "lightblue")
marquee.pack(side="top", fill="x", pady=0)
#content of left frame 3 of frame 2
tk.Label(f2_3, text = "OFFERS :-                            ",
font = "times 15 bold italic",bg = "black", fg = "red", padx = "20").pack(anchor = "nw")
tk.Label(f2_3,text="No offers Available",
font = "times 12 bold italic",bg = "black", fg = "red",justify = "left", padx = "20").pack(side = "top", anchor = "nw")

#content of right frame 4 of frame 2 
tk.Label(f2_4, text = "PACKAGES :-                                              ",
font = "times 15 bold italic",bg = "black", fg = "red", padx = "20").pack(anchor = "nw")
tk.Label(f2_4,text="Complete Ranchi darshan with tour guid: RS 5000 -/ ",
font = "times 12 bold italic",bg = "black", fg = "lightgreen",justify = "left", padx = "20").pack(side = "top", anchor = "nw")
tk.Label(f2_4,text="Complete Ranchi darshan without tour guid: RS 2000 -/ ",
font = "times 12 bold italic",bg = "black", fg = "lightgreen",justify = "left", padx = "20").pack(side = "top", anchor = "nw")
tk.Label(f2_4,text="Three Days Four Night Ranchi Privilege: RS 8000 -/ ",
font = "times 12 bold italic",bg = "black", fg = "lightgreen",justify = "left", padx = "20").pack(side = "top", anchor = "nw")

#video for frame 4
my_label = tk.Label(f4)
my_label.pack()
thread = threading.Thread(target=stream, args=(my_label,))
thread.daemon = 1
thread.start()

#menu bar of the main window
app = Manu()
#Headind for about Ranchi in frame 6
tk.Label(f6,text = '''About Ranchi:-''',
font = "times 18 bold italic", bg = "black", fg = "orange", justify = "left",anchor = "nw").pack(fill = "x",padx = 5)
#content of about ranchi in the remaining area of root 
S = tk.Scrollbar(root)
T = tk.Text(root, height=4, width=60)
S.pack(side=tk.RIGHT, fill=tk.Y)
T.pack(side=tk.LEFT, fill=tk.Y)
S.config(command=T.yview)
T.config(yscrollcommand=S.set)
quote = """Ranchi is the capital of the Indian state of Jharkhand
and 4th Largest city of India by area. 
Ranchi was the centre of the Jharkhand movement,
which called for a separate state for the tribal regions 
of South Bihar, 
northern Orissa, western West Bengal and the eastern area of what is present-day Chhattisgarh.
The Jharkhand state was formed on 15 November 2000 by 
carving out the Bihar divisions of Chota Nagpur and 
Santhal Parganas. 
Ranchi has been selected as one of the hundred
Indian cities to be developed as a smart city under PM
Narendra Modi's flagship Smart Cities Mission.

Geography:

Ranchi lies at 23°22′N 85°20′E near to the 
Tropic of Cancer. 
Its municipal area is 652.02 km2 (251.75 sq mi), 
and its average elevation is 651 m above sea level.
Ranchi is surrounded by lush agriculturally fertile land.
Ranchi is located in the southern part of the Chota Nagpur plateau,
which is the eastern section of the Deccan plateau.
Ranchi has a hilly topography and its dense tropical 
forests a combination that produces
a relatively moderate climate compared to the rest of the state. 
However, due to the uncontrolled deforestation, and development of the city, 
the average temperature has increased.

Climate:

Although Ranchi has a humid subtropical climate 
(Köppen Climate Classification: Cwa), 
its location and the forests surrounding it combine to produce 
the unusually pleasant climate for which it's known. 
Summer temperatures range from 20 °C to 42 degrees, 
winter temperatures from 0 °C to 25 degrees. 
December and January are the coolest months, 
with temperatures dipping to the freezing point in some areas (Kanke). 
The annual rainfall is about 1430 mm (56.34 inches). 
From June to September the rainfall is about 1,100 mm.
"""
T.insert(tk.END, quote)
T.config(state = "disabled",bg = "black", fg = "white")

#instructig to check the menu bar in frame 5
tk.Label(f5, text = '''The Above content is from wikipideya !''',
font = "times 15 bold italic", bg = "black", fg = "red", justify = "left",anchor = "nw").pack(fill = "x", padx = 5)

tk.Label(f5, text = '''Do check the menubars to know more !''',
font = "times 15 bold italic", bg = "black", fg = "pink", justify = "left",anchor = "nw").pack(fill = "x", padx = 5)

root.mainloop()