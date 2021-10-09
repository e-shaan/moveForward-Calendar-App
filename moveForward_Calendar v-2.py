from tkinter import *
from tkcalendar import *
import datetime
import calendar
import tkinter.font as tkFont




def grab_date():
    
    batch = ''
    for i in range(7):
        if checklist[i].get()==1:
            batch += days[i]
            
    Batch = str(batch)
    print(Batch)
    date = cal.get_date()

    
    
    date =datetime.datetime.strptime(date, "%m/%d/%y").strftime("%d/%m/%y")
    date = datetime.datetime.strptime(date, '%d/%m/%y')

    day = calendar.day_name[date.weekday()]



    sessions = int( session_entry.get())

    sessions = sessions+1

    
    while sessions!=0:
        if sessions == 3:
            stop_date = date + datetime.timedelta(1)
            #stop_day = calendar.day_name[date.weekday()]

        date = date + datetime.timedelta(1)
        day = calendar.day_name[date.weekday()]

        if day in Batch:
            sessions = sessions -1



    stop_date = stop_date.strftime("%d/%m/%y")
    next_date = date.strftime("%d/%m/%y")
    #print(stop_date)

    

    text = "Batch Stop Date :  " +stop_date
    my_label.config(text = text)

    text = "Next Batch Date :  " +next_date
    my_label2.config(text = text)


#create the user interface

#main root window
root = Tk()
root.title('moveForward Calendar')
#root.iconbitmap("logo.ico")
root.geometry('800x600')
root.configure(bg='#646EA4')

root.state('zoomed')

#calendar module
date_today = datetime.date.today()
cal = Calendar(root ,selectmode = 'day', year=date_today.year, month=date_today.month , day = date_today.day) 
cal.pack( fill='both', expand = True)
fontStyle1 = tkFont.Font(family="Comic Sans MS", size=12)
fontStyle2 = tkFont.Font(family="Comic Sans MS", size=14)    


left_frame = Frame(root)
left_frame.pack(padx= 60 ,side=LEFT)


right_frame = Frame(root)
right_frame.pack(padx= 60 , side=RIGHT)

bottom_frame = Frame(root)
bottom_frame.pack(  side=BOTTOM)


#list to store the days
days = ["Monday" , "Tuesday", "Wednesday" ,"Thursday","Friday" , "Saturday" ,"Sunday"]

#list to store the days off/on value

checklist = []

for i in range(7):
    checklist.append(0)
    checklist[i]= IntVar()

    C1 = Checkbutton(root, bg='#646EA4',font = fontStyle2, text = days[i], variable = checklist[i], \
                 onvalue = 1, offvalue = 0, height=1, \
                 width = 10)

    C1.pack()
    



my_label2 = Label(root ,text = 'Next Batch Date : ' ,font = fontStyle2,  bg="coral", fg="midnight blue")
my_label2.pack(pady =0,expand=True,side=BOTTOM)

my_label = Label(root ,text = 'Batch Stop Date : ' ,font = fontStyle2,  bg="coral", fg="midnight blue")
my_label.pack(pady =4,expand=True,side=BOTTOM)





my_button = Button(root,text = 'Get Dates',command = grab_date,font = fontStyle2,  bg="coral", fg="midnight blue")
my_button.pack(expand=False,side=BOTTOM)
session = StringVar(root, value='Enter number of sessions...')
session_entry = Entry(root,justify =CENTER,fg="midnight blue",bg='coral',font = fontStyle2 ,textvariable = session) 

session_entry.pack(pady =7,expand=True,side=BOTTOM)




root.mainloop()









