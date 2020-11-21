#the header files will be shown hear
import tkinter as tk
from tkinter import *
from tkinter import ttk
from PIL import ImageTk , Image
import imageio
import threading
import webbrowser
#The functions of the whole menu 
'''
Total number of the menu is nine and sub menus are 15
so the function will be 15
'''

#marquee Class
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
#function for managing the links 
def callback(url):
    webbrowser.open_new(url)
#relegious menu and sub menu
def pahari():
    temp = tk.Toplevel()
    temp.title('Pahari')
    temp.geometry("400x600")
    temp.state('zoomed')
    temp.configure(bg = 'black')
    #Frames for the Relegious window
    fbasehead = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaseimg = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaselink = tk.Frame(fbaseimg, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext1 = tk.Frame(fbasetext, borderwidth = 5,bg = 'black' , relief = "sunken")
    #packing the frames in the correct position
    fbasehead.pack(side = "top",fill = "x")
    fbaseimg.pack(side = "left",fill = "y")
    fbaselink.pack(side = "bottom",fill = "x")
    fbasetext.pack(side = "right",fill = "y")
    fbasetext1.pack(side = "bottom",fill = "x")


    #adding the heading
    tk.Label(fbasehead, text = 'Pahari mandir: -', bg = 'black', fg = 'yellow', font = 'times 20 bold italic').pack(fill = 'x', side = 'left',anchor = 'nw')
    #adding the image to the frame img
    img = ImageTk.PhotoImage(Image.open("./res/pahari.jpg"))
    tk.Label(fbaseimg, image = img).pack(expand = "yes",side = "top", anchor = "nw")
    # adding the Link heading to Frame 
    tk.Label(fbaseimg, text='Follow the link down to \nget the direction of Pahari Mandir: -', 
    fg = 'red', bg = 'black', font = 'times 20 bold italic underline' ).pack(fill = 'x', side = 'top')
    #adding link to label
    link1 = tk.Label(fbaselink, text="Direcion To Pahari Mandir", fg="blue",bg = 'white', cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.google.com/maps/dir/22.7770702,86.1853464/Pahari+Mandir,+Kumhartoli,+Ranchi,+Jharkhand/@23.0761698,85.4459499,10z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x39f4e0e3ac9571fb:0xbfd684943698a996!2m2!1d85.31075!2d23.3754286!3e0?hl=en"))
    #working on the text frame 
    S = tk.Scrollbar(fbasetext)
    T = tk.Text(fbasetext, height=2, width=150)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """A Shiv Temple positioned on a hill west of Ranchi. through the month of Shravana, devotees offer\n on the lingam. the hill give a panaromic view of city Is one of the landmark of Ranchi Town. The \nShiva temple is located on the top of the hill also known as Pahari Mandir. At the bottom of the\n hill is Ranchi Lake. Ranchi lake was excavated by Colonel Onsely in 1842.\n
    \n
    About Pahari Mandir
    \n
    The temple of Lord Shankara (Shiva) is situated in the heart of the city on a hill called Pahari Mandir. It is a bare black land outcropping in the midst of a flat land. The age old Pahari Mandir is located 8 kms from the railway station and 12 kms from the airport. The 2140 feet Ranchi hill houses the temple at its summit. One needs to climb a flight of 468 steps to reach the summit.

    This place is fast developing into a religious tourist site as this is the best place to have a bird’s eye view of the city of Ranchi and also attain some salvation by paying ones obsequies to the Lord. A huge crowd of Shiva devotees gather here between the months of February and October, during Shivaratri and other important days earmarked to pray to the Lord. The Lord also known as Pahari Baba is worshipped in the form of a linga. The hillock also known as Richi Buru is famous for its breathtaking views of the city and some spectacular sunsets and sunrises.



    At the foot of this hill is the beautiful Ranchi Lake. The lake was dug by a Britisher; Colonel Onsely in 1842 is frequented by all visitors for its beauty. The lake is flanked by two temples and a pillared bathing ghat where tourists heading to the Pahari temple take a dip before proceeding to climb the steps of the hillock. The people of Ranchi have a unique way of remembering the heroes who sacrificed their lives during the freedom struggle. It is said many freedom fighters were sent to the gallows atop this hill. When the country won freedom, the residents of Ranchi, decided to pay respect to those martyrs by hoisting the tricolor on the hill. And the tradition continues with people hosting the tricolor during Independence and Republic Day atop the temple as a mark of respect towards those who sacrificed their lives. This is a unique gesture found at a temple, which is rare and special.



    The temple also has the relation to some freedom fighters of Ranchi. The real name of this beautiful embedded old shiv mandir which is about 300 ft. high is 'Richi Buru'. The temple built on top of Ranchi or Fansi hill can be reached by climbing a flight of steps, numbering a few hundreds. From there the devotees can have spectacular views of the city and the Ranchi Lake which is flowing through the bottom of the hill.

    It is a very charming and imposing temple of Lord Shankara which is another name of Lord Shiva. Ranch hill was earlier being known as Phansi Tongri and it was the place where freedom fighters were hanged to death. To remember the importance of this important hill in the freedom movement, tricolor flag is unfurled on the Independence Days and Republic days.

    The surroundings of temple have well maintained picturesque surroundings and to reach the temple at the top of the mountain requires tapping up of more than 300 steps. Most of the devotees visit this place to make their wishes and also make the opportunity to thank Lord Shiva for the blessings. One can have a bird’s view of the whole Ranchi city from the temple premises and the view is really an enchanting eye- pleasing experience. The trees of different species add to the beauty of the hill especially during the rainy season. During Shravan time, the devotees offer Jal (Dhara) to Lord Shiva and the Shravan season is a major draw of visitors.

    """
    T.insert(tk.END, quote)
    T.config(state = "disabled",bg = "black", fg = "white")

    #instructig to check the menu bar in frame 5
    tk.Label(fbasetext1, text = '''The Above content is from wikipideya !''',
    font = "times 15 bold italic", bg = "black", fg = "red", justify = "left",anchor = "nw").pack(fill = "x", padx = 5, side = 'top')
    temp.mainloop()
#jagnath menu
def jagnath():
    temp = tk.Toplevel()
    temp.title('Pahari')
    temp.geometry("400x600")
    temp.state('zoomed')
    temp.configure(bg = 'black')
    #Frames for the Relegious window
    fbasehead = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaseimg = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaselink = tk.Frame(fbaseimg, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext1 = tk.Frame(fbasetext, borderwidth = 5,bg = 'black' , relief = "sunken")
    #packing the frames in the correct position
    fbasehead.pack(side = "top",fill = "x")
    fbaseimg.pack(side = "left",fill = "y")
    fbaselink.pack(side = "bottom",fill = "x")
    fbasetext.pack(side = "right",fill = "y")
    fbasetext1.pack(side = "bottom",fill = "x")


    #adding the heading
    tk.Label(fbasehead, text = 'jagnath: -', bg = 'black', fg = 'yellow', font = 'times 20 bold italic').pack(fill = 'x', side = 'left',anchor = 'nw')
    #adding the image to the frame img
    img = ImageTk.PhotoImage(Image.open("./res/jagnath.jpg"))
    tk.Label(fbaseimg, image = img).pack(expand = "yes",side = "top", anchor = "nw")
    # adding the Link heading to Frame 
    tk.Label(fbaseimg, text='Follow the link down to \nget the direction of Pahari Mandir: -', 
    fg = 'red', bg = 'black', font = 'times 20 bold italic underline' ).pack(fill = 'x', side = 'top')
    #adding link to label
    link1 = tk.Label(fbaselink, text="Direcion To Jagnath Mandir", fg="blue",bg = 'white', cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.google.com/maps/dir/22.7770702,86.1853464/Jagannath+Mandir,+Jagannathpur+Chowk+Khataal,+Sector+1+Jagannathpur,+hec,+Khataal,+Dhurwa,+Khataal,+Jagannathpur,+Ranchi,+Jharkhand+834004/@23.0472334,85.1728547,9z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x39f4e0035ace6e73:0x41f4e59a6d674446!2m2!1d85.2816259!2d23.3168511!3e0?hl=en"))
    #working on the text frame 
    S = tk.Scrollbar(fbasetext)
    T = tk.Text(fbasetext, height=2, width=150)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """Jagannath Temple in Ranchi, Jharkhand, India, was built by king of Barkagarh Jagannathpur Thakur Ani Nath Shahdeo, in 1691. Completed on December 25, 1691, it is located about 10 km from the main town. The temple is on top of a small hillock.


    An early nineteenth century photograph of the Jagannath temple of Ranchi
    Similar to the famous Jagannath Temple in Puri, Odisha, this temple is built in the same architectural style, although smaller. And similar to the Rath Yatra in Puri, an annual fair cum rath yatra is held at this temple in the month of Aashaadha, attracting thousands of tribal and non-tribal devotees[3] not only from Ranchi but also from neighbouring villages and towns and is celebrated with much pomp and vigor.

    The temple has been built on a hill top. To reach the top visitors can climb the stairs or take the vehicle route. There are many steps and the climber needs to rest intermittently before resuming. People also take the vehicle route leading directly to the top . To facilitate the arduous climb to the top the management of the temple have made provisions for fresh water and the shade of a huge tree that many tourists generally make use of once they reach the top. The view of the city from the top is breathtaking.

    The temple collapsed on 6 August 1990. With the active participation of the then State Government of Bihar, and some devoted patrons the reconstruction of the temple started on 8 February 1992 and has now been fully restored. The temple has regained back its former glory. And devotees and ardent worshippers make a beeline to the temple every year.


    """
    T.insert(tk.END, quote)
    T.config(state = "disabled",bg = "black", fg = "white")

    #instructig to check the menu bar in frame 5
    tk.Label(fbasetext1, text = '''The Above content is from wikipideya !''',
    font = "times 15 bold italic", bg = "black", fg = "red", justify = "left",anchor = "nw").pack(fill = "x", padx = 5, side = 'top')
    temp.mainloop()
#dewri menu
def dewri():
    temp = tk.Toplevel()
    temp.title('Dewri Mandir')
    temp.geometry("400x600")
    temp.state('zoomed')
    temp.configure(bg = 'black')
    #Frames for the Relegious window
    fbasehead = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaseimg = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaselink = tk.Frame(fbaseimg, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext1 = tk.Frame(fbasetext, borderwidth = 5,bg = 'black' , relief = "sunken")
    #packing the frames in the correct position
    fbasehead.pack(side = "top",fill = "x")
    fbaseimg.pack(side = "left",fill = "y")
    fbaselink.pack(side = "bottom",fill = "x")
    fbasetext.pack(side = "right",fill = "y")
    fbasetext1.pack(side = "bottom",fill = "x")


    #adding the heading
    tk.Label(fbasehead, text = 'Dewri Mandir: -', bg = 'black', fg = 'yellow', font = 'times 20 bold italic').pack(fill = 'x', side = 'left',anchor = 'nw')
    #adding the image to the frame img
    img = ImageTk.PhotoImage(Image.open("./res/dewri-mandir.jpg"))
    tk.Label(fbaseimg, image = img).pack(expand = "yes",side = "top", anchor = "nw")
    # adding the Link heading to Frame 
    tk.Label(fbaseimg, text='Follow the link down to \nget the direction of Pahari Mandir: -', 
    fg = 'red', bg = 'black', font = 'times 20 bold italic underline' ).pack(fill = 'x', side = 'top')
    #adding link to label
    link1 = tk.Label(fbaselink, text="Direcion To Dewri Mandir", fg="blue",bg = 'white', cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.google.com/maps/dir/22.7770702,86.1853464/Deori+Mandir+Ranchi,+Ranchi,+Jharkhand/@22.9118173,85.794648,11z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x39f5a6a9b0e7dfc5:0xc3e41bc84f982427!2m2!1d85.682888!2d23.0461347!3e0?hl=en"))
    #working on the text frame 
    S = tk.Scrollbar(fbasetext)
    T = tk.Text(fbasetext, height=2, width=150)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """Dewri Mandir is located in Tamar 60 km toward south from the capital of Indian states Jharkhand i.e. Ranchi. It is on the Tata-Ranchi Highway (NH33). It is a very old temple of Goddess Durga. The main attraction is that the 700 year old idol of the Goddess Durga has 16 Hands (Normally Goddess Durga has 8 Hands). The temple is very old and is currently under renovation. The temple is constructed via the placing of large stones on top of each other without any cementing material.

    At the temple devotees tie yellow and red sacred threads on bamboo for the fulfilment of their wishes. Upon the fulfillment of their wishes, they again come to the temple and untie the thread. Dedicated to Solha Bhuji Goddess, an avatar of Goddess Durga, Dewri Mandir temple is located a little outside the main city of Ranchi. Spread over nearly two acres, this old temple in Ranchi also houses an idol of Lord Shiva here. Legend has it that whoever has tried to alter the structure of the temple has had to face the wrath of the gods and suffer consequences. Dewri Temple is also believed to be the only temple where six tribal priests, known as Pahans, perform rituals and offer prayers alongside the Brahmin priests. Who are mainly known as Panda's. Located about 60 km from Ranchi, this temple is on the right side of the Ranchi-Tata road, toward the town of Tamar.
    """
    T.insert(tk.END, quote)
    T.config(state = "disabled",bg = "black", fg = "white")

    #instructig to check the menu bar in frame 5
    tk.Label(fbasetext1, text = '''The Above content is from wikipideya !''',
    font = "times 15 bold italic", bg = "black", fg = "red", justify = "left",anchor = "nw").pack(fill = "x", padx = 5, side = 'top')
    temp.mainloop()
#sun menu
def sun():
    temp = tk.Toplevel()
    temp.title('Sun Temple')
    temp.geometry("400x600")
    temp.state('zoomed')
    temp.configure(bg = 'black')
    #Frames for the Relegious window
    fbasehead = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaseimg = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaselink = tk.Frame(fbaseimg, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext1 = tk.Frame(fbasetext, borderwidth = 5,bg = 'black' , relief = "sunken")
    #packing the frames in the correct position
    fbasehead.pack(side = "top",fill = "x")
    fbaseimg.pack(side = "left",fill = "y")
    fbaselink.pack(side = "bottom",fill = "x")
    fbasetext.pack(side = "right",fill = "y")
    fbasetext1.pack(side = "bottom",fill = "x")


    #adding the heading
    tk.Label(fbasehead, text = 'Sun Temple: -', bg = 'black', fg = 'yellow', font = 'times 20 bold italic').pack(fill = 'x', side = 'left',anchor = 'nw')
    #adding the image to the frame img
    img = ImageTk.PhotoImage(Image.open("./res/sun temple.jpg"))
    tk.Label(fbaseimg, image = img).pack(expand = "yes",side = "top", anchor = "nw")
    # adding the Link heading to Frame 
    tk.Label(fbaseimg, text='Follow the link down to \nget the direction of Pahari Mandir: -', 
    fg = 'red', bg = 'black', font = 'times 20 bold italic underline' ).pack(fill = 'x', side = 'top')
    #adding link to label
    link1 = tk.Label(fbaselink, text="Direcion To Sun temple", fg="blue",bg = 'white', cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.google.com/maps/dir/22.7770702,86.1853464/Sun+Temple,+Ranchi,+Jharkhand/@23.0789464,85.44595,10z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x39f4e33a27536e21:0x79f58d31a883b6ba!2m2!1d85.4260052!2d23.3811033!3e0?hl=en"))
    #working on the text frame 
    S = tk.Scrollbar(fbasetext)
    T = tk.Text(fbasetext, height=2, width=150)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """The Surya Temple or Surya Mandir (Hindi: सूर्य मंदिर, रांची), located near Bundu, is a Hindu temple complex dedicated to the solar deity, Surya.

    It is situated on top of a hill, on the NH-33 (Ranchi-Tata Road), approximately 40 km (25 mi) from the capital city of Jharkhand, Ranchi. The temple is constructed in the form of huge chariot with elegantly designed eighteen wheels and seven naturalistic horses. The temple also houses several other deities including Shiva, Parvati and Ganesha.

    The temple was built by Sanskriti Vihar, a charitable trust, headed by Shri Sita Ram Maroo, the Managing Director of Ranchi Express Group. The foundation stone was laid by Swami Shri Vasudevanand Saraswati on 24 October 1991 and the Prana Pratishtha was undertaken by Swami Shri Vamdev Ji Maharaj on 10 July 1994.

    A Dharmashala for pilgrims has been constructed. There is also a pond where devotees can bathe during Chhath Puja for worshiping the Sun God.

    """
    T.insert(tk.END, quote)
    T.config(state = "disabled",bg = "black", fg = "white")

    #instructig to check the menu bar in frame 5
    tk.Label(fbasetext1, text = '''The Above content is from wikipideya !''',
    font = "times 15 bold italic", bg = "black", fg = "red", justify = "left",anchor = "nw").pack(fill = "x", padx = 5, side = 'top')
    temp.mainloop()
# registtration menu
def form():
    ''' This function is for the Registration Menu'''
    root = Toplevel()
    root.geometry("644x344")
    root.title('Registration form')
    #Heading
    Label(root, text="Give us opportunity to serve you:-\nFill this form so that we can reach you ",
    font="comicsansms 13 bold underline", pady=15).grid(row=0, column=2)

    #Text for our form
    name = Label(root, text="Name")
    phone = Label(root, text="Phone")
    gender = Label(root, text="Gender")
    emergency = Label(root, text="Alternate Contact")

    #Pack text for our form
    name.grid(row=1, column=2)
    phone.grid(row=2, column=2)
    gender.grid(row=3, column=2)
    emergency.grid(row=4, column=2)

    # Tkinter variable for storing entries
    namevalue = StringVar()
    phonevalue = StringVar()
    gendervalue = StringVar()
    emergencyvalue = StringVar()
    shouldicallyou = IntVar()


    #Entries for our form
    nameentry = Entry(root, textvariable=namevalue)
    phoneentry = Entry(root, textvariable=phonevalue)
    genderentry = Entry(root, textvariable=gendervalue)
    emergencyentry = Entry(root, textvariable=emergencyvalue)

    # Packing the Entries
    nameentry.grid(row=1, column=3)
    phoneentry.grid(row=2, column=3)
    genderentry.grid(row=3, column=3)
    emergencyentry.grid(row=4, column=3)

    #Checkbox & Packing it
    shouldicallyou = Checkbutton(root,text="Should we call You?", variable = shouldicallyou)
    shouldicallyou.grid(row=6, column=3)

    #Button & packing it and assigning it a command
    Button(root,text="Submit to Coustomer records").grid(row=7, column=3)
    root.mainloop()
#park menu and sub menu
#sub menu of parks 
#oramanghi menu
def oramanghi():
    temp = tk.Toplevel()
    temp.title('Oramanghi Park')
    temp.geometry("400x600")
    temp.state('zoomed')
    temp.configure(bg = 'black')
    #Frames for the Relegious window
    fbasehead = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaseimg = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaselink = tk.Frame(fbaseimg, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext1 = tk.Frame(fbasetext, borderwidth = 5,bg = 'black' , relief = "sunken")
    #packing the frames in the correct position
    fbasehead.pack(side = "top",fill = "x")
    fbaseimg.pack(side = "left",fill = "y")
    fbaselink.pack(side = "bottom",fill = "x")
    fbasetext.pack(side = "right",fill = "y")
    fbasetext1.pack(side = "bottom",fill = "x")


    #adding the heading
    tk.Label(fbasehead, text = 'Oramanghi: -', bg = 'black', fg = 'yellow', font = 'times 20 bold italic').pack(fill = 'x', side = 'left',anchor = 'nw')
    #adding the image to the frame img
    img = ImageTk.PhotoImage(Image.open("./res/sun temple.jpg"))
    tk.Label(fbaseimg, image = img).pack(expand = "yes",side = "top", anchor = "nw")
    # adding the Link heading to Frame 
    tk.Label(fbaseimg, text='Follow the link down to \nget the direction of Pahari Mandir: -', 
    fg = 'red', bg = 'black', font = 'times 20 bold italic underline' ).pack(fill = 'x', side = 'top')
    #adding link to label
    link1 = tk.Label(fbaselink, text="Direcion To Sun temple", fg="blue",bg = 'white', cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.google.com/maps/dir/22.7770702,86.1853464/Sun+Temple,+Ranchi,+Jharkhand/@23.0789464,85.44595,10z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x39f4e33a27536e21:0x79f58d31a883b6ba!2m2!1d85.4260052!2d23.3811033!3e0?hl=en"))
    #working on the text frame 
    S = tk.Scrollbar(fbasetext)
    T = tk.Text(fbasetext, height=2, width=150)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """The Surya Temple or Surya Mandir (Hindi: सूर्य मंदिर, रांची), located near Bundu, is a Hindu temple complex dedicated to the solar deity, Surya.

    It is situated on top of a hill, on the NH-33 (Ranchi-Tata Road), approximately 40 km (25 mi) from the capital city of Jharkhand, Ranchi. The temple is constructed in the form of huge chariot with elegantly designed eighteen wheels and seven naturalistic horses. The temple also houses several other deities including Shiva, Parvati and Ganesha.

    The temple was built by Sanskriti Vihar, a charitable trust, headed by Shri Sita Ram Maroo, the Managing Director of Ranchi Express Group. The foundation stone was laid by Swami Shri Vasudevanand Saraswati on 24 October 1991 and the Prana Pratishtha was undertaken by Swami Shri Vamdev Ji Maharaj on 10 July 1994.

    A Dharmashala for pilgrims has been constructed. There is also a pond where devotees can bathe during Chhath Puja for worshiping the Sun God.

    """
    T.insert(tk.END, quote)
    T.config(state = "disabled",bg = "black", fg = "white")

    #instructig to check the menu bar in frame 5
    tk.Label(fbasetext1, text = '''The Above content is from wikipideya !''',
    font = "times 15 bold italic", bg = "black", fg = "red", justify = "left",anchor = "nw").pack(fill = "x", padx = 5, side = 'top')
    temp.mainloop()
#rock garden
def rock():
    temp = tk.Toplevel()
    temp.title('Rock Garden')
    temp.geometry("400x600")
    temp.state('zoomed')
    temp.configure(bg = 'black')
    #Frames for the Relegious window
    fbasehead = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaseimg = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaselink = tk.Frame(fbaseimg, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext1 = tk.Frame(fbasetext, borderwidth = 5,bg = 'black' , relief = "sunken")
    #packing the frames in the correct position
    fbasehead.pack(side = "top",fill = "x")
    fbaseimg.pack(side = "left",fill = "y")
    fbaselink.pack(side = "bottom",fill = "x")
    fbasetext.pack(side = "right",fill = "y")
    fbasetext1.pack(side = "bottom",fill = "x")


    #adding the heading
    tk.Label(fbasehead, text = 'Rock Garden: -', bg = 'black', fg = 'yellow', font = 'times 20 bold italic').pack(fill = 'x', side = 'left',anchor = 'nw')
    #adding the image to the frame img
    img = ImageTk.PhotoImage(Image.open("./res/sun temple.jpg"))
    tk.Label(fbaseimg, image = img).pack(expand = "yes",side = "top", anchor = "nw")
    # adding the Link heading to Frame 
    tk.Label(fbaseimg, text='Follow the link down to \nget the direction of Pahari Mandir: -', 
    fg = 'red', bg = 'black', font = 'times 20 bold italic underline' ).pack(fill = 'x', side = 'top')
    #adding link to label
    link1 = tk.Label(fbaselink, text="Direcion To Sun temple", fg="blue",bg = 'white', cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.google.com/maps/dir/22.7770702,86.1853464/Sun+Temple,+Ranchi,+Jharkhand/@23.0789464,85.44595,10z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x39f4e33a27536e21:0x79f58d31a883b6ba!2m2!1d85.4260052!2d23.3811033!3e0?hl=en"))
    #working on the text frame 
    S = tk.Scrollbar(fbasetext)
    T = tk.Text(fbasetext, height=2, width=150)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """The Surya Temple or Surya Mandir (Hindi: सूर्य मंदिर, रांची), located near Bundu, is a Hindu temple complex dedicated to the solar deity, Surya.

    It is situated on top of a hill, on the NH-33 (Ranchi-Tata Road), approximately 40 km (25 mi) from the capital city of Jharkhand, Ranchi. The temple is constructed in the form of huge chariot with elegantly designed eighteen wheels and seven naturalistic horses. The temple also houses several other deities including Shiva, Parvati and Ganesha.

    The temple was built by Sanskriti Vihar, a charitable trust, headed by Shri Sita Ram Maroo, the Managing Director of Ranchi Express Group. The foundation stone was laid by Swami Shri Vasudevanand Saraswati on 24 October 1991 and the Prana Pratishtha was undertaken by Swami Shri Vamdev Ji Maharaj on 10 July 1994.

    A Dharmashala for pilgrims has been constructed. There is also a pond where devotees can bathe during Chhath Puja for worshiping the Sun God.

    """
    T.insert(tk.END, quote)
    T.config(state = "disabled",bg = "black", fg = "white")

    #instructig to check the menu bar in frame 5
    tk.Label(fbasetext1, text = '''The Above content is from wikipideya !''',
    font = "times 15 bold italic", bg = "black", fg = "red", justify = "left",anchor = "nw").pack(fill = "x", padx = 5, side = 'top')
    temp.mainloop()
#oxygen menu
def oxygen():
    temp = tk.Toplevel()
    temp.title('Oxygen Park')
    temp.geometry("400x600")
    temp.state('zoomed')
    temp.configure(bg = 'black')
    #Frames for the Relegious window
    fbasehead = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaseimg = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaselink = tk.Frame(fbaseimg, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext1 = tk.Frame(fbasetext, borderwidth = 5,bg = 'black' , relief = "sunken")
    #packing the frames in the correct position
    fbasehead.pack(side = "top",fill = "x")
    fbaseimg.pack(side = "left",fill = "y")
    fbaselink.pack(side = "bottom",fill = "x")
    fbasetext.pack(side = "right",fill = "y")
    fbasetext1.pack(side = "bottom",fill = "x")


    #adding the heading
    tk.Label(fbasehead, text = 'Oxygen Park: -', bg = 'black', fg = 'yellow', font = 'times 20 bold italic').pack(fill = 'x', side = 'left',anchor = 'nw')
    #adding the image to the frame img
    img = ImageTk.PhotoImage(Image.open("./res/sun temple.jpg"))
    tk.Label(fbaseimg, image = img).pack(expand = "yes",side = "top", anchor = "nw")
    # adding the Link heading to Frame 
    tk.Label(fbaseimg, text='Follow the link down to \nget the direction of Pahari Mandir: -', 
    fg = 'red', bg = 'black', font = 'times 20 bold italic underline' ).pack(fill = 'x', side = 'top')
    #adding link to label
    link1 = tk.Label(fbaselink, text="Direcion To Sun temple", fg="blue",bg = 'white', cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.google.com/maps/dir/22.7770702,86.1853464/Sun+Temple,+Ranchi,+Jharkhand/@23.0789464,85.44595,10z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x39f4e33a27536e21:0x79f58d31a883b6ba!2m2!1d85.4260052!2d23.3811033!3e0?hl=en"))
    #working on the text frame 
    S = tk.Scrollbar(fbasetext)
    T = tk.Text(fbasetext, height=2, width=150)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """The Surya Temple or Surya Mandir (Hindi: सूर्य मंदिर, रांची), located near Bundu, is a Hindu temple complex dedicated to the solar deity, Surya.

    It is situated on top of a hill, on the NH-33 (Ranchi-Tata Road), approximately 40 km (25 mi) from the capital city of Jharkhand, Ranchi. The temple is constructed in the form of huge chariot with elegantly designed eighteen wheels and seven naturalistic horses. The temple also houses several other deities including Shiva, Parvati and Ganesha.

    The temple was built by Sanskriti Vihar, a charitable trust, headed by Shri Sita Ram Maroo, the Managing Director of Ranchi Express Group. The foundation stone was laid by Swami Shri Vasudevanand Saraswati on 24 October 1991 and the Prana Pratishtha was undertaken by Swami Shri Vamdev Ji Maharaj on 10 July 1994.

    A Dharmashala for pilgrims has been constructed. There is also a pond where devotees can bathe during Chhath Puja for worshiping the Sun God.

    """
    T.insert(tk.END, quote)
    T.config(state = "disabled",bg = "black", fg = "white")

    #instructig to check the menu bar in frame 5
    tk.Label(fbasetext1, text = '''The Above content is from wikipideya !''',
    font = "times 15 bold italic", bg = "black", fg = "red", justify = "left",anchor = "nw").pack(fill = "x", padx = 5, side = 'top')
    temp.mainloop()
# falls menu and sub menu 
#dassam fall
def dassam():
    temp = tk.Toplevel()
    temp.title('Dassam Fall')
    temp.geometry("400x600")
    temp.state('zoomed')
    temp.configure(bg = 'black')
    #Frames for the Relegious window
    fbasehead = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaseimg = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaselink = tk.Frame(fbaseimg, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext1 = tk.Frame(fbasetext, borderwidth = 5,bg = 'black' , relief = "sunken")
    #packing the frames in the correct position
    fbasehead.pack(side = "top",fill = "x")
    fbaseimg.pack(side = "left",fill = "y")
    fbaselink.pack(side = "bottom",fill = "x")
    fbasetext.pack(side = "right",fill = "y")
    fbasetext1.pack(side = "bottom",fill = "x")


    #adding the heading
    tk.Label(fbasehead, text = 'Dassam Fall: -', bg = 'black', fg = 'yellow', font = 'times 20 bold italic').pack(fill = 'x', side = 'left',anchor = 'nw')
    #adding the image to the frame img
    img = ImageTk.PhotoImage(Image.open("./res/sun temple.jpg"))
    tk.Label(fbaseimg, image = img).pack(expand = "yes",side = "top", anchor = "nw")
    # adding the Link heading to Frame 
    tk.Label(fbaseimg, text='Follow the link down to \nget the direction of Pahari Mandir: -', 
    fg = 'red', bg = 'black', font = 'times 20 bold italic underline' ).pack(fill = 'x', side = 'top')
    #adding link to label
    link1 = tk.Label(fbaselink, text="Direcion To Sun temple", fg="blue",bg = 'white', cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.google.com/maps/dir/22.7770702,86.1853464/Sun+Temple,+Ranchi,+Jharkhand/@23.0789464,85.44595,10z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x39f4e33a27536e21:0x79f58d31a883b6ba!2m2!1d85.4260052!2d23.3811033!3e0?hl=en"))
    #working on the text frame 
    S = tk.Scrollbar(fbasetext)
    T = tk.Text(fbasetext, height=2, width=150)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """The Surya Temple or Surya Mandir (Hindi: सूर्य मंदिर, रांची), located near Bundu, is a Hindu temple complex dedicated to the solar deity, Surya.

    It is situated on top of a hill, on the NH-33 (Ranchi-Tata Road), approximately 40 km (25 mi) from the capital city of Jharkhand, Ranchi. The temple is constructed in the form of huge chariot with elegantly designed eighteen wheels and seven naturalistic horses. The temple also houses several other deities including Shiva, Parvati and Ganesha.

    The temple was built by Sanskriti Vihar, a charitable trust, headed by Shri Sita Ram Maroo, the Managing Director of Ranchi Express Group. The foundation stone was laid by Swami Shri Vasudevanand Saraswati on 24 October 1991 and the Prana Pratishtha was undertaken by Swami Shri Vamdev Ji Maharaj on 10 July 1994.

    A Dharmashala for pilgrims has been constructed. There is also a pond where devotees can bathe during Chhath Puja for worshiping the Sun God.

    """
    T.insert(tk.END, quote)
    T.config(state = "disabled",bg = "black", fg = "white")

    #instructig to check the menu bar in frame 5
    tk.Label(fbasetext1, text = '''The Above content is from wikipideya !''',
    font = "times 15 bold italic", bg = "black", fg = "red", justify = "left",anchor = "nw").pack(fill = "x", padx = 5, side = 'top')
    temp.mainloop()
#hundru fall
def hundru():
    temp = tk.Toplevel()
    temp.title('Hundru Fall')
    temp.geometry("400x600")
    temp.state('zoomed')
    temp.configure(bg = 'black')
    #Frames for the Relegious window
    fbasehead = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaseimg = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaselink = tk.Frame(fbaseimg, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext1 = tk.Frame(fbasetext, borderwidth = 5,bg = 'black' , relief = "sunken")
    #packing the frames in the correct position
    fbasehead.pack(side = "top",fill = "x")
    fbaseimg.pack(side = "left",fill = "y")
    fbaselink.pack(side = "bottom",fill = "x")
    fbasetext.pack(side = "right",fill = "y")
    fbasetext1.pack(side = "bottom",fill = "x")


    #adding the heading
    tk.Label(fbasehead, text = 'Hundru Fall: -', bg = 'black', fg = 'yellow', font = 'times 20 bold italic').pack(fill = 'x', side = 'left',anchor = 'nw')
    #adding the image to the frame img
    img = ImageTk.PhotoImage(Image.open("./res/sun temple.jpg"))
    tk.Label(fbaseimg, image = img).pack(expand = "yes",side = "top", anchor = "nw")
    # adding the Link heading to Frame 
    tk.Label(fbaseimg, text='Follow the link down to \nget the direction of Pahari Mandir: -', 
    fg = 'red', bg = 'black', font = 'times 20 bold italic underline' ).pack(fill = 'x', side = 'top')
    #adding link to label
    link1 = tk.Label(fbaselink, text="Direcion To Sun temple", fg="blue",bg = 'white', cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.google.com/maps/dir/22.7770702,86.1853464/Sun+Temple,+Ranchi,+Jharkhand/@23.0789464,85.44595,10z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x39f4e33a27536e21:0x79f58d31a883b6ba!2m2!1d85.4260052!2d23.3811033!3e0?hl=en"))
    #working on the text frame 
    S = tk.Scrollbar(fbasetext)
    T = tk.Text(fbasetext, height=2, width=150)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """The Surya Temple or Surya Mandir (Hindi: सूर्य मंदिर, रांची), located near Bundu, is a Hindu temple complex dedicated to the solar deity, Surya.

    It is situated on top of a hill, on the NH-33 (Ranchi-Tata Road), approximately 40 km (25 mi) from the capital city of Jharkhand, Ranchi. The temple is constructed in the form of huge chariot with elegantly designed eighteen wheels and seven naturalistic horses. The temple also houses several other deities including Shiva, Parvati and Ganesha.

    The temple was built by Sanskriti Vihar, a charitable trust, headed by Shri Sita Ram Maroo, the Managing Director of Ranchi Express Group. The foundation stone was laid by Swami Shri Vasudevanand Saraswati on 24 October 1991 and the Prana Pratishtha was undertaken by Swami Shri Vamdev Ji Maharaj on 10 July 1994.

    A Dharmashala for pilgrims has been constructed. There is also a pond where devotees can bathe during Chhath Puja for worshiping the Sun God.

    """
    T.insert(tk.END, quote)
    T.config(state = "disabled",bg = "black", fg = "white")

    #instructig to check the menu bar in frame 5
    tk.Label(fbasetext1, text = '''The Above content is from wikipideya !''',
    font = "times 15 bold italic", bg = "black", fg = "red", justify = "left",anchor = "nw").pack(fill = "x", padx = 5, side = 'top')
    temp.mainloop()
#junha fall
def jonha():
    temp = tk.Toplevel()
    temp.title('Jonha Fall')
    temp.geometry("400x600")
    temp.state('zoomed')
    temp.configure(bg = 'black')
    #Frames for the Relegious window
    fbasehead = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaseimg = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaselink = tk.Frame(fbaseimg, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext1 = tk.Frame(fbasetext, borderwidth = 5,bg = 'black' , relief = "sunken")
    #packing the frames in the correct position
    fbasehead.pack(side = "top",fill = "x")
    fbaseimg.pack(side = "left",fill = "y")
    fbaselink.pack(side = "bottom",fill = "x")
    fbasetext.pack(side = "right",fill = "y")
    fbasetext1.pack(side = "bottom",fill = "x")


    #adding the heading
    tk.Label(fbasehead, text = 'Jonha fall: -', bg = 'black', fg = 'yellow', font = 'times 20 bold italic').pack(fill = 'x', side = 'left',anchor = 'nw')
    #adding the image to the frame img
    img = ImageTk.PhotoImage(Image.open("./res/sun temple.jpg"))
    tk.Label(fbaseimg, image = img).pack(expand = "yes",side = "top", anchor = "nw")
    # adding the Link heading to Frame 
    tk.Label(fbaseimg, text='Follow the link down to \nget the direction of Pahari Mandir: -', 
    fg = 'red', bg = 'black', font = 'times 20 bold italic underline' ).pack(fill = 'x', side = 'top')
    #adding link to label
    link1 = tk.Label(fbaselink, text="Direcion To Sun temple", fg="blue",bg = 'white', cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.google.com/maps/dir/22.7770702,86.1853464/Sun+Temple,+Ranchi,+Jharkhand/@23.0789464,85.44595,10z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x39f4e33a27536e21:0x79f58d31a883b6ba!2m2!1d85.4260052!2d23.3811033!3e0?hl=en"))
    #working on the text frame 
    S = tk.Scrollbar(fbasetext)
    T = tk.Text(fbasetext, height=2, width=150)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """The Surya Temple or Surya Mandir (Hindi: सूर्य मंदिर, रांची), located near Bundu, is a Hindu temple complex dedicated to the solar deity, Surya.

    It is situated on top of a hill, on the NH-33 (Ranchi-Tata Road), approximately 40 km (25 mi) from the capital city of Jharkhand, Ranchi. The temple is constructed in the form of huge chariot with elegantly designed eighteen wheels and seven naturalistic horses. The temple also houses several other deities including Shiva, Parvati and Ganesha.

    The temple was built by Sanskriti Vihar, a charitable trust, headed by Shri Sita Ram Maroo, the Managing Director of Ranchi Express Group. The foundation stone was laid by Swami Shri Vasudevanand Saraswati on 24 October 1991 and the Prana Pratishtha was undertaken by Swami Shri Vamdev Ji Maharaj on 10 July 1994.

    A Dharmashala for pilgrims has been constructed. There is also a pond where devotees can bathe during Chhath Puja for worshiping the Sun God.

    """
    T.insert(tk.END, quote)
    T.config(state = "disabled",bg = "black", fg = "white")

    #instructig to check the menu bar in frame 5
    tk.Label(fbasetext1, text = '''The Above content is from wikipideya !''',
    font = "times 15 bold italic", bg = "black", fg = "red", justify = "left",anchor = "nw").pack(fill = "x", padx = 5, side = 'top')
    temp.mainloop()
#panch gagh
def panch():
    temp = tk.Toplevel()
    temp.title('Panch Gagh Fall')
    temp.geometry("400x600")
    temp.state('zoomed')
    temp.configure(bg = 'black')
    #Frames for the Relegious window
    fbasehead = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaseimg = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbaselink = tk.Frame(fbaseimg, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext = tk.Frame(temp, borderwidth = 5,bg = 'black' , relief = "sunken")
    fbasetext1 = tk.Frame(fbasetext, borderwidth = 5,bg = 'black' , relief = "sunken")
    #packing the frames in the correct position
    fbasehead.pack(side = "top",fill = "x")
    fbaseimg.pack(side = "left",fill = "y")
    fbaselink.pack(side = "bottom",fill = "x")
    fbasetext.pack(side = "right",fill = "y")
    fbasetext1.pack(side = "bottom",fill = "x")


    #adding the heading
    tk.Label(fbasehead, text = 'Panch Gagh Fall: -', bg = 'black', fg = 'yellow', font = 'times 20 bold italic').pack(fill = 'x', side = 'left',anchor = 'nw')
    #adding the image to the frame img
    img = ImageTk.PhotoImage(Image.open("./res/sun temple.jpg"))
    tk.Label(fbaseimg, image = img).pack(expand = "yes",side = "top", anchor = "nw")
    # adding the Link heading to Frame 
    tk.Label(fbaseimg, text='Follow the link down to \nget the direction of Pahari Mandir: -', 
    fg = 'red', bg = 'black', font = 'times 20 bold italic underline' ).pack(fill = 'x', side = 'top')
    #adding link to label
    link1 = tk.Label(fbaselink, text="Direcion To Sun temple", fg="blue",bg = 'white', cursor="hand2")
    link1.pack()
    link1.bind("<Button-1>", lambda e: callback("https://www.google.com/maps/dir/22.7770702,86.1853464/Sun+Temple,+Ranchi,+Jharkhand/@23.0789464,85.44595,10z/data=!3m1!4b1!4m10!4m9!1m1!4e1!1m5!1m1!1s0x39f4e33a27536e21:0x79f58d31a883b6ba!2m2!1d85.4260052!2d23.3811033!3e0?hl=en"))
    #working on the text frame 
    S = tk.Scrollbar(fbasetext)
    T = tk.Text(fbasetext, height=2, width=150)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """The Surya Temple or Surya Mandir (Hindi: सूर्य मंदिर, रांची), located near Bundu, is a Hindu temple complex dedicated to the solar deity, Surya.

    It is situated on top of a hill, on the NH-33 (Ranchi-Tata Road), approximately 40 km (25 mi) from the capital city of Jharkhand, Ranchi. The temple is constructed in the form of huge chariot with elegantly designed eighteen wheels and seven naturalistic horses. The temple also houses several other deities including Shiva, Parvati and Ganesha.

    The temple was built by Sanskriti Vihar, a charitable trust, headed by Shri Sita Ram Maroo, the Managing Director of Ranchi Express Group. The foundation stone was laid by Swami Shri Vasudevanand Saraswati on 24 October 1991 and the Prana Pratishtha was undertaken by Swami Shri Vamdev Ji Maharaj on 10 July 1994.

    A Dharmashala for pilgrims has been constructed. There is also a pond where devotees can bathe during Chhath Puja for worshiping the Sun God.

    """
    T.insert(tk.END, quote)
    T.config(state = "disabled",bg = "black", fg = "white")

    #instructig to check the menu bar in frame 5
    tk.Label(fbasetext1, text = '''The Above content is from wikipideya !''',
    font = "times 15 bold italic", bg = "black", fg = "red", justify = "left",anchor = "nw").pack(fill = "x", padx = 5, side = 'top')
    temp.mainloop()
#about Section 
#about software 
def abs():
    temp = Toplevel()
    temp.title('About Software')
    temp.geometry("400x400")
    temp.state('zoomed')
    temp.config(bg ='black')
    tk.Label(temp, text = 'About sotware:', font = 'times 20 bold italic underline',anchor = 'nw', bg = 'black', fg = 'yellow').pack(side = 'top', fill = 'x')
    tk.Label(temp, text = 'Description:', font = 'times 18 bold italic underline',anchor = 'nw', bg = 'black', fg = 'orange').pack(side = 'top', fill = 'x')
    S = tk.Scrollbar(temp)
    T = tk.Text(temp, height=2, width=200)
    S.pack(side=tk.RIGHT, fill=tk.Y)
    T.pack(side=tk.LEFT, fill=tk.Y)
    S.config(command=T.yview)
    T.config(yscrollcommand=S.set)
    quote = """This software is developed by Awanish Kumar in aprox 20 days of hard work though i would like acknowledge some of helping factors that are listed: - 
    My professor 
    My Trust
    My best Buddy's 
    My friends 
    My parents 
    My well wisher's
    And Many More
    This software contains the copyright so do ask me before downloading the code from git 

    Thank You 
    """
    T.insert(tk.END, quote)
    T.config(state = "disabled",bg = "black", fg = "white")
    temp.mainloop()
#about developer
def abd():
    temp = tk.Toplevel()
    temp.title('About Developer')
    temp.geometry("400x600")
    temp.state('zoomed')
    temp.configure(bg = 'black')
    #Frames for the Relegious window
    f1 = tk.Frame(temp, borderwidth = 0,bg = 'black' , relief = "sunken")
    f2 = tk.Frame(temp, borderwidth = 0,bg = 'black' , relief = "sunken")
    f3 = tk.Frame(temp, borderwidth = 0,bg = 'black' , relief = "sunken")
    #packing the frames in the correct position
    f1.pack(side = "top",fill = "y", anchor = 'w')
    f2.pack(side = "top",fill = "x")
    f3.pack(side = "top",fill = "y", anchor = 'e')
    #content of F1
    text1 = tk.Text(f1, height=20, width=30)
    pic = tk.PhotoImage(file='./res/awanish1.gif')
    text1.insert(tk.END, '\n')
    text1.image_create(tk.END, image=pic)

    text1.pack(side=tk.LEFT)

    text2 = tk.Text(f1, height=20, width=50)
    scroll = tk.Scrollbar(f1, command=text2.yview)
    text2.configure(yscrollcommand=scroll.set)
    text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 20, 'bold'))
    text2.tag_configure('color',
                        foreground='#476042',
                        font=('Tempus Sans ITC', 12, 'bold'))
    text2.tag_bind('follow',
                '<1>',
                lambda e, t=text2: t.insert(tk.END, "Not now, maybe later!"))
    text2.insert(tk.END,'\nAwanish Kumar\n', 'big')
    quote = """
    Awanish Kumar:
    I'm the student of sarala Birla University:
    Roll no - BCA 190039\n
    i developed this software Ranchi tourism
    Assigned by My professor Shridhar B Dandin,
    Hope you all like My work
    """
    text2.insert(tk.END, quote, 'color')
    text2.insert(tk.END, 'follow-up\n', 'follow')
    text2.pack(side=tk.LEFT)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)
    # content of frame 2
    
    
    marquee = Marquee(f2, text="This Application is developed by Awanish Kumar under the Guidence of", borderwidth=0, relief="flat", bg = 'lightblue')
    marquee.pack(side="top", fill="x", pady=10)


    #conteent of frame 3
    text1 = tk.Text(f3, height=20, width=30)
    photo = tk.PhotoImage(file='./res/prof sb dandin.gif')
    text1.insert(tk.END, '\n')
    text1.image_create(tk.END, image=photo)

    text1.pack(side=tk.LEFT)

    text2 = tk.Text(f3, height=20, width=50)
    scroll = tk.Scrollbar(f3, command=text2.yview)
    text2.configure(yscrollcommand=scroll.set)
    text2.tag_configure('bold_italics', font=('Arial', 12, 'bold', 'italic'))
    text2.tag_configure('big', font=('Verdana', 20, 'bold'))
    text2.tag_configure('color',
                        foreground='#476042',
                        font=('Tempus Sans ITC', 12, 'bold'))
    text2.tag_bind('follow',
                '<1>',
                lambda e, t=text2: t.insert(tk.END, "Not now, maybe later!"))
    text2.insert(tk.END,'\nProf Shridhar B Dandin\n', 'big')
    quote = """
    Associate Professor
    B.E., M.S., Ph.D(Pursuing)
    Department of CSE
    And our Python Teacher
    He helped me a lot in encouraging me 
    to complete my project Ranchi tourism 
    Thanks a lot to sir  
    """
    text2.insert(tk.END, quote, 'color')
    text2.insert(tk.END, 'follow-up\n', 'follow')
    text2.pack(side=tk.LEFT)
    scroll.pack(side=tk.RIGHT, fill=tk.Y)

    temp.mainloop()