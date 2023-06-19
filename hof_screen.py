from tkinter import *

file = open("hof.txt")
data = file.read()
file.close()

class SplashScreen(Frame):
    def __init__(self, master=None, width=1.0, height=1.0, useFactor=True):
        Frame.__init__(self, master)
        self.pack(side=TOP, fill=BOTH, expand=YES)

        # get screen width and height
        ws = self.master.winfo_screenwidth()
        hs = self.master.winfo_screenheight()
        w = (useFactor and ws*width) or width
        h = (useFactor and ws*height) or height
        # calculate position x, y
        x = (ws/2) - (w/2) 
        y = (hs/2) - (h/2)
        self.master.geometry('%dx%d+%d+%d' % (w, h, x, y))
        
        self.master.overrideredirect(True)
        self.lift()

if __name__ == '__main__':
    root = Tk()

    sp = SplashScreen(root)
    sp.config(bg="violet")

    m = Label(sp, text=data)
    
    
    m.pack(side=TOP, expand=YES)
    m.config(bg="violet",justify=CENTER, font=("calibri", 24))

    root.after(5000, root.destroy)
    root.mainloop()
    
