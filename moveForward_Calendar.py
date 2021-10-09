from tkinter import *
from tkcalendar import *
import datetime
import calendar
import tkinter.font as tkFont


def cal_sessions(course , level):

    session_dictionary ={
            'Primary(7-9)'      : {'1' : 9,  '2' : 12, '3' : 12} ,
            'Middle(10-12)'     : {'1' : 9,  '2' : 12, '3' : 12} ,
            'AI_Junior(7-12)'   : {'1' : 10, '2' : 12} ,
            'Python_one_hour(13+)'       : {'1' : 12,  '2' : 12,  '3A' : 12,  '3B' : 12,  '3C' : 12} ,
            'Python_two_hours(13+)'       : {'1' : 6,  '2' : 6,  '3A' : 6,  '3B' : 6,  '3C' : 6} ,
            'Python_AI(13+)'    : {'3A' : 6,  '3B' : 6,  '3C' : 6}
            }

    try:
        sessions = session_dictionary[course][level]
    except:
        sessions = 'Invalid Level'

    return sessions


def grab_date():
    Batch = batch.get()
    date = cal.get_date()

    
    
    date =datetime.datetime.strptime(date, "%m/%d/%y").strftime("%d/%m/%y")
    date = datetime.datetime.strptime(date, '%d/%m/%y')

    day = calendar.day_name[date.weekday()]

    if Batch == 'Batch ':
        my_label.config(text = "Enter Batch! ")
        my_label2.config(text = "Enter Batch! ")
        return



    if day not in Batch:
        my_label.config(text = "Invalid Batch! ")
        my_label2.config(text = "Invalid Batch! ")
        return    
        


    sessions = cal_sessions(course.get() , level.get())
    
    if sessions == 'Invalid Level':
        my_label.config(text = sessions)
        my_label2.config(text = sessions)
        return

    sessions = int(sessions)+1

    
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

root = Tk()
root.title('moveForward Calendar')
#root.iconbitmap("logo.ico")
root.geometry('640x500')
root.configure(bg='#646EA4')


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



batch = StringVar()
batch.set('Batch ')
batch_options = [ '(MWF) Monday_Wednesday_Friday' ,
            '(TTSat) Tuesday_Thursday_Saturday',
            '(TTSun) Tuesday_Thursday_Sunday',
            '(ThurSun) Thursday_Sunday',
            '(TueSat) Thursday_Saturday',
            '(MWF) Monday_Tuesday_Wednesday',
            '(WSun) Wednesday_Sunday',
            '(TT) Tuesday_Thursday',
            '(MF) Monday_Friday',
            '(TueF) Tuesday_Friday',
            '(Sat) Saturday',
            '(SatSun) Saturday_Sunday']

batch_drop = OptionMenu(root, batch ,*batch_options)
batch_drop.config(font = fontStyle2,  bg="coral", fg="midnight blue")
batch_drop.pack(expand=True,side=TOP)

course = StringVar()

course.set('Course ')
course_options = [ 'Primary(7-9)' ,
            'Middle(10-12)',
            'AI_Junior(7-12)',
            'Python_one_hour(13+)',
            'Python_two_hours(13+)',      
            'Python_AI(13+)']

age_drop = OptionMenu(root, course ,*course_options)
age_drop.config(font = fontStyle1,  bg="coral", fg="midnight blue") 
age_drop.pack(expand=True,side=TOP)

level = StringVar()
level.set('Level ')
level_options = [ '1' ,
            '2',
            '3',
            '3A',
            '3B',
            '3C']

level_drop = OptionMenu(root, level ,*level_options)
level_drop.config(font = fontStyle1,  bg="coral", fg="midnight blue")
level_drop.pack(expand=True,side=TOP)



my_button = Button(root,text = 'Get Stop Date',command = grab_date,font = fontStyle2,  bg="coral", fg="midnight blue")
my_button.pack(expand=False)



my_label2 = Label(root ,text = 'Next Batch Date : ' ,font = fontStyle2,  bg="coral", fg="midnight blue")
my_label2.pack(pady =0,fill=X,expand=True,side=BOTTOM)

my_label = Label(root ,text = 'Batch Stop Date : ' ,font = fontStyle2,  bg="coral", fg="midnight blue")
my_label.pack(pady =10,fill=X,expand=True,side=BOTTOM)


root.mainloop()









