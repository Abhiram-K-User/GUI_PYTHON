#Project by Abhiram.K!
import tkinter as tk
import requests
import html
import random
api_string="https://opentdb.com/api.php?amount=10&category=15&difficulty=easy&type=multiple"
win=tk.Tk()
i=score=j=0
curr_answer=""
m1=tk.StringVar()
time=tk.IntVar()
q_no=tk.IntVar()
time.set(100)
choice1=tk.StringVar()
choice2=tk.StringVar()
choice3=tk.StringVar()
choice4=tk.StringVar()

print("Welcome to my Program!")
response=requests.get(api_string)
a=response.json()
b=a['results']
def question_Finder():
    questions=[]
    if(response.status_code==200):
        for i in range(0,len(b)):
            c=b[i]
            q=html.unescape(c['question']) #Used for the conversion of the ASCII characters to a HTML format in order to account for special characters
            questions.append(q) 
        return questions
    else:
        return None

def choice_finder(x):
    c=b[x]['incorrect_answers']
    c.append(b[x]['correct_answer'])
    c=html.unescape(c)
    return c

def timer():
    if(time.get()>0):
        x=time.get()
        time.set(x-1)
        win.after(1000,timer)

def ui_updater(questions,num):
    try:
        global i
        m1.set(questions[i])
        question=tk.Label(win,textvariable=m1,font=("Calibri",20))
        question.grid(row=0,column=0)
        c=choice_finder(i)
        i=i+num
        corr_answer=c[3]
        random.shuffle(c)
        choice1.set(c[0])
        button1=tk.Button(win,textvariable=choice1,command=lambda:question_analyze(choice1.get(),corr_answer)).grid(row=1,column=0)
        choice2.set(c[1])
        button2=tk.Button(win,textvariable=choice2,command=lambda:question_analyze(choice2.get(),corr_answer)).grid(row=2,column=0)
        choice3.set(c[2])
        button3=tk.Button(win,textvariable=choice3,command=lambda:question_analyze(choice3.get(),corr_answer)).grid(row=3,column=0)
        choice4.set(c[3])
        button4=tk.Button(win,textvariable=choice4,command=lambda:question_analyze(choice4.get(),corr_answer)).grid(row=4,column=0)
    except IndexError:
        win.destroy()
        print(f"""QUIZ ANALYSIS
        Number of Questions: 10
        Score obtained:{score}
Time remaining:{time.get()} seconds""")

def question_analyze(given_ans,corr_ans):
    global score
    global curr_answer
    if(given_ans==corr_ans and curr_answer!=given_ans):
        curr_answer=given_ans
        score+=1

v=question_Finder() 
m1.set(v[0])
win.title("MY Quiz App")
win.state("zoomed")
next_button=tk.Button(win,text="Next",command=lambda: ui_updater(v,1)).place(x=200,y=200)
prev_button=tk.Button(win,text="Previous",command=lambda: ui_updater(v,-1)).place(x=250,y=200)
a=tk.Label(win,text="Time:",font=("Arial",15)).grid(row=0,column=1)
time_remaining=tk.Label(win,textvariable=time,font=("Arial",15)).grid(row=0,column=2)
timer()
win.mainloop()

