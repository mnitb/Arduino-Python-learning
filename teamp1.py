import wmi
import serial
import time
import os
port=os.path.basename(__file__).replace(".py","")
port=port.replace(".exe","")
tolerance_percentages=4 #float(input("enter the tolerance percentages: "))
w = wmi.WMI(namespace="root\OpenHardwareMonitor")
arduino = serial.Serial(port='COM'+port, baudrate=115200, timeout=.1)
def write_read(x):
    arduino.write(bytes(x, 'utf-8'))
    time.sleep(0.05)
    #if x !=arduino.readline().decode('utf-8'): print(False)
    #print(arduino.readline().decode('utf-8'))
while True:
	temperature_infos = w.Sensor()
	for sensor in temperature_infos:
		if sensor.SensorType==u'Temperature':
			cputemp=int(sensor.Value)
			cputemp=str(cputemp)
		if (sensor.SensorType==u'Load') and (sensor.Name==u'Memory'):
			ramloads=int(sensor.Value)
			ramloads=str(ramloads)
		if (sensor.SensorType==u'Load') and (sensor.Name==u'CPU Total'):
			cpuloads=int(sensor.Value+tolerance_percentages)
			cpuloads=str(cpuloads)
	if int(cpuloads)<=9:
		cpuloads=" "+cpuloads 
	a=cputemp+ramloads+cpuloads+time.asctime(time.localtime(time.time()))[11:13]+time.asctime(time.localtime(time.time()))[14:16]
	#print(a)
	write_read(a)
	time.sleep(2)

