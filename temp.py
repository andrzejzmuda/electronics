import sys
import Adafruit_DHT

while True:
	humid, temp = Adafruit_DHT.read_retry(11,4)

	print('Temp: {0:0.1f} C Humid: {1:0.1f}').format(temp, humid)
