import tkinter as tk
from tkinter import messagebox
import random

root=tk.Tk()
root.title("FOCUS APP")
root.geometry("500x500")
root.configure(bg="#1e1e1e")

label=tk.Label(root,text="FOCUS MODE",font=("Segoe UI",18,"bold"),fg="white",bg="#1e1e1e")
label.pack(pady=20)

tk.Label(root,text="Enter study time(min)",fg="#cccccc",bg="#1e1e1e",font=("Segoe UI", 11)).pack()

time_entry=tk.Entry(root,bg="#757575",fg="white",font=("Segoe UI",12),width=20)
time_entry.pack(pady=10)

status=tk.Label(root,text="",bg="#7E00AF",fg="white",font=("Segoe UI",12))
status.pack()

remain=tk.Label(root,text="",bg="#1e1e1e",fg="white",  font=("Segoe UI",16,"bold"))
remain.pack(pady=10)

message=[    "Stay focused 🔥",
    "Keep going 💪",
    "No distractions 😤",
    "You got this 🚀"]
def show_msg():
    if running and not on_break:
        msg=random.choice(message)
        status.config(text=msg)
    root.after(5000,show_msg)

time_left=0
running=False

on_break=False
break_time=10

total_time=0

active=False

def countdown():
    global time_left,running,on_break
    if running and not on_break:
        if time_left==5:
            extra=messagebox.askyesno("Need more Time?")
            if extra:
                time_left+=10
        if time_left>0:
            remain.config(text=f"time left:{time_left}")
            time_left-=1
            root.after(1000,countdown)
        elif time_left==0:
            status.config(text="session finished")
            running=False

            studied=max(0,total_time - time_left)
            remain.config(text=f"Studied:{studied}sec")

def start():
   
    global time_left,running,total_time,active

    if running:
        conform=messagebox.askyesno("The timer is running  do you want restart?")
        if not conform:
            return
    if time_left>0 and not running:
        conform=messagebox.askyesno("Already in paused Do u wanna restart?")
        if not conform:
            return

    try:
        total_time=int(time_entry.get())
        time_left=total_time
        running=True
        active=True
        status.config(text="Session Started")
        countdown()
    except:
        status.config(text="enter valid number")

def pause():
    global running,time_left,on_break
    if on_break:
        status.config(text="Already on Break")
        return
    if time_left==0:
        status.config(text="Start the session first")
        return
    if not running:
        status.config(text="Already paused")
        return
    running=False
    status.config(text="Paused")
Pbtn=tk.Button(root,text="paused",command=pause,bg="orange",fg="white")
Pbtn.pack(pady=5)

def resume():
    global running ,on_break,time_left,active

    if not active:
        status.config(text="Session already Finished")
        return  
    if time_left == 0:
        status.config(text="start the session first")
        return
    if running:
        status.config(text="the session is already running")
        return
    if on_break:
        status.config(text="Finish Break First")
        return
    running=True
    status.config(text="Resumed")
    countdown()
Rbtn=tk.Button(root,text="Resume",command=resume,bg="green",fg="white")
Rbtn.pack(pady=5)


def take_break():
    global running,on_break,break_time,time_left

    if on_break:
        status.config(text="you already on break in the session ")
        return
    if time_left==0:
        status.config(text="Start the session first")
        return
    if not running:
        status.config(text="can't take break during pause ")
        return
   
    running=False
    on_break=True
    break_time=10
    status.config(text="On Break ☕")
    break_countdown()

def break_countdown():
    global on_break,break_time,running
    if break_time > 0:
        remain.config(text=f"Break Time:{break_time}")
        break_time-=1
        root.after(1000,break_countdown)
    else:
        on_break=False
        status.config(text="Break Finished")
        running=True
        countdown()

def finish_early():
    global running,active
    
    if not running:
        status.config(text="No active Session")
        return
    running=False
    active=False
    status.config(text="Finished Early")

    studied=max(0,total_time - time_left)
    remaining=time_left
    remain.config(text=f"Finished Early\n Studied time:{studied}sec\nRemaining time:{remaining}sec")



Bbtn=tk.Button(root,text="Break",command=take_break,bg="#ff9f1c",fg="white")
Bbtn.pack(pady=5)

Sbtn=tk.Button(root,text="Start",command=start,bg="#3a86ff",fg="white",font=("Segoe UI", 11, "bold"), padx=20,pady=8)
Sbtn.pack(pady=20)

tk.Button(root,text="Finish Early",command=finish_early,bg="red",fg="white").pack(pady=5)

show_msg()
root.mainloop()