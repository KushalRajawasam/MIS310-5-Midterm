from tkinter import *
from PIL import ImageTk, Image
import pandas as pd

root = Tk()
root.title('CCSU Mobile App')
root.geometry("800x600")
root.resizable(False, False)
root.configure(bg='light blue')

img = Image.open('logo1.png')
try:
    img = img.resize((100, 100), Image.Resampling.LANCZOS)
except AttributeError:
    img = img.resize((100, 100), Image.ANTIALIAS)
img = img.convert("RGBA")
data_img = img.getdata()
newData = []
for item in data_img:
    if item[:3] == (255, 255, 255):
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
img.putdata(newData)
img.save("transparent.png")
logo = Image.open("transparent.png")
logo = ImageTk.PhotoImage(logo)
logoLabel = Label(root, image=logo, bg='light blue')
logoLabel.place(x=10, y=10)

data = pd.read_csv("midterm_exam_2.csv")

lb = Label(root, justify="left", bg="light blue", anchor="nw", wraplength=540)
lb.place(x=130, y=200)

def calender():
    col = 'CalendarDate'
    df = pd.DataFrame(data, columns=[col])
    selected_rows = df[~df[col].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=200)

def building():
    col = 'Buildings'
    df = pd.DataFrame(data, columns=[col])
    selected_rows = df[~df[col].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=200)

def faculty():
    col = 'FacultyName'
    df = pd.DataFrame(data, columns=[col])
    selected_rows = df[~df[col].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=200)

def school_of_business():
    col = 'SchoolOfBusiness' if 'SchoolOfBusiness' in data.columns else ('School of Business' if 'School of Business' in data.columns else None)
    if col is None:
        lb.config(text="School of Business column not found.")
        return
    df = pd.DataFrame(data, columns=[col])
    selected_rows = df[~df[col].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=200)

def mis_department():
    col = 'MISDepartment' if 'MISDepartment' in data.columns else ('MIS Department' if 'MIS Department' in data.columns else None)
    if col is None:
        lb.config(text="MIS Department column not found.")
        return
    df = pd.DataFrame(data, columns=[col])
    selected_rows = df[~df[col].isnull()]
    lb.config(text=selected_rows.to_string(index=False))
    lb.place(x=130, y=200)

btn_bg = "#2b4c7e"
btn_fg = "white"

button1 = Button(root, text='Calendar', command=calender, bg=btn_bg, fg=btn_fg, activebackground=btn_bg, activeforeground=btn_fg)
button1.place(x=50, y=120, width=110, height=30)

button2 = Button(root, text='Buildings', command=building, bg=btn_bg, fg=btn_fg, activebackground=btn_bg, activeforeground=btn_fg)
button2.place(x=170, y=120, width=110, height=30)

button3 = Button(root, text='Faculty', command=faculty, bg=btn_bg, fg=btn_fg, activebackground=btn_bg, activeforeground=btn_fg)
button3.place(x=290, y=120, width=110, height=30)

button4 = Button(root, text='School of Business', command=school_of_business, bg=btn_bg, fg=btn_fg, activebackground=btn_bg, activeforeground=btn_fg)
button4.place(x=50, y=160, width=200, height=30)

button5 = Button(root, text='MIS Department', command=mis_department, bg=btn_bg, fg=btn_fg, activebackground=btn_bg, activeforeground=btn_fg)
button5.place(x=270, y=160, width=200, height=30)

mainloop()
