#!/usr/bin/env python3


import time
from math import sqrt, pow, exp
import random
import tkinter as tk


def main():
    global click, remove
    click=0
    remove=0
    allFalse()
    checklist=[var_match_1, var_match_2, var_match_3, var_match_4, var_match_5, var_match_6, var_match_7, var_match_8, var_match_9, var_match_10, var_match_11, var_match_12]
    studylist="studylist.txt"
    mlist=matchinglist(studylist)
    match_creation(mlist)

def allFalse():
    global var_match_1, var_match_2, var_match_3, var_match_4, var_match_5, var_match_6, var_match_7, var_match_8, var_match_9, var_match_10, var_match_11, var_match_12
    var_match_1=False
    var_match_2=False
    var_match_3=False
    var_match_4=False
    var_match_5=False
    var_match_6=False
    var_match_7=False
    var_match_8=False
    var_match_9=False
    var_match_10=False
    var_match_11=False
    var_match_12=False
def backgroundReset():
    for i in range(12):
        buttonlist[i].config(background='white')
        buttonlist[i].update()

def click1():
    global var_match_1, click, remove
    if var_match_1==True:
        var_match_1==False
        buttonlist[0].config(background='white')
        buttonlist[0].update()
    else:
        var_match_1=True
        buttonlist[0].config(background='green')
        buttonlist[0].update()

    print("one")
    click+=1
    if click ==2:
        if var_match_2==True:
            print("correct")
            remove+=1
            if remove >=6:
                print("done")
            buttonlist[0].config(background='white', state='disabled')
            #buttonlist[0]["state"] = "disabled"
            #buttonlist[0].grid_remove()
            #buttonlist[0].pack(pady=10)
            buttonlist[1].config(background='white', state='disabled')
            click=0
        else:
            click=0
            allFalse()
            backgroundReset()
