from tkinter import Label, Tk 
import time
app_window = Tk() 
app_window.title("clock") 
app_window.geometry("450x150") 
app_window.resizable(5,5)

text_font= ("Boulder", 75, 'bold')
background = "#ffd700"
foreground= "#363529"
border_width = 30

label = Label(app_window, font=text_font, bg=background, fg=foreground, bd=border_width) 
label.grid(row=0, column=1)

def digital_clock(): 
   time_live = time.strftime("%H:%M:%S")
   label.config(text=time_live) 
   label.after(300, digital_clock)

digital_clock()
app_window.mainloop()