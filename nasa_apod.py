import requests as rq
import tkinter as tk
from PIL import Image,ImageTk
from io import BytesIO
from tkinter import messagebox
root=tk.Tk()
root.title("APOD Displaying App")
year_var=tk.StringVar()
month_var=tk.StringVar()
day_var=tk.StringVar()

def retrieve_image(url):
    try:
        request=rq.get(url)
        img=request.content
        return img
    except:
        print("Image retrieval error")

def secondary_win():
    a=rq.get(f"https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&date={year_var.get()}-{month_var.get()}-{day_var.get()}")
    if(a.status_code==200):
        sub_win=tk.Toplevel()
        b=a.json()
        c=b['hdurl']
        desc=b['explanation'] #Description of APOD
        nasa_img=Image.open(BytesIO(retrieve_image(c)))
        nasa_img.thumbnail((600,400),Image.LANCZOS) 
        photo=ImageTk.PhotoImage(nasa_img)
        img_label=tk.Label(sub_win,image=photo)
        img_label.pack()
        img_label.image=photo #creates a reference for the photo
        sub_text=tk.Label(sub_win,text="Description",font=("Arial",15,"bold"),bg="light green").pack()
        img_desc=tk.Label(sub_win,text=desc,wraplength=600,bg="light blue")
        img_desc.pack()
    else:
        messagebox.showerror(message=f"An error has occurred Status Code: {a.status_code}",title="ERROR")

display_quer=tk.Label(root,text="Enter the Year, Month and Day respectively in the boxes",font=("Times New Roman",16,"bold"))
display_quer.grid(row=1,column=0)
year_label=tk.Label(root,text="Year:")
year_label.grid(row=3,column=0)
year_entry=tk.Entry(root,textvariable=year_var)
year_entry.grid(row=3,column=1)
month_label=tk.Label(root,text="Month:")
month_label.grid(row=3,column=2)
month_entry=tk.Entry(root,textvariable=month_var)
month_entry.grid(row=3,column=3)
day_label=tk.Label(root,text="Day:")
day_label.grid(row=3,column=4)
day_entry=tk.Entry(root,textvariable=day_var)
day_entry.grid(row=3,column=5)
submit_button=tk.Button(root,command=lambda:secondary_win(),text="Submit")
submit_button.grid(row=4,column=1)
root.mainloop()
