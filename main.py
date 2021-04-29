import serial
from win32com.client import Dispatch as d
from os import system as s
from time import sleep as s

sum = 0
engine = d("SAPI.SpVoice")
ser = serial.Serial('COM4', baudrate = 9600, timeout = 1)


while True:
	try:
		data = int(str(ser.readline().decode('ascii')).replace('\r\n', '').replace("'", ''))
		print(f'Расстояние до объекта: {data}см')
		if data < 80:
			engine.Speak('Стой падла, расстреляю')
			s(2)
		data = 100
	except:
		pass

#ser.write('1\r\n')