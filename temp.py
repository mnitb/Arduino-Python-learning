port="9"#input("enter the port address: ")
tolerance_percentages=4 #float(input("enter the tolerance percentages: "))
import wmi
import serial
import time
neo=0
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
arduino = serial.Serial(port='COM'+port, baudrate=115200, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    data = arduino.readline()
    if x!=data.decode('UTF-8') : print("warning ",data.decode('UTF-8')," ",a)
while True:
	temperature_infos = w.Sensor()
	for sensor in temperature_infos:
		if sensor.SensorType==u'Temperature':
				#print(sensor.Name,end=' ')
				tg=int(sensor.Value)
				tg=str(tg)
		if (sensor.SensorType==u'Load') and (sensor.Name==u'Memory'):
			tg1=int(sensor.Value)
			tg1=str(tg1)
		if (sensor.SensorType==u'Load') and (sensor.Name==u'CPU Total'):
			tg2=int(sensor.Value+tolerance_percentages)
			tg2=str(tg2)
	if int(tg2)<=9:
		tg2=" "+tg2 
	a=tg+tg1+tg2
	#print("CPU.Usage",tg2+"%",end=" | ")
	#print("CPU.Temp",tg+"°C",end=" | ")
	#print("Ram.Usage",tg1+"%")
	print(tg2+"%",end=" | ")
	print(tg+"°C",end=" | ")
	print(tg1+"%")
	write_read(a)
	time.sleep(2)

