'''
To do List of the game 
1: => create the frame to make the proper allign of the tickets and the Tambola Board . done()
2: => Create the ticket for the Tambola Game (For Now the algorithm of the ticket will be constant but latter the ticket will be random )
3: =>Create the main menu for the tambola game and the documentation section of the tambola game 
4 : => Create the registration  form for filling the name of the players 
5 : => Create the Exit buton for the game 
6: => Wraping up the project for the host 
'''
#imprting the Necessary file's
import tkinter as tk
import random 
from tkinter import messagebox as mb
# to change the color in the click we need to declare the all  main and the secondry variable as global     
x1 = 0
y1 = 0   
z1 = 10
q1 = 10
a = 0
print(z1)
print(q1)
#variables for declaring the Winner
r1_t1 = 0
r2_t1 = 0
r3_t1 = 0
def tambola():
    root = tk.Toplevel()
    root.geometry("400x400")
    root.title('Tambola game')
    root.config(bg = 'white')
    root.state('zoomed')
    #frame to align the host and the ticket
    framehead = tk.Frame(root, borderwidth = 0, bg = 'white', relief = 'ridge') 
    framehost = tk.Frame(root, borderwidth = 5, bg = 'white', relief = 'ridge')
    frameticket = tk.Frame(root, borderwidth = 5, bg = 'white', relief = 'ridge')
    frameticket1 = tk.Frame(frameticket, borderwidth = 5, bg = 'white', relief = 'ridge')
    framedeclare = tk.Frame(frameticket, borderwidt = 0, bg = 'white', relief = 'ridge')


    #packing the frame to the proper alignment 
    framehead.pack(side = 'top', fill = 'x')
    framehost.pack(side = 'left',  fill = 'y')
    frameticket.pack(side = 'right',  fill = 'y')
    frameticket1.pack(side = 'top',  fill = 'x')
    framedeclare.pack(side = 'top',  fill = 'both')
    #making comment function
    # tk.Label(framecoment,text = 'Comment: -', font = 'comicsans 15 bold italic', bg ='white', fg = 'red', anchor = 'nw').pack(fill = 'x')
    # labelVar = tk.StringVar()
    # comm = tk.Label(framecoment, textvariable=labelVar, font = 'times 15 bold ', bg = 'black', fg = 'yellow')
    # comm.pack(pady = 15)    
    # comm.configure(text = a)
    #creating the heading of the play window
    tk.Label(framehead, text = "Welcome to the Tambola game: -", font = 'times 15 bold ', bg = 'white', fg = 'black',anchor = 'nw').pack(fill = 'x', pady = 10)  
    #creating the host side
    x1 = 10
    y1 = 10
    canvas = tk.Canvas(framehost, width = 560 ,  height = 500 , bg = 'white')
    num = 1
    for j in range(9):
        for i in range(10):
            canvas.create_oval(x1,y1,x1+50,y1+50, outline = 'black',width = 0, fill = 'lightblue')
            tk.Label(canvas, text = str(num)).place(x = x1 + 16, y = y1+16)
            # print(f"the value of label = {num} and the value of x1 = {x1} the value of  y1 = {y1}")
            x1 = x1+55
            num = num+1
        y1 = y1+55
        x1 = 10
        canvas.pack()
    #generating the Ticket1
    tk.Label(frameticket1, text = 'Angry Ticket: -', font = 'times 18 bold', bg = 'white', fg = 'red').pack(anchor = 'nw')
    t1 = 10
    t2 = 10
    ticket1 =  tk.Canvas(frameticket1, width = 510,  height = 180 , bg = 'black')
    for j in range(3):
        for i in range(9):
            ticket1.create_rectangle(t1,t2,t1+50,t2+50, outline = 'white', fill = 'lightblue')
            tk.Label(ticket1, text = "17").place(x = 65 + 16, y = 10+16)
            tk.Label(ticket1, text = "23").place(x = 120 + 16, y = 10+16)
            tk.Label(ticket1, text = "42").place(x = 230 + 16, y = 10+16)
            tk.Label(ticket1, text = "54").place(x = 285 + 16, y = 10+16)
            tk.Label(ticket1, text = "85").place(x = 450 + 16, y = 10+16)
            tk.Label(ticket1, text = "4").place(x = 10 + 16, y = 65+16)
            tk.Label(ticket1, text = "27").place(x = 120 + 16, y = 65+16)
            tk.Label(ticket1, text = "30").place(x = 175 + 16, y = 65+16)
            tk.Label(ticket1, text = "58").place(x = 285 + 16, y = 65+16)
            tk.Label(ticket1, text = "74").place(x = 395 + 16, y = 65+16)
            tk.Label(ticket1, text = "8").place(x = 10 + 16, y = 120+16)
            tk.Label(ticket1, text = "33").place(x = 175 + 16, y = 120+16)
            tk.Label(ticket1, text = "44").place(x = 230 + 16, y = 120+16)
            tk.Label(ticket1, text = "62").place(x = 340 + 16, y = 120+16)
            tk.Label(ticket1, text = "87").place(x = 450 + 16, y = 120+16)
            # print(f"the number of the block {num} x1 = {x1} y1 = {y1}")
            t1 = t1+55
        t2 = t2+55
        t1 = 10
        ticket1.pack(padx = 120)
    # generating the Second Ticket
    tk.Label(frameticket1, text = 'Poison Ticket: -', font = 'times 18 bold', bg = 'white', fg = 'red').pack(anchor = 'nw')
    t1 = 10 
    t2 = 10
    ticket2 =  tk.Canvas(frameticket1, width = 510,  height = 180 , bg = 'black')
    for j in range(3):
        for i in range(9):
            ticket2.create_rectangle(t1,t2,t1+50,t2+50, outline = 'white', fill = 'lightblue')
            tk.Label(ticket2, text = "16").place(x = 65 + 16, y = 10+16)
            tk.Label(ticket2, text = "22").place(x = 120 + 16, y = 10+16)
            tk.Label(ticket2, text = "41").place(x = 230 + 16, y = 10+16)
            tk.Label(ticket2, text = "60").place(x = 340 + 16, y = 10+16)
            tk.Label(ticket2, text = "80").place(x = 450 + 16, y = 10+16)
            tk.Label(ticket2, text = '5').place(x = 10 + 16, y = 65+16)
            tk.Label(ticket2, text = "26").place(x = 120 + 16, y = 65+16)
            tk.Label(ticket2, text = "48").place(x = 230 + 16, y = 65+16)
            tk.Label(ticket2, text = "63").place(x = 340 + 16, y = 65+16)
            tk.Label(ticket2, text = "83").place(x = 450 + 16, y = 65+16)
            tk.Label(ticket2, text = "29").place(x = 120 + 16, y = 120+16)
            tk.Label(ticket2, text = "31").place(x = 175 + 16, y = 120+16)
            tk.Label(ticket2, text = "57").place(x = 285 + 16, y = 120+16)
            tk.Label(ticket2, text = "79").place(x = 395 + 16, y = 120+16)
            tk.Label(ticket2, text = "86").place(x = 450 + 16, y = 120+16)
            # print(f"the number of the block {num} x1 = {x1} y1 = {y1}")
            t1 = t1+55
        t2 = t2+55
        t1 = 10
        ticket2.pack(padx = 120)
    # making the function to correct the first index of the value of  y1 
    #  defining the function to get the click to be done 
    def click_me():
        global z1
        global q1
        global x1
        global y1
        #Taking the value of  main variable to the secondry variable 
        z1 = x1
        q1 = y1
        print(z1)
        print(q1)
        numx = random.randint(0,9)
        numy = random.randint(0,8)
        # again taking the value of the main variable to the secondry variable to fix some bug
        z1 = x1
        q1 = y1
        x1 = 10+55*numx
        y1 = 10+55*numy
        canvas.create_oval(x1,y1,x1+50,y1+50, outline = 'black',width = 0, fill = 'red')
        canvas.pack()
        #condition to change the color after the second click 
        canvas.create_oval(z1,q1,z1+50,q1+50, outline = 'black',width = 0,fill ='blue')
        canvas.pack()
        def commentry():
            #creating the variable that will store the value of comment
            global a
            #creating the commentry Section
            if x1 == 230 and y1 == 65:
                mb.showinfo(title = 'Commentry', message= ' The day we celebrate independence day! \nThe Number is 15 ')
            elif x1 == 285 and y1 == 10:
                # labelVar.set('And that is a Sixer, hit by Sehwag! \n The Number is 6')
                mb.showinfo(title = 'Commentry', message= 'And that is a Sixer, hit by Sehwag! \n The Number is 6')
            elif x1 == 175 and y1 == 10:
                # labelVar.set('A Boundary Hit by sachin ! \n The number is 4 ')
                mb.showinfo(title = 'Commentry', message = 'A Boundary Hit by sachin ! \n The number is 4 ')
            elif x1 == 340 and y1 == 10:
                mb.showinfo(title = 'Commentry', message = 'A Boundary Hit by sachin ! \n The number is 4 ')
            elif x1 == 285 and y1 == 120:
                mb.showinfo(title = 'Commentry', message = 'A Boundary Hit by sachin ! \n The number is 4 ')
            elif x1 == 340 and y1 == 395:
                mb.showinfo(title = 'Commentry', message = 'A Boundary Hit by sachin ! \n The number is 4 ')
            elif x1 == 65 and y1 ==10:
                mb.showinfo(title = 'Commentry', message = 'A Boundary Hit by sachin ! \n The number is 4 ')
            elif x1 == 505 and y1 == 285:
                mb.showinfo(title = 'Commentry', message = 'Retirement Day ! \n The Number is 60')
            else:
                pass
        commentry()
        # conditional statement of the Ticket 1
        def condi_ticket1():
            global r1_t1
            global r2_t1
            global r3_t1
            if x1 == 340 and y1 == 65:
                # r1_t1 += 65
                ticket1.create_rectangle(65, 10, 65+50, 10+50, outline = 'black',fill = 'orange')
            elif x1 == 120 and y1 == 120:
                # r1_t1 += 120
                ticket1.create_rectangle(120 , 10, 120+50, 10+50, outline = 'black', fill = 'orange')
            elif x1 == 65 and y1 == 230:
                # r1_t1 += 230
                ticket1.create_rectangle(230 , 10, 230+50, 10+50, outline = 'black', fill = 'orange')
            elif x1 == 175 and y1 == 285:
                # r1_t1 += 285
                ticket1.create_rectangle(285 , 10, 285+50, 10+50, outline = 'black', fill = 'orange')
            elif x1 == 230 and y1 == 450:
                # r1_t1 += 450
                ticket1.create_rectangle(450 , 10, 450+50, 10+50, outline = 'black', fill = 'orange')
            elif x1 == 175 and y1 == 10:
                # r2_t1 += 10
                ticket1.create_rectangle(10 , 65, 10+50, 65+50, outline = 'black', fill = 'green')
            elif x1 == 340 and y1 == 120:
                # r2_t1 += 120
                ticket1.create_rectangle(120 , 65, 120+50, 65+50, outline = 'black', fill = 'green')
            elif x1 == 505 and y1 == 120:
                # r2_t1 += 175
                ticket1.create_rectangle(175 , 65, 175+50, 65+50, outline = 'black', fill = 'green')
            elif x1 == 395 and y1 == 285:
                # r2_t1 += 285
                ticket1.create_rectangle(285 , 65, 285+50, 65+50, outline = 'black', fill = 'green')
            elif x1 == 175 and y1 == 395:
                # r2_t1 += 395
                ticket1.create_rectangle(395 , 65, 395+50, 65+50, outline = 'black', fill = 'green')
            elif x1 == 395 and y1 == 10:
                # r3_t1 += 10
                ticket1.create_rectangle(10 , 120, 10+50, 120+50, outline = 'black', fill = 'yellow')
            elif x1 == 120 and y1 == 175:
                # r3_t1 += 175
                ticket1.create_rectangle(175 , 120, 175+50, 120+50, outline = 'black', fill = 'yellow')
            elif x1 == 175 and y1 == 230:
                # r3_t1 += 230
                ticket1.create_rectangle(230 , 120, 230+50, 120+50, outline = 'black', fill = 'yellow')
            elif x1 == 65 and y1 == 340:
                # r3_t1 += 340
                ticket1.create_rectangle(340 , 120, 340+50, 120+50, outline = 'black', fill = 'yellow')
            elif x1 == 340 and y1 == 450:
                # r3_t1 += 450
                ticket1.create_rectangle(450 , 120, 450+50, 120+50, outline = 'black', fill = 'yellow')
            else:
                pass
            # if r1_t1 == 1150:
            #     tk.Label(framedeclare, text = 'Angry Ticket => Top Row Completed !', bg = 'white', fg = 'red', font = 'times 15 bold', ).pack(side = 'top',anchor = 'nw')
            # elif r2_t1 == 985:
            #     tk.Label(framedeclare, text = 'Angry Ticket => Mid Row Completed !', bg = 'white', fg = 'orange', font = 'times 15 bold', ).pack(side = 'top', anchor = 'nw')
            # elif r3_t1 == 1205:
            #     tk.Label(framedeclare, text = 'Angry Ticket => Bottom Row Completed !', bg = 'white', fg = 'orange', font = 'times 15 bold', ).pack(side = 'top', anchor = 'nw')
            # elif r1_t1 == 1150 and r2_t1 == 985 and r3_t1 == 1205:
            #     mb.showerror('winner', message = 'Angry is the winner', parent=root)
        condi_ticket1()
        #condition For Ticket 2
        def condi_ticket2():
            if x1 == 285 and y1 == 65:
                ticket2.create_rectangle(65, 10, 65+50, 10+50, outline = 'black',fill = 'orange')
            elif x1 == 65 and y1 == 120:
                ticket2.create_rectangle(120 , 10, 120+50, 10+50, outline = 'black', fill = 'orange')
            elif x1 == 10 and y1 == 230:
                ticket2.create_rectangle(230 , 10, 230+50, 10+50, outline = 'black', fill = 'orange')
            elif x1 == 505 and y1 == 285:
                ticket2.create_rectangle(340 , 10, 340+50, 10+50, outline = 'black', fill = 'orange')
            elif x1 == 505 and y1 == 395:
                ticket2.create_rectangle(450 , 10, 450+50, 10+50, outline = 'black', fill = 'orange')
            elif x1 == 230 and y1 == 10:
                ticket2.create_rectangle(10 , 65, 10+50, 65+50, outline = 'black', fill = 'green')
            elif x1 == 285 and y1 == 120:
                ticket2.create_rectangle(120 , 65, 120+50, 65+50, outline = 'black', fill = 'green')
            elif x1 == 395 and y1 == 230:
                ticket2.create_rectangle(230 , 65, 230+50, 65+50, outline = 'black', fill = 'green')
            elif x1 == 120 and y1 == 340:
                ticket2.create_rectangle(340 , 65, 340+50, 65+50, outline = 'black', fill = 'green')
            elif x1 == 120 and y1 == 450:
                ticket2.create_rectangle(450 , 65, 450+50, 65+50, outline = 'black', fill = 'green')
            elif x1 == 450 and y1 == 120:
                ticket2.create_rectangle(120 , 120, 120+50, 120+50, outline = 'black', fill = 'yellow')
            elif x1 == 10 and y1 == 175:
                ticket2.create_rectangle(175 , 120, 175+50, 120+50, outline = 'black', fill = 'yellow')
            elif x1 == 340 and y1 == 285:
                ticket2.create_rectangle(285 , 120, 285+50, 120+50, outline = 'black', fill = 'yellow')
            elif x1 == 450 and y1 == 395:
                ticket2.create_rectangle(395 , 120, 395+50, 120+50, outline = 'black', fill = 'yellow')
            elif x1 == 285 and y1 == 450:
                ticket2.create_rectangle(450 , 120, 450+50, 120+50, outline = 'black', fill = 'yellow')
            else:
                pass
        condi_ticket2()
    #hear the lamda is the one liner function
    tk.Button(framehost ,  text = 'click me', command = lambda: [click_me()], bg = 'grey', fg = 'black', relief = 'ridge',font = 'times 15 bold italic').pack(fill = 'x')
    tk.Label(framedeclare, text = 'Declaration: -', font = 'times 20 bold', fg = 'black', bg = 'white').pack(anchor = 'nw')
    root.mainloop()    
