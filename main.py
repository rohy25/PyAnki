from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import json
import time
from tkinter.scrolledtext import ScrolledText

MyDict = {}
varstop = 0
Display_list = []
MyDick_Val = []

class StudyTop(tk.Toplevel):

    def get_var(self):
        global varstop
        return varstop

    def set_var(self, val):
        global varstop
        varstop = val

    def clear(self):
        list = self.pack_slaves()
        for l in list:
            l.destroy()

    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Study")
        self.geometry("300x400")

        self.set_var(0)
        self.QueryWord()

    def WaitFlag(self):
        while True:
            varstop = self.get_var()
            print(varstop)
            if varstop == 1:
                self.set_var(0)
                break
            else:
                time.sleep(1)

    def AnswerWord(self):
        self.clear()

        study_front = ttk.Label(self, text="")
        k = Display_list[self.get_var()]
        study_front.config(text=k)
        study_front.pack(side=tk.TOP, pady=10)

        sep1 = ttk.Separator(self, orient="horizontal")
        sep1.pack(fill="both")

        study_back = ttk.Label(self, text="")
        study_back.config(text=root.MyDict[k])
        study_back.pack(side=tk.TOP, pady=20)


        self.buttonframe = tk.Frame(self)
        self.buttonframe.pack(fill=tk.X, anchor=tk.N)
        #button_confirm1 = ttk.Button(self, text="5dyas", command=self.QueryWord)
        #button_confirm1.pack()
        self.option_add("*Font", "Arial 12")
        button_confirm1 = tk.Button(self.buttonframe, width=7, text="10min", fg="white", bg="red", command=self.QueryWord)
        button_confirm1.pack(side=tk.LEFT, padx=2, pady=100)
        button_confirm2 = tk.Button(self.buttonframe, width=7, text="8days", fg="white", bg="black", command=self.QueryWord)
        button_confirm2.pack(side=tk.LEFT, padx=2, pady=100)
        button_confirm3 = tk.Button(self.buttonframe, width=7, text="18days", fg="white", bg="green", command=self.QueryWord)
        button_confirm3.pack(side=tk.LEFT, padx=2, pady=100)
        button_confirm4 = tk.Button(self.buttonframe, width=7, text="26days", fg="white", bg="blue", command=self.QueryWord)
        button_confirm4.pack(side=tk.LEFT, padx=2, pady=100)

        self.set_var(self.get_var()+1)

    def QueryWord(self):
        self.clear()
        self.option_add("*Font", "Arial 12")
        study_front = tk.Label(self, text="")

        try:
            k = Display_list[self.get_var()]
        except IndexError:
            study_front.config(text="Congrats! Study done today!!!", fg="blue")
            study_front.pack(side=tk.TOP, pady=50)
            return

        study_front.config(text=k)
        study_front.pack(side=tk.TOP, pady=10)

        sep1 = ttk.Separator(self, orient="horizontal")
        sep1.pack(fill="both")

        #button_confirm1 = ttk.Button(self, text="Check answer", command=self.AnswerWord)
        #button_confirm1.pack()
        button_confirm1 = tk.Button(self, width=10, text="answer", fg="white", bg="red", command=self.AnswerWord)
        button_confirm1.pack(side=tk.TOP, pady=100)

class AddTop(tk.Toplevel):

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.SaveWord()
            self.destroy()

    def __init__(self):
        tk.Toplevel.__init__(self)
        self.title("Add New Words")
        self.geometry("300x400")
        self.protocol("WM_DELETE_WINDOW", self.on_closing)

        self.addframe = tk.Frame(self)
        self.addframe.pack(fill=tk.X, anchor=tk.N)
        self.option_add("*Font", "Arial 12")
        tk.Label(self.addframe, text="Front", fg="blue").pack(side=tk.TOP, padx=1, pady=1)
        #self.textFront = tk.Entry(self.addframe, width=40, textvariable=str)
        self.textFront = tk.Text(self.addframe, height=2)
        self.textFront.pack(expand=tk.YES, fill=tk.BOTH, side=tk.TOP, padx=10, pady=2)
        #self.textFront.pack(side=tk.TOP, padx=10, pady=2)
        tk.Label(self.addframe, text="Back", fg="red").pack(side=tk.TOP, padx=1, pady=1)
        self.textBack = tk.Text(self.addframe, height=5)
        self.textBack.pack(expand=tk.YES, fill=tk.BOTH, side=tk.TOP, padx=10, pady=2)
        #self.textBack = tk.Entry(self.addframe, width=40, textvariable=str)
        #self.textBack.pack(side=tk.TOP, padx=10, pady=2)
        button = tk.Button(self, width=10, text="Add", fg="white", bg="red", command=self.AddWord)
        button.pack(side=tk.TOP, padx=10, pady=80)

        #button2 = ttk.Button(self, text="Save", command=self.SaveWord)
        #button2.pack()
    def clear_text(self):
        self.textFront.delete(1.0, tk.END)
        self.textBack.delete(1.0, tk.END)
        self.textFront.focus()

    def AddWord(self):
        if len(self.textBack.get(1.0, "end-1c")) == 0:
            print("Empty back")
            messagebox.showinfo("Back is empty.")
        else:
            #add here value info MyDick_Val
            root.MyDict[self.textFront.get(1.0, "end-1c")] = self.textBack.get(1.0, "end-1c")
            print(root.MyDict)
            self.clear_text()

    def SaveWord(self):
        f = open('Mypyanki', 'w')
        json.dump(root.MyDict, f)
        f.close()

def root_clear():
    list = root.pack_slaves()
    for l in list:
        l.destroy()

def RefreshTop():
    root_clear()
    root_label = ttk.Label(root, text="")
    root_disp = [0, 0, 0, 0]

    while True:
        try:
            f = open('Mypyanki', 'r')
            root.MyDict = json.load(f)
            root_disp[3] = len(root.MyDict)
            root_label.config(text=root_disp)
            root_label.pack()
            f.close()
            break
        except FileNotFoundError:
            break

def center_window(w, h):
    # get screen width and height
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    # calculate position x, y
    x = (ws/2) - (w/2)
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))

root = tk.Tk()
#root.geometry("300x400")
center_window(300, 400)
root.title('연재의 단어장')
root.resizable(False, False)
root.option_add("*Font","Arial 14")

menubar = tk.Menu(root)
menu1 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = "File", menu=menu1)
menu2 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Study", menu=menu2)
menu3 = tk.Menu(menubar, tearoff=0)
menubar.add_cascade(label = "Add New Words", menu=menu3)

menu1.add_command(label="Exit")
menu1.add_command(label="Refresh", command=RefreshTop)
menu2.add_command(label="Start", command=StudyTop)
menu3.add_command(label="Add", command=AddTop)
root.config(menu=menubar)#윈도창에 메뉴등록

RefreshTop()
Display_list = list(root.MyDict)
print(Display_list)

root.mainloop() #hahaha