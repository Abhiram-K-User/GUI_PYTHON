#Made by Abhiram.K!
import tkinter as tk
from tkinter import messagebox
c=tk.Tk()
#A display to show the calculations
ui_bar=tk.StringVar()
#A list to store the elements
s1=[]
total=0
#Appending numbers and arithmetic operators
def num_append(num):
    global total
    total=total*10+num
    ui_bar.set(total)

def str_append(oper):
    global total
    s1.append(total)
    s1.append(oper)
    ui_bar.set(s1)
    total=0
#Main code to compute numbers from the list
def calc():
    global total
    s1.append(total)
    res=0
    i=1
    while i<len(s1)-1:
        if s1[i] == "+":
            s1[i+1]=s1[i-1]+s1[i+1]         
        elif s1[i] == "-":
            s1[i+1]=s1[i-1]-s1[i+1]
        elif s1[i] == "*":
            s1[i+1]=s1[i-1]*s1[i+1]
        elif s1[i] == "/":
            try:
                s1[i+1]=s1[i-1]/s1[i+1]
            #In case of division by Zero
            except ZeroDivisionError:
                messagebox.showerror("ERROR!","Division by Zero is Invalid!")
        i+=2
    res=s1[len(s1)-1]
    ui_bar.set(res)
    s1.clear()
    res=0
    total=0

opers=['+','-','*','/']
x1=y1=40
j=1
c.geometry("400x500")
c.title("My Calculator")
#A label to display the current numbers
w=tk.Label(c,textvariable=ui_bar,bg="GREEN",fg="WHITE")
w.config(font=("Arial",18))
w.place(x=100,y=0)
#A loop to display buttons from 0-9
for i in range(0,9):
    if i%3==0:
        y1+=40
        x1=40
    button=tk.Button(c,width=5,text=f"{j}",command=lambda j=j :num_append(j))
    button.place(x=x1,y=y1)
    x1+=40
    j+=1
button=tk.Button(c,width=5,text="0",command=lambda:num_append(0))
button.place(x=80,y=200)
x1=300
y1=40
#Buttons for arithmetic operators
button=tk.Button(c,width=5,text="+",command=lambda:str_append("+"))    
button.place(x=200,y=240)
button=tk.Button(c,width=5,text="-",command=lambda:str_append("-"))    
button.place(x=200,y=270)
button=tk.Button(c,width=5,text="*",command=lambda:str_append("*"))    
button.place(x=200,y=300)
button=tk.Button(c,width=5,text="/",command=lambda:str_append("/"))    
button.place(x=200,y=330)
button=tk.Button(c,width=5,text="=/AC",command=lambda: calc())
button.place(x=200,y=360)
#End of the GUI loop
c.mainloop()

