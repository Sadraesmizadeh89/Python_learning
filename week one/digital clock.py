from tkinter import *
import time

window = Tk()
window.title('digital clock')
window.geometry('600x400')

def myTime():
    hour = time.strftime('%H')
    minute = time.strftime('%M')
    second =time.strftime('%S')
    AM_PM = time.strftime('%p')
    day = time.strftime('%A')
    zone = time.strftime('%Z')

    mytext = hour + ':' + minute + ':' + second + ' ' + AM_PM
    mytext2 = day + ', ' + zone
    myLabel.config(text=mytext)
    myLabel2.config(text=mytext2)
    myLabel.after(1000, myTime)
    

myLabel = Label(window, text='', font=('Arial', 70  ), fg='white', bg='blue')
myLabel.pack()
myLabel2 = Label(window, text='H', font=('Arial', 24))
myLabel2.pack()

myTime()

window.mainloop()