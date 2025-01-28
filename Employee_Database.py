import tkinter as tk
from tkinter import messagebox
import json
main=tk.Tk()
main.title("Database Table")
main.geometry("400x400")
i=0
Employee=dict()
EmpName=tk.StringVar()
EmpId=tk.StringVar()
Designation=tk.StringVar()
Dob=tk.StringVar()
search_ele=tk.StringVar()

def create():
    Emp_Details=[]
    Emp_Details.append(EmpName.get())
    Emp_Details.append(Designation.get())
    Emp_Details.append(Dob.get())
    Employee[EmpId.get()]=Emp_Details
    EmpName.set("")
    EmpId.set("")
    Designation.set("")
    Dob.set("")

def search():
    if search_ele.get() in Employee:
        messagebox.showinfo(title="Result",message="Employee Found!")
        search_ele.set("")
    else:
        messagebox.showerror(title="Result",message="Employee not Found!")
        search_ele.set("")

def delete():
    if search_ele.get() in Employee:
        del Employee[search_ele.get()]
        messagebox.showinfo(message="Employee info successfully removed!")
    else:
        messagebox.showerror(message="Employee not Found!")

def create_window():
    win=tk.Toplevel(main)
    win.geometry("300x150")
    win.title("Creation Window")
    label=tk.Label(win,text="Name:").grid(row=0,column=0)
    entry=tk.Entry(win,textvariable=EmpName).grid(row=0,column=1)
    label=tk.Label(win,text="ID:").grid(row=1,column=0)
    entry=tk.Entry(win,textvariable=EmpId).grid(row=1,column=1)
    label=tk.Label(win,text="Designation:").grid(row=2,column=0)
    entry=tk.Entry(win,textvariable=Designation).grid(row=2,column=1)
    label=tk.Label(win,text="DOB:").grid(row=3,column=0)
    entry=tk.Entry(win,textvariable=Dob).grid(row=3,column=1)
    submit=tk.Button(win,text="Submit",command=lambda:create()).grid(row=4,column=1)

def search_window():
    s=tk.Toplevel(main)
    s.title("Search Window")
    s.geometry("300x100")
    label=tk.Label(s,text="Enter the Employee ID").pack()
    entry=tk.Entry(s,textvariable=search_ele).pack()
    submit=tk.Button(s,command=lambda:search(),text="Search").pack()

def display_employee():
    k=l=1
    q=tk.Toplevel(main)
    q.configure(bg="Black")
    q.title("Employee Table")
    heading=tk.Label(q,text="ID",bg="Black",fg="White",font=("Arial,30"),padx=10).grid(row=0,column=1)
    heading=tk.Label(q,text="Name",bg="Black",fg="White",font=("Arial,30"),padx=10).grid(row=0,column=2)
    heading=tk.Label(q,text="Designation",bg="Black",fg="White",font=("Arial,30"),padx=10).grid(row=0,column=3)
    heading=tk.Label(q,text="DOB",bg="Black",fg="White",font=("Arial,30"),padx=10).grid(row=0,column=4)
    for x in Employee:
        label=tk.Label(q,text=x,font=("Arial",30),bg="Black",fg="white").grid(row=k,column=l)
        l+=1
        for a in Employee[x]:
            label=tk.Label(q,text=a,font=("Arial",30),bg="Black",fg="White").grid(row=k,column=l)
            l+=1
        l=1
        k+=1

def delete_window():
    d=tk.Toplevel(main)
    d.geometry("400x100")
    label=tk.Label(d,text="Enter the Employee ID to delete").pack()
    entry=tk.Entry(d,textvariable=search_ele).pack()
    submit=tk.Button(d,command=lambda:delete(),text="Delete").pack()

def save_file():
    with open ("savefile.json","w") as file:
        json.dump(Employee,file)
        messagebox.showinfo(message="File successfully Saved!",title="Save Window")
def load_file():
    global Employee
    try:
        with open("savefile.json","r") as file:
            try:
                Employee=json.load(file)
                messagebox.showinfo(message="File successfully Loaded!",title="Load Window")
            except SyntaxError:
                messagebox.showerror(message="File was unable to be loaded!")
    except FileNotFoundError:
        messagebox.showerror(message="Save file was unable to be found")
        
button=tk.Button(main,command=lambda:create_window(),text="Create Employee",pady=20).grid(row=0,column=0)
button=tk.Button(main,command=lambda:search_window(),text="Search Employee",pady=20).grid(row=1,column=0)
button=tk.Button(main,command=lambda:delete_window(),text="Delete Employee",pady=20).grid(row=2,column=0)
button=tk.Button(main,command=lambda:display_employee(),text="Display Employee",pady=20).grid(row=3,column=0)
button=tk.Button(main,command=lambda:save_file(),text="Save",pady=20).grid(row=4,column=0)
button=tk.Button(main,command=lambda:load_file(),text="Load",pady=20).grid(row=5,column=0)
main.mainloop()
