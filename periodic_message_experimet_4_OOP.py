
import serial # library used to communicate with serial port
import re # library used to extract data from string
import tkinter as tk
import sys


class WeatherStation(tk.Tk):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, **kwargs):
        super().__init__()
        self.geometry("500x200")
        self.title('Weather Station')
        self.resizable(False, False)
        self.btn_quit = tk.Button(master=self, text="Quit", font=50, command=self.close_application)
        self.btn_quit.place(x=230, y=100)
        self.lbl_temp = tk.Label(master=self, text="Initial text", font=50)
        self.lbl_temp.place(x=230, y=20)
        self.lbl_hum = tk.Label(master=self, text="Initial text", font=50)
        self.lbl_hum.place(x=100, y=20)
        self.lbl_pres = tk.Label(master=self, text="Initial text", font=50)
        self.lbl_pres.place(x=330, y=20)
        
    def run(self):
        self.mainloop()
        
    def close_application(self):
        self.destroy()
        
        
       
        
App = WeatherStation();
App.run()
        