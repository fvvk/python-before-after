from tkinter import *
from tkinter.filedialog import askopenfilename
from tkinter.messagebox import showerror




class MyFrame(Frame):
    def __init__(self):
        Frame.__init__(self)
        self.master.title("Kontext-Sucher")
        self.master.rowconfigure(5, weight=1)
        self.master.columnconfigure(5, weight=1)
        self.grid(sticky=W+E+N+S)

        self.button1 = Button(self, text="Datei auswählen", command=self.load_file, width=15)
        self.button1.grid(row=1, column=0, sticky=W)

        self.label1 = Label(self, text="Wort eingeben: ", width=15)
        self.label1.grid(row=2, column=0, sticky=E)

        self.field_entry = Entry(self, text="Wort eingeben: ", width=40)
        self.field_entry.grid(row=2, column=1, sticky=E)

        self.button_submit = Button(self, text="Start", command=self.callback, width=15)
        self.button_submit.grid(row=3, column=0, sticky=W)

    def load_file(self):
        fname = askopenfilename(filetypes=(("Text files", "*.txt"),
                                           ("HTML files", "*.html;*.htm"),
                                           ("All files", "*.*") ))
        if fname:
            try:
                with open(fname) as f:
                    mylist = [line.rstrip('\n') for line in f]
                    string= "".join(mylist)
                    words=string.split()
                    print(words)
            except:
                showerror("Open Source File", "Failed to read file\n'%s'" % fname)
            return
        print('datei geladen')
        context(input("> "))
                                
    def context(word):
        for ind,x in enumerat(words):
                if x.strip(",'.!")==word or x.strip(',".!')==word:
                    with open('output.txt', 'a') as f:
                        print(" ".join(words[ind-8:ind]+words[ind:ind+9]), file=f)

    def callback():
        context("starte")


if __name__ == "__main__":
    MyFrame().mainloop()