#Main Window created With Freehand Python code
root = tk.Tk()
root.geometry("600x600")
root.config(bg = 'black')
root.state('zoomed')
root.title()
frame = tk.Frame(root, borderwidth =  5, bg = 'white', relief = 'sunken')
frame1 = tk.Frame(root, borderwidth =  0, bg = 'black', relief = 'sunken')
frame.pack(side = 'top',fill = 'y')
frame1.pack(side = 'bottom', anchor = 'nw', fill = 'x')
tk.Label(frame, text = 'Tambola By Juhi Kumari\n', font = 'comicsans 40 bold', bg = 'white').pack(fill = 'x')
tk.Button(frame,  text = 'Play now', command = lambda: [tambola()], bg = 'white', fg = 'black', relief = 'ridge',font = 'times 15 bold italic').pack(pady = 10)
tk.Button(frame,  text = 'Quit', command = lambda: [root.destroy()], bg = 'white', fg = 'black', relief = 'ridge',font = 'times 15 bold italic').pack(pady = 15)
tk.Label(frame, text = '\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n', bg = 'white').pack()
tk.Label(frame1, text = 'Acknowledgement: -', font = 'comicsans 30 bold',bg = 'black', fg = 'White').pack(anchor = 'nw',fill='x')
tk.Label(frame1, text = 'SB Dandin sir', font = 'comicsans 15 bold', fg = 'Red', bg = 'black').pack(fill ='x')
tk.Label(frame1, text = 'Awanish Kumar', font = 'comicsans 15 bold', fg = '#FFDAB9', bg = 'black').pack(fill ='x')


root.mainloop()