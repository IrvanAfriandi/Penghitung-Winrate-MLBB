from tkinter import *
import tkinter as tk
from PIL import Image, ImageTk
from tkinter import Frame,Label,Entry,Button,Radiobutton,ttk,VERTICAL,YES,BOTH,END,Tk,W,StringVar,messagebox

class FirstPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.background()
        Button = tk.Button(self, text="Masuk", font=("Arial", 25), borderwidth=4,command=lambda: controller.show_frame(SecondPage))
        Button.place(x=200, y=300)

    def background(self):
        image = Image.open("BGMain.png")
        image = image.resize((747, 447))
        photo = ImageTk.PhotoImage(image)
        label = Label(self, image=photo)
        label.pack(side=LEFT, anchor=NW)
        label.image = photo
        label.pack()
    

class SecondPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='white')
        self.background()
        self.InputData()
    def InputData(self):
        Label0 = Label(self, background='#800000', width=52, height=20, borderwidth=4, relief=RIDGE)
        Label0.place(x=360, y=40)
        Label1 = Label(self, text='Masukkan Data',
                       background='#800000', 
                       fg='white', 
                       font=('Times_New_Roman',15))
        Label1.place(x=480, y=55)
        Label2 = Label(self, text='Total Match',
                       background='#800000', 
                       fg='white', 
                       font=('Times_New_Roman',15))
        Label2.place(x=375, y=120)
        Label3 = Label(self, text='Win Rates',
                       background='#800000', 
                       fg='white', 
                       font=('Times_New_Roman',15))
        Label3.place(x=375, y=170)
        Label4 = Label(self, text='Target Win Rates',
                       background='#800000', 
                       fg='white', 
                       font=('Times_New_Roman',15))
        Label4.place(x=375, y=220)
        Persen = Label(self, text='%',
                       background='#800000', 
                       fg='white', 
                       font=('Times_New_Roman',15))
        Persen.place(x=655, y=170)
        Persen1 = Label(self, text='%',
                        background='#800000', 
                        fg='white', 
                        font=('Times_New_Roman',15))
        Persen1.place(x=655, y=220)

        self.txtTMatch = Entry(self, font=('bold',10), borderwidth=2) 
        self.txtTMatch.place(x=560, y=120, width=150)
        self.txtTMatch.focus_set() 
        self.txtTMatch.bind("<Return>",self.Enter1)
        
        self.txtWinrate = Entry(self, font=('bold',10), borderwidth=2) 
        self.txtWinrate.place(x=560, y=170, width=90)
        self.txtWinrate.bind("<Return>",self.Enter2)
        self.txtTargetWinrate = Entry(self, font=('bold',10), borderwidth=2) 
        self.txtTargetWinrate.place(x=560, y=220, width=90)
        self.txtTargetWinrate.bind("<Return>",self.Enter3)

        Button = tk.Button(self, text="Hitung", font=("Arial", 15), command=self.Enter3)
        Button.place(x=515, y=290)

    def OutputData(self, event=None):
        TMatch = str(self.txtTMatch.get())
        TMatch = int(TMatch)
        
        TWinrate = str(self.txtWinrate.get())
        Wr = TWinrate.replace(",", ".")
        Wr = float(Wr)
        TWr = str(self.txtTargetWinrate.get())
        TargetWinRate = TWr.replace(",", ".")
        TargetWinRate = float(TargetWinRate)
        messagebox.showinfo("Mohon Bersabar", "Data Sedang Diproses")

        Label01 = Label(self, background='#800000', 
                        width=52, 
                        height=20, 
                        borderwidth=4, 
                        relief=RIDGE)
        Label01.place(x=360, y=40)
        Label11 = Label(self, text='Dengan Total Match',
                        background='#800000', 
                        fg='white', 
                        font=('Times_New_Roman',14))
        Label11.place(x=370, y=55)
        Label111 = Label(self, text='dan juga Winrate\t             %',
                        background='#800000', 
                        fg='white', 
                        font=('Times_New_Roman',14))
        Label111.place(x=370, y=90)
        Label12 = Label(self, text='Anda Telah Menang Sebanyak\t             X',
                        background='#800000', 
                        fg='white', 
                        font=('Times_New_Roman',14))
        Label12.place(x=375, y=135)
        Label13 = Label(self, text='Dan Telah Kalah Sebanyak\t             X',
                        background='#800000', 
                        fg='white', 
                        font=('Times_New_Roman',14))
        Label13.place(x=375, y=170)
        Label14 = Label(self, text='Untuk Mencapai Winrate\t  %',
                        background='#800000', 
                        fg='white', 
                        font=('Times_New_Roman',14))
        Label14.place(x=375, y=220)
        Label15 = Label(self, text='Anda Harus Memenangkan Pertandingan',
                        background='#800000', 
                        fg='white', 
                        font=('Times_New_Roman',14))
        Label15.place(x=375, y=250)
        Label16 = Label(self, text='Sebanyak\t\tPertandingan Tanpa',
                        background='#800000', 
                        fg='white', 
                        font=('Times_New_Roman',14))
        Label16.place(x=375, y=280)
        Label17 = Label(self, text='Kalah sama sekali.',
                        background='#800000', 
                        fg='white', 
                        font=('Times_New_Roman',14))
        Label17.place(x=375, y=310)


        self.txtShowMatch = Entry(self, background='#800000', fg='white', font=('Times_New_Roman',14))
        self.txtShowMatch.place(x=555, y=57, width=73)
        self.txtShowWinrate = Entry(self, background='#800000', fg='white', font=('Times_New_Roman',14))
        self.txtShowWinrate.place(x=555, y=93, width=50)
        self.txtShowWin = Entry(self, background='#800000', fg='white', font=('Times_New_Roman',14))
        self.txtShowWin.place(x=640, y=138, width=53)
        self.txtShowLose = Entry(self, background='#800000', fg='white', font=('Times_New_Roman',14))
        self.txtShowLose.place(x=640, y=173, width=53)
        self.txtShowTWr = Entry(self, background='#800000', fg='white', font=('Times_New_Roman',14))
        self.txtShowTWr.place(x=590, y=223, width=53)
        self.txtShowTMatch = Entry(self, background='#800000', fg='white', font=('Times_New_Roman',14))
        self.txtShowTMatch.place(x=470, y=283, width=73)

        Button = tk.Button(self, text="Reset", font=("Arial", 10), command=self.InputData)
        Button.place(x=680, y=315)

        

        TotalWin =  self.Win(TMatch, Wr)
        TotalLose = self.Lose(TMatch, Wr)
        TargetWR = self.TargetWR(TMatch, Wr, TargetWinRate)

     
        self.txtShowMatch.insert(END,str(TMatch))
        self.txtShowWinrate.insert(END,str(TWinrate))
        self.txtShowWin.insert(END,str(TotalWin))
        self.txtShowLose.insert(END,str(TotalLose))
        self.txtShowTWr.insert(END,str(TWr))
        self.txtShowTMatch.insert(END,str(TargetWR))
        messagebox.showinfo("Horeee", "Data Berhasil Dihitung")

    def Win(self, TMatch, Wr):
        TotalMenang = TMatch * Wr/100
        TotalMenang = int(TotalMenang)
        return TotalMenang
    def Lose(self, TMatch, Wr):
        TotalMenang = TMatch * Wr/100
        TotalMenang = int(TotalMenang)
        TotalKalah = TMatch - TotalMenang
        return TotalKalah
    def TargetWR(self, TMatch, Wr, TargetWinRate):
        tWin = TMatch * (Wr / 100)
        tLose = TMatch - tWin
        sisaWr = 100 - TargetWinRate
        wrResult = 100 / sisaWr
        seratusPersen = tLose * wrResult
        final = seratusPersen - TMatch
        final = int(final)
        return final
        
    def background(self):
        image = Image.open("BGMain2.png")
        image = image.resize((747, 445))
        photo = ImageTk.PhotoImage(image)
        label = Label(self, image=photo)
        label.pack(side=LEFT, anchor=NW)
        label.image = photo
        label.pack()

    def Enter1(self, event=None):
        a = str(self.txtTMatch.get())
        if (a==''):
            messagebox.showinfo("Pemberitahuan", "Mohon Lengkapi datanya dulu")
            self.txtTMatch.focus_set()
        else:
            self.txtWinrate.focus_set() 
    def Enter2(self, event=None):
        b = str(self.txtWinrate.get())
        if (b==''):
            messagebox.showinfo("Pemberitahuan", "Mohon Lengkapi datanya dulu")
            self.txtWinrate.focus_set() 
        wr = b.replace(",", ".")
        Wr = float(wr)
        if (Wr>=100):
            messagebox.showinfo("Pemberitahuan", "Winrate tidak bisa melebihi 100%")
            self.txtWinrate.focus_set() 
        else:
            self.txtTargetWinrate.focus_set() 
    def Enter3(self, event=None):
        c = str(self.txtTargetWinrate.get())
        if (c==''):
            messagebox.showinfo("Pemberitahuan", "Mohon Lengkapi datanya dulu")
            self.txtTargetWinrate.focus_set()
        d = c.replace(",", ".")
        d = float(d)
        if (d>=100):
            messagebox.showinfo("Pemberitahuan", "Mau sampai kiamat juga gak bisa bro :)")
            self.txtTargetWinrate.focus_set()
        else:
            self.OutputData()

class ThirdPage(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.configure(bg='Tomato')

        Button = tk.Button(self, text="Home", font=("Arial", 15), command=lambda: controller.show_frame(FirstPage))
        Button.place(x=650, y=350)

        Button = tk.Button(self, text="Back", font=("Arial", 15), command=lambda: controller.show_frame(SecondPage))
        Button.place(x=100, y=350)


class Application(tk.Tk):
    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        # creating a window
        window = tk.Frame(self)
        window.pack()

        window.grid_rowconfigure(0, minsize=500)
        window.grid_columnconfigure(0, minsize=800)

        self.frames = {}
        for F in (FirstPage, SecondPage, ThirdPage):
            frame = F(window, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        self.show_frame(FirstPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()
        self.title("Aplikasi Penghitung Winrate Hero MLBB")


app = Application()
app.geometry("750x450+230+100")
app.mainloop()