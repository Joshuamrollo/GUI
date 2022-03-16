import tkinter
import tkinter.messagebox

class MyGUI:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('300x100')
        self.main_window.title('YO')

        self.top_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

          

        self.mybutton = tkinter.Button(self.main_window, text='Click Me!', command=self.do_something)
        self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)

        self.top_frame.pack(side='top')
        self.bottom_frame.pack(side='top')

        self.mybutton.pack(side='left')
        self.quit_button.pack(side='right')

        tkinter.mainloop()

    def do_something(self):
        tkinter.messagebox.showinfo('Response', 'Thanks for clicking the button')

my_gui = MyGUI()

print("moving on.....")