import tkinter as tk
from tkinter import filedialog,PhotoImage,Frame,Button,Menu
import pygame
import os


screen = tk.Tk()
screen.title("Audio Media Player")
screen.geometry("500x300")

pygame.mixer.init()

menubar = Menu(screen)
screen.config(menu=menubar)

songs = []
current_song = ""
paused = False

def load_music():
    global current_song
    screen.directory = filedialog.askdirectory()

    for song in os.listdir(screen.directory):
        _,ext = os.path.splitext(song)

        if ext == ".mp3":
            songs.append(song)

    for song in songs:
        songlist.insert("end",song)

    songlist.selection_set(0)

    current_song = songs[songlist.curselection()[0]]

def play_music():
    global current_song,paused
    if not paused:
        pygame.mixer.music.load(os.path.join(screen.directory,current_song))
        pygame.mixer.music.play()
    
    else:
        pygame.mixer.music.unpause()
        paused = False

def pause_music():
    global current_song,paused
    pygame.mixer.music.pause()
    paused = True

def next_music():
    global current_song,paused
    try:
        songlist.selection_clear(0,"END")
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
        
    except:
        pass

def prev_music():
    global current_song,paused
    try:
        songlist.selection_clear(0,"END")
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass
        
    
songlist = tk.Listbox(screen,bg="black",fg="white",width=100,height=15)

organise_menu = Menu(menubar,tearoff=False)
organise_menu.add_command(label="Select Music Folder",command=load_music)
menubar.add_cascade(label="Organize",menu=organise_menu)



songlist.pack()

play_btn_image = PhotoImage(file="play.png")

next_btn_image = PhotoImage(file="next.png")

previous_btn_image = PhotoImage(file="previous.png")

pause_btn_image = PhotoImage(file="pause.png")

control_frame = Frame(screen)
control_frame.pack()

play_btn = Button(control_frame,image=play_btn_image,borderwidth=0,command=play_music)

previous_btn = Button(control_frame,image=previous_btn_image,borderwidth=0,command=prev_music)

next_btn = Button(control_frame,image=next_btn_image,borderwidth=0,command=next_music)

pause_btn = Button(control_frame,image=pause_btn_image,borderwidth=0,command=pause_music)

previous_btn.grid(row=0,column=0,padx=15, pady=7)
play_btn.grid(row=0,column=1,padx=15, pady=7)
pause_btn.grid(row=0,column=2,padx=15, pady=7)
next_btn.grid(row=0,column=3,padx=15, pady=7)

screen.mainloop()

