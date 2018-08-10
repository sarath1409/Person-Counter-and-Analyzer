import pandas as pd
import RPi.GPIO as IO
import datetime as dt
import time
import os.path
IO.setwarnings(False)
IO.setmode(IO.BCM)
IO.setup(2,IO.OUT)#GPIO 2 -> Red LED as output
IO.setup(3,IO.OUT)#GPIO 3 -> Green LED as output
IO.setup(14,IO.IN)#GPIO 14 -> IR sensor as input
print('_______________READY_______________')
file_name = "Report_for_" + str(dt.datetime.now().strftime("%d-%m-%y"))+".csv"
start_hour,end_hour = 0,59	#entering the starting and closing times of shopping malls in 24 hours
count = 0#count variable
time_field = "%M"

df = pd.DataFrame(columns = ['Count','Time'] )
df.Count = [0]*(end_hour+1 - start_hour)
df.Time = list(range(start_hour,end_hour+1))
df.set_index('Time',inplace=True)

if(os.path.isfile(file_name)):
	print("File Exists!")
	df1 = pd.read_csv(file_name)
	df1.set_index('Time',inplace=True)
	df = df.add(df1)
	
t = int(dt.datetime.now().strftime(time_field))
while(True):
	if(t <= end_hour and t>= start_hour):
		if(t < int(dt.datetime.now().strftime(time_field))):
			t = int(dt.datetime.now().strftime(time_field))
			count = 0

		if(IO.input(14) == True): #object is far away
			IO.output(2,True)
			IO.output(3,False)

		if(IO.input(14) == False): #object if nearby
			IO.output(3,True)
			IO.output(2,False)
			count += 1
			print("{0}:time || {1}:count".format(t,count))
			df.at[t,'Count'] = count
			df.to_csv(file_name)
			time.sleep(1.5000)


			
			

