
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
        self.after(1000, self.get_weather)
        self.mainloop()
        
    def close_application(self):
        self.destroy()
        
        
    def extract_temp(self,message):

        data_string = message.decode("utf-8")
        temp = re.findall('<temp=([\d]+[.,\d]+),', data_string) # extract values from string
        if temp:
            return temp[0]
        else:
            return temp
      
        
        
    def extract_hum (self ,message):
          
        data_string = message.decode("utf-8")
        hum = re.findall('hum=([\d]+[.,\d]+),', data_string)
        
        if hum:
            return hum[0]
        else:
            return hum
        
        
        
    def extract_pres (self, message):
        
        data_string = message.decode("utf-8")
        pres = re.findall('hum=([\d]+[.,\d]+),', data_string)
        
        if pres:
            return pres[0]
        else:
            return pres
      
    
    def extract_data(self, message):
        self.temp=self.extract_temp(message)
        self.hum=self.extract_hum(message)
        self.pres=self.extract_pres(message)
        self.data=[self.temp, self.hum, self.pres]
        self.data_values= [float(num) for num in self.data if num]
        #data_values=[values +10 if values.is_integer() else values for values in data_values ]
       
        
        return data_values
    
    
    def get_weather() :
       # global data_file
        print("get_weather() working...")
        message = b'<temp=4.2,humd=42,press=1042>' # read one line (until EOL) from the serial port
        print(message)
        temp=self.extract_temp(message)
        hum=self.extract_hum(message)
        pres=self.extract_pres(message)
        data= self.extract_data(message)
        print(data)
        
        #if len(data)==3:
            #temp, hum, pres= [f"{values}" for values in data]
        print(temp)
        print(hum)
        print(pres)
        #if temp:
            #data_file.write(f'{temp}; {pres}; {hum}\n')
        if temp:
           self.lbl_temp["text"]= temp + " ºC"
           self.lbl_hum["text"]=hum + " %"
           self.lbl_pres["text"]=pres + " hPa"
           
         
        
    
        
        
       
        
App = WeatherStation();
App.run()
        