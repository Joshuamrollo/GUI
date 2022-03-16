import tkinter
import tkinter.messagebox

class kilo_conv:
    def __init__(self):
        self.main_window = tkinter.Tk()

        self.main_window.geometry('600x300')
        self.main_window.title('Student Test Average')

        self.frame1 = tkinter.Frame(self.main_window)
        self.frame2 = tkinter.Frame(self.main_window)
        self.frame3 = tkinter.Frame(self.main_window)
        self.frame4 = tkinter.Frame(self.main_window)
        self.frame5 = tkinter.Frame(self.main_window)

        self.frame1.pack(side='top')
        self.frame2.pack(side='top')
        self.frame3.pack(side='top')
        self.frame4.pack(side='top')
        self.frame5.pack(side='top')

        self.label1 = tkinter.Label(self.frame1, text='Enter the score for test 1:')
        self.input1 = tkinter.Entry(self.frame1)

        self.label1.pack(side='left')
        self.input1.pack(side='left')

        self.label2 = tkinter.Label(self.frame2, text='Enter the score for test 2:')
        self.input2 = tkinter.Entry(self.frame2)

        self.label2.pack(side='left')
        self.input2.pack(side='left')

        self.label3 = tkinter.Label(self.frame3, text='Enter the score for test 3:')
        self.input3 = tkinter.Entry(self.frame3)

        self.label3.pack(side='left')
        self.input3.pack(side='left')

        self.avg_label = tkinter.Label(self.frame4, text="Average:")
        self.avg_var = tkinter.StringVar()
        self.avg = tkinter.Label(self.frame4, textvariable=self.avg_var)

        self.avg_label.pack(side='left')
        self.avg.pack(side='left')

        self.avg_button = tkinter.Button(self.frame5, text='Average', command=self.calc)
        self.quit_button = tkinter.Button(self.frame5, text='Quit', command=self.main_window.destroy)

        self.avg_button.pack(side='left')
        self.quit_button.pack(side='right')

        #color
        self.main_window.config(bg='green')
        self.frame4.config(bg='green')
        self.frame1.config(bg='green')
        self.frame3.config(bg='green')
        self.frame2.config(bg='green')
        self.frame5.config(bg='green')
        self.avg_button.config(bg='green', fg='yellow')
        self.quit_button.config(bg='green', fg='yellow')
        self.label1.config(bg='green', fg='yellow')
        self.label3.config(bg='green', fg='yellow')
        self.label2.config(bg='green', fg='yellow')
        self.avg_label.config(bg='green', fg='yellow')
        self.input1.config(bg='green', fg='yellow')
        self.input2.config(bg='green', fg='yellow')
        self.input3.config(bg='green', fg='yellow')
        self.avg.config(bg='green', fg='yellow')




        tkinter.mainloop()


    def calc(self):
        num1 = float(self.input1.get())
        num2 = float(self.input2.get())
        num3 = float(self.input3.get())
        avg = (num1 + num2 + num3) / 3

        self.avg_var.set(avg)

my_gui = kilo_conv()