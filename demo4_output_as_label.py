import tkinter
import tkinter.messagebox

class kilo_conv:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('300x100')
        self.main_window.title('km to miles')

        self.top_frame = tkinter.Frame(self.main_window)
        self.mid_frame = tkinter.Frame(self.main_window)
        self.bottom_frame = tkinter.Frame(self.main_window)

        self.promt_label = tkinter.Label(self.top_frame, text='Enter a distance in KM: ')
        self.kilo_entry = tkinter.Entry(self.top_frame)
        
        self.promt_label.pack(side='left')
        self.kilo_entry.pack(side='right')

        self.description_label = tkinter.Label(self.mid_frame, text="Converted to miles:")

        self.miles_var = tkinter.StringVar()
        self.miles_label = tkinter.Label(self.mid_frame, textvariable=self.miles_var)

        self.description_label.pack(side='left')
        self.miles_label.pack(side='left')

        self.calcbutton = tkinter.Button(self.main_window, text='Convert', command=self.convert)
        self.quit_button = tkinter.Button(self.main_window, text='Quit', command=self.main_window.destroy)

        self.top_frame.pack(side='top')
        self.mid_frame.pack(side='top')
        self.bottom_frame.pack(side='top')

        self.calcbutton.pack(side='left')
        self.quit_button.pack(side='right')

        tkinter.mainloop()


    def convert(self):
        kilo = float(self.kilo_entry.get())

        miles = round(kilo * 0.6214,2)

        self.miles_var.set(miles)

my_gui = kilo_conv()