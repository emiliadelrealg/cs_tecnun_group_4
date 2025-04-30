
import serial # library used to communicate with serial port
import re # library used to extract data from string
import tkinter as tk
import sys


class WeatherStation(tk.Tk):
    def __new__(cls, *args, **kwargs):
        return super().__new__(cls)
    
    def __init__(self, **kwargs):
        super().__init__()


def extract_temp(message):
    
    data_string = message.decode("utf-8")
    temp = re.findall('<temp=([\d]+[.,\d]+),', data_string) # extract values from string
    if temp:
        return temp[0]
    else:
        return temp
    

def extract_hum (message):
    
    data_string = message.decode("utf-8")
    hum = re.findall('hum=([\d]+[.,\d]+),', data_string) # extract values from string
    if hum:
        return hum[0]
    else:
        return hum
   

def extract_pres (message):
    
    data_string = message.decode("utf-8")
    pres = re.findall('pres=([\d]+[.,\d]+)>', data_string) # extract values from string
    if pres:
        return pres[0]
    else:
        return pres
   

def close_application():
    window.destroy()

def extract_data(message):
    temp=extract_temp(message)
    hum=extract_hum(message)
    pres=extract_pres(message)
    data=[temp, hum, pres]
    data_values= [float(num) for num in data if num]
    data_values=[values +10 if values.is_integer() else values for values in data_values ]
    return data_values

def get_weather() :
    global data_file
    print("get_weather() working...")
    message = ser.readline() # read one line (until EOL) from the serial port
    print(message)
    temp=extract_temp(message)
    hum=extract_hum(message)
    pres=extract_pres(message)
    data= extract_data(message)
    print(data)
    if len(data)==3:
        temp, hum, pres= [f"{values}" for values in data]
    print(temp)
    print(hum)
    print(pres)
    if temp:
        data_file.write(f'{temp}; {pres}; {hum}\n')
    if temp:
       lbl_temp["text"]= temp + " ºC"
       lbl_hum["text"]=hum + " %"
       lbl_pres["text"]=pres + " hPa"
    
    window.after(1000, get_weather)
  
    
SERIAL_SPEED = 9600
COM_PORT = 'COM5'
ser = serial.Serial() # create a serial instance
ser.port = COM_PORT # set the port number
ser.baudrate = SERIAL_SPEED # set the baudrate of the port
    
    
try:
    ser.open() # open the serial port
    if ser.isOpen(): # check if the serial port is opened successfully
        print("Port " + ser.port + " opened successfully")
        
except Exception as e:
    print(e)
    


try:
    data_file=open("archivo.csv","w")
    
except IOError as e:
    print(f"Error al abrir el archivo: {e}")
    sys.exit()
    
window = tk.Tk()
window.geometry("500x200")

btn_quit = tk.Button(master=window, text="Quit", font=50, command=close_application)
btn_quit.place(x=230, y=100)
lbl_temp = tk.Label(master=window, text="Initial text", font=50)
lbl_temp.place(x=230, y=20)
lbl_hum = tk.Label(master=window, text="Initial text", font=50)
lbl_hum.place(x=100, y=20)
lbl_pres = tk.Label(master=window, text="Initial text", font=50)
lbl_pres.place(x=330, y=20)
window.after(1000, get_weather)

window.mainloop()

ser.close()
data_file.close()

