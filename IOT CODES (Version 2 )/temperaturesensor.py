import adafruit_dht
import time
import board
dhtDevice = adafruit_dht.DHT22(board.D4)
while True:
    try:
        temperature = dhtDevice.temperature
        humidity = dhtDevice.humidity
        print('Temp={0:0.1f}*C Humidity={1:0.1f}%'.format(temperature,humidity))
    except RuntimeError as error:
        print(error.args[0])
        time.sleep(2.0)
        continue
    except Exception as error :
        dhtDevice.exit()
        raise error
    time.sleep(2.0)
