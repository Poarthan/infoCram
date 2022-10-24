#/usr/bin/env python3


import time
from math import sqrt, pow, exp
import random
import tkinter as tk
from tkinter import font as tkFont


class rip(tk.Button):
    def __init__(self, master=None, **kwargs):
        self.img = tk.PhotoImage()
        tk.Button.__init__(self, master, image=self.img, compound='center', **kwargs)

def main():
    start=time.time()
    global click, remove, usedFONT
    usedFONT='Arial'
    click=0
    remove=0
    allFalse()
    checklist=[var_match_1, var_match_2, var_match_3, var_match_4, var_match_5, var_match_6, var_match_7, var_match_8, var_match_9, var_match_10, var_match_11, var_match_12]
    studylist="studylist.txt"
    mlist=matchinglist(studylist)
    setup2=time.time()
    print("time", setup2-start, "-------------------------------------------------------------------------\n-----------------------------------------------------------------")
    match_creation(mlist)

def fontConfig(text):

    print("spaces", text.count(' '))
    print("UHHH", hh)
    arial36b = tkFont.Font(family='Arial', size=hh//4)
    width = arial36b.measure(text)
    print("width:", width)
    n=width//(ww//3)
    print("n:", n)
    print(text)
    usedSize=hh//(n*2)
    print("finalsize", usedSize)
   # lineSize=ww//3-ww//14

    return int(usedSize)

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
    varlist=[var_match_1, var_match_2, var_match_3, var_match_4, var_match_5, var_match_6, var_match_7, var_match_8, var_match_9, var_match_10, var_match_11, var_match_12]
    #print(varlist)

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

                finaltime=time.time()
                print(finaltime-setfin, "TIME TAKEN")
            buttonlist[0].config(background='gray', state='disabled')
            #buttonlist[0]["state"] = "disabled"
            #buttonlist[0].grid_remove()
            #buttonlist[0].pack(pady=10)
            buttonlist[1].config(background='gray', state='disabled')
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

                finaltime=time.time()
                print(finaltime-setfin, "TIME TAKEN")

            buttonlist[0].config(background='gray', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[1].config(background='gray', state='disabled')
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

                finaltime=time.time()
                print(finaltime-setfin, "TIME TAKEN")

            buttonlist[2].config(background='gray', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[3].config(background='gray', state='disabled')
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

                finaltime=time.time()
                print(finaltime-setfin, "TIME TAKEN")

            buttonlist[2].config(background='gray', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[3].config(background='gray', state='disabled')
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

                finaltime=time.time()
                print(finaltime-setfin, "TIME TAKEN")

            buttonlist[4].config(background='gray', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[5].config(background='gray', state='disabled')
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

                finaltime=time.time()
                print(finaltime-setfin, "TIME TAKEN")

            buttonlist[4].config(background='gray', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[5].config(background='gray', state='disabled')
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

                finaltime=time.time()
                print(finaltime-setfin, "TIME TAKEN")

            buttonlist[6].config(background='gray', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[7].config(background='gray', state='disabled')
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

                finaltime=time.time()
                print(finaltime-setfin, "TIME TAKEN")

            buttonlist[6].config(background='gray', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[7].config(background='gray', state='disabled')
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

                finaltime=time.time()
                print(finaltime-setfin, "TIME TAKEN")

            buttonlist[8].config(background='gray', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[9].config(background='gray', state='disabled')
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

                finaltime=time.time()
                print(finaltime-setfin, "TIME TAKEN")

            buttonlist[8].config(background='gray', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[9].config(background='gray', state='disabled')
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

                finaltime=time.time()
                print(finaltime-setfin, "TIME TAKEN")

            buttonlist[10].config(background='gray', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[11].config(background='gray', state='disabled')
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

                finaltime=time.time()
                print(finaltime-setfin, "TIME TAKEN")

            buttonlist[10].config(background='gray', state='disabled')
            #buttonlist[0].pack(pady=10)
            buttonlist[11].config(background='gray', state='disabled')
            click=0
        else:
            click=0
            allFalse()
            backgroundReset()

def match_creation(matchlist):
    global buttonlist, ww, hh, setfin
    setfin=0
    set1=time.time()
    wordlist=[]
    for i in range(6):
        chosen=random.randint(0,len(matchlist)-1)
        while chosen in wordlist:
            chosen=random.randint(0,len(matchlist)-1)
            if len(matchlist) < 6:
                break
        wordlist.append(chosen)
    mmm=[]
    try:
        for i in range(len(wordlist)):
            mmm.append(matchlist[wordlist[i]])
    except IndexError:
        print("ERRRRRRRRRRROOOOOOOOOOOOOOOOORR__________________________________________________________________________________-----\n--------------------------------------------------------------")
        print(len(wordlist))
        print(wordlist)
        print(matchlist)
        print(i)
    win = tk.Tk()
    screen_wid=win.winfo_screenwidth()
    screen_height=win.winfo_screenheight()
    print(screen_wid, screen_height)
    ww=screen_wid//2
    hh=screen_height-screen_height//5
    print(ww, hh, "hello")
    win.geometry(f'{ww}x{hh}')
    win.columnconfigure((0,1,2,3),weight=3)
    win.rowconfigure((0,1,2), weight=1)
    frame = tk.Frame(win)
    frame.pack()
    buttonlist=[]

    pos=[[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2],[3,0],[3,1],[3,2]]

    commandlist=[click1,click2,click3,click4,click5,click6,click7,click8,click9,click10,click11,click12]
    #def fontConfig(text, blocksize):
    #    n=340//len(text)
    #    usedSize=n-20
    #    if usedSize>100:
    #        usedSize=100
    #    print(usedSize, text, n)
    #    return usedSize

    random.shuffle(pos)
    for i in range(6):
        fontSIZE=fontConfig(mmm[i][0])
        sfonts=tkFont.Font(size=fontSIZE)
        buttonlist.append(rip(frame,  height=hh//4-hh//20,  width=ww//3-ww//15, font=sfonts, wraplength=ww//3-ww//14,  text=mmm[i][0],  fg="black",  bg='white',  command=commandlist[i*2]))
        buttonlist[i*2].grid(row=pos[i*2][0], column=pos[i*2][1])
        fontSIZE=fontConfig(mmm[i][1])
        sfonts=tkFont.Font(size=fontSIZE)

        buttonlist.append(rip(frame, height=hh//4-hh//20,  width=ww//3-ww//15, font=sfonts, wraplength=ww//3-ww//14, text=mmm[i][1], fg="black",   bg='white', command=commandlist[i*2+1]))
        buttonlist[i*2+1].grid(row=pos[i*2+1][0], column=pos[i*2+1][1])
    setfin=time.time()
    print("setupd time", setfin-set1, "------------------------------------------------------\n---------------------------------------------")
    win.mainloop()


def matchinglist(list):
    newlines=[]
    matchsplitchar="!!!!!"
    with open(f'{list}') as file:
        lines = [line.rstrip() for line in file]

    for stuff in lines:
        things=stuff.split(matchsplitchar)
        newlines.append(things)
    #print(newlines)
    return newlines #, unusual

if __name__ == "__main__":
    main()
