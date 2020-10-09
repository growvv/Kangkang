import serial
import time
ser = serial.Serial('/dev/ttyACM0',9600,timeout=1)
time.sleep(2.0)
fo = open("out.txt","r")
end = fo.read()
fo.close()
#str.encode(end)
#print type(end)
#end = 'n'
time.sleep(1.0)
end = int(end)
if end == 1:
    t = '1'
if end == 0:
    t = '2'
#print type(end)
ser.flush()
try:
    ser.write(t)
    res = ser.readline()
    print res
    ser.flush()
except:
    ser.close()