def click2():
    global var_match_2, click, remove
    if var_match_2==True:
        var_match_2==False
        buttonlist[1].config(background='white')
        buttonlist[1].update()
    else:
        var_match_2=True
        buttonlist[1].config(background='green')
        buttonlist[1].update()

    print("two")
    click+=1
    if click ==2:
        if var_match_1==True:
            print("correct")
            remove+=1
            if remove >=6:
                print("done")

            buttonlist[0].config(background='white', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[1].config(background='white', state='disabled')
            click=0
        else:
            click=0
            allFalse()
            backgroundReset()
def click3():
    global var_match_3, click, remove
    if var_match_3==True:
        var_match_3==False
        buttonlist[2].config(background='white')
        buttonlist[2].update()

    else:
        var_match_3=True
        buttonlist[2].config(background='green')
        buttonlist[2].update()

    print("one")
    click+=1
    if click ==2:
        if var_match_4==True:
            print("correct")
            remove+=1
            if remove >=6:
                print("done")

            buttonlist[2].config(background='white', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[3].config(background='white', state='disabled')
            click=0
        else:
            click=0
            allFalse()
            backgroundReset()
def click4():
    global var_match_4, click, remove
    if var_match_4==True:
        var_match_4==False
        buttonlist[3].config(background='white')
        buttonlist[3].update()
    else:
        var_match_4=True
        buttonlist[3].config(background='green')
        buttonlist[3].update()

    print("two")
    click+=1
    if click ==2:
        if var_match_3==True:
            print("correct")
            remove+=1
            if remove >=6:
                print("done")

            buttonlist[2].config(background='white', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[3].config(background='white', state='disabled')
            click=0
        else:
            click=0
            allFalse()
            backgroundReset()
def click5():
    global var_match_5, click, remove
    if var_match_5==True:
        var_match_5==False
        buttonlist[4].config(background='white')
        buttonlist[4].update()
    else:
        var_match_5=True
        buttonlist[4].config(background='green')
        buttonlist[4].update()
    print("one")
    click+=1
    if click ==2:
        if var_match_6==True:
            print("correct")
            remove+=1
            if remove >=6:
                print("done")

            buttonlist[4].config(background='white', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[5].config(background='white', state='disabled')
            click=0
        else:
            click=0
            allFalse()
            backgroundReset()
def click6():
    global var_match_6, click, remove
    if var_match_6==True:
        var_match_6==False
        buttonlist[5].config(background='white')
        buttonlist[5].update()
    else:
        var_match_6=True
        buttonlist[5].config(background='green')
        buttonlist[5].update()
    print("two")
    click+=1
    if click ==2:
        if var_match_5==True:
            print("correct")
            remove+=1
            if remove >=6:
                print("done")

            buttonlist[4].config(background='white', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[5].config(background='white', state='disabled')
            click=0
        else:
            click=0
            allFalse()
            backgroundReset()
def click7():
    global var_match_7, click, remove
    if var_match_7==True:
        var_match_7==False
        buttonlist[6].config(background='white')
        buttonlist[6].update()
    else:
        var_match_7=True
        buttonlist[6].config(background='green')
        buttonlist[6].update()
    print("one")
    click+=1
    if click ==2:
        if var_match_8==True:
            print("correct")
            remove+=1
            if remove >=6:
                print("done")

            buttonlist[6].config(background='white', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[7].config(background='white', state='disabled')
            click=0
        else:
            click=0
            allFalse()
            backgroundReset()
def click8():
    global var_match_8, click, remove
    if var_match_8==True:
        var_match_8==False
        buttonlist[7].config(background='white')
        buttonlist[7].update()
    else:
        var_match_8=True
        buttonlist[7].config(background='green')
        buttonlist[7].update()
    print("two")
    click+=1
    if click ==2:
        if var_match_7==True:
            print("correct")
            remove+=1
            if remove >=6:
                print("done")

            buttonlist[6].config(background='white', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[7].config(background='white', state='disabled')
            click=0
        else:
            click=0
            allFalse()
            backgroundReset()
def click9():
    global var_match_9, click, remove
    if var_match_9==True:
        var_match_9==False
        buttonlist[8].config(background='white')
        buttonlist[8].update()
    else:
        var_match_9=True
        buttonlist[8].config(background='green')
        buttonlist[8].update()
    print("one")
    click+=1
    if click ==2:
        if var_match_10==True:
            print("correct")
            remove+=1
            if remove >=6:
                print("done")

            buttonlist[8].config(background='white', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[9].config(background='white', state='disabled')
            click=0
        else:
            click=0
            allFalse()
            backgroundReset()
def click10():
    global var_match_10, click, remove
    if var_match_10==True:
        var_match_10==False
        buttonlist[9].config(background='white')
        buttonlist[9].update()
    else:
        var_match_10=True
        buttonlist[9].config(background='green')
        buttonlist[9].update()
    print("two")
    click+=1
    if click ==2:
        if var_match_9==True:
            print("correct")
            remove+=1
            if remove >=6:
                print("done")

            buttonlist[8].config(background='white', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[9].config(background='white', state='disabled')
            click=0
        else:
            click=0
            allFalse()
            backgroundReset()
def click11():
    global var_match_11, click, remove
    if var_match_11==True:
        var_match_11==False
        buttonlist[10].config(background='white')
        buttonlist[10].update()
    else:
        var_match_11=True
        buttonlist[10].config(background='green')
        buttonlist[10].update()
    print("one")
    click+=1
    if click ==2:
        if var_match_12==True:
            print("correct")
            remove+=1
            if remove >=6:
                print("done")

            buttonlist[10].config(background='white', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[11].config(background='white', state='disabled')
            click=0
        else:
            click=0
            allFalse()
            backgroundReset()
def click12():
    global var_match_12, click, remove
    if var_match_12==True:
        var_match_12==False
        buttonlist[11].config(background='white')
        buttonlist[11].update()
    else:
        var_match_12=True
        buttonlist[11].config(background='green')
        buttonlist[11].update()
    print("two")
    click+=1
    if click ==2:
        if var_match_11==True:
            print("correct")
            remove+=1
            if remove >=6:
                print("done")

            buttonlist[10].config(background='white', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[11].config(background='white', state='disabled')
            click=0
        else:
            click=0
            allFalse()
            backgroundReset()

def match_creation(matchlist):
    global blist, buttonlist

    wordlist=[]
    for i in range(6):
        chosen=random.randint(0,len(matchlist))
        while chosen in wordlist:
            chosen=random.randint(0,len(matchlist))
            if len(matchlist) < 6:
                break
        wordlist.append(chosen)
    mmm=[]
    for i in range(len(wordlist)):
        mmm.append(matchlist[wordlist[i]])
    win = tk.Tk()
    win.geometry('1200x900')
    win.columnconfigure((0,1,2,3),weight=3)
    win.rowconfigure((0,1,2), weight=1)
    frame = tk.Frame(win)
    frame.pack()
    buttonlist=[]
    blist=[]
    blist.append(mmm[0][0])
    pos=[[0,0],[0,1],[0,2],[0,3],[1,0],[1,1],[1,2],[1,3],[2,0],[2,1],[2,2],[2,3]]
    random.shuffle(pos)
    print(pos)
    buttonlist.append(tk.Button(frame,
                       height=10,
                       width=30,
                       text=mmm[0][0],
                       fg="black",
                       bg='white',
                       command= click1))
    buttonlist[0].grid(row=pos[0][0], column=pos[0][1])
    blist.append(mmm[0][1])
    buttonlist.append(tk.Button(frame,
                   height=10,
                   width=30,
                   text=mmm[0][1],
                   fg="black",
                        bg='white',
                   command=click2))
    buttonlist[1].grid(row=pos[1][0], column=pos[1][1])
    buttonlist.append(tk.Button(frame,
                       height=10,
                       width=30,
                       text=mmm[1][0],
                       fg="black",
                        bg='white',
                       command= click3))
    buttonlist[2].grid(row=pos[2][0], column=pos[2][1])
    blist.append(mmm[1][1])
    buttonlist.append(tk.Button(frame,
                   height=10,
                   width=30,
                   text=mmm[1][1],
                   fg="black",
                        bg='white',
                   command=click4))
    buttonlist[3].grid(row=pos[3][0], column=pos[3][1])
    buttonlist.append(tk.Button(frame,
                       height=10,
                       width=30,
                       text=mmm[2][0],
                       fg="black",
                        bg='white',
                       command= click5))
    buttonlist[4].grid(row=pos[4][0], column=pos[4][1])
    blist.append(mmm[2][1])
    buttonlist.append(tk.Button(frame,
                   height=10,
                   width=30,
                   text=mmm[2][1],
                   fg="black",
                        bg='white',
                   command=click6))
    buttonlist[5].grid(row=pos[5][0], column=pos[5][1])
    buttonlist.append(tk.Button(frame,
                       height=10,
                       width=30,
                       text=mmm[3][0],
                       fg="black",
                        bg='white',
                       command= click7))
    buttonlist[6].grid(row=pos[6][0], column=pos[6][1])
    blist.append(mmm[3][1])
    buttonlist.append(tk.Button(frame,
                   height=10,
                   width=30,
                   text=mmm[3][1],
                   fg="black",
                   bg='white',
                   command=click8))
    buttonlist[7].grid(row=pos[7][0], column=pos[7][1])
    buttonlist.append(tk.Button(frame,
                       height=10,
                       width=30,
                       text=mmm[4][0],
                       fg="black",
                       bg='white',
                       command= click9))
    buttonlist[8].grid(row=pos[8][0], column=pos[8][1])
    blist.append(mmm[4][1])
    buttonlist.append(tk.Button(frame,
                   height=10,
                   width=30,
                   text=mmm[4][1],
                   fg="black",
                   bg='white',
                   command=click10))
    buttonlist[9].grid(row=pos[9][0], column=pos[9][1])
    buttonlist.append(tk.Button(frame,
                       height=10,
                       width=30,
                       text=mmm[5][0],
                       fg="black",
                       bg='white',
                       command= click11))
    buttonlist[10].grid(row=pos[10][0], column=pos[10][1])
    blist.append(mmm[5][1])
    buttonlist.append(tk.Button(frame,
                   height=10,
                   width=30,
                   text=mmm[5][1],
                   fg="black",
                   bg='white',
                   command=click12))
    buttonlist[11].grid(row=pos[11][0], column=pos[11][1])
    randomlist=[[0,0], [0,100],[0,200],[0,300]]
    #for i in range(len(randomlist)):
    #    buttonlist[i].place(x=randomlist[i][0], y=randomlist[i][1])
    #    ba1=
    #    bb=
    #    bb1=
    #    bc=
    #    bc1=
    #    bd=
    #    bd1=
    #    be=
    #    be1=
    #    bf=
    #    bf1=

    win.mainloop()


def matchinglist(list):
    newlines=[]
    matchsplitchar="!!!!!"
    with open(f'{list}') as file:
        lines = [line.rstrip() for line in file]

    for stuff in lines:
        things=stuff.split(matchsplitchar)
        newlines.append(things)
    print(newlines)
    return newlines #, unusual

if __name__ == "__main__":
    main()


