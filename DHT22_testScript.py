import Adafruit_DHT
sensor = Adafruit_DHT.DHT22

#This is the GPIO Pin number, not just the Pin number.
#This pin in pin 7 but sits in GPIO Pin 4. Use 4 below.
pin = 4

humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
temperature = temperature * 9/5.0 + 32

if humidity is not None and temperature is not None:
        print('Temp={0:0.1f}*F  Humidity={1:0.1f}%'.format(temperature, humidity))
else:
print('Failed to get reading. Try again!')