from flask import Flask
import Adafruit_DHT

app = Flask(__name__)

@app.route("/metrics")
def metrics():
    DHT11_sensor = Adafruit_DHT.DHT11
    DHT_pin = 4
    hum, temp = Adafruit_DHT.read_retry(DHT11_sensor, DHT_pin)
    if hum and temp:
        dht11_data = f"""garden_humidity {hum} 
garden_temperature {temp}"""

    return f"{dht11_data}", 200, {'Content-Type': 'text/plain; charset=utf-8'}

if __name__ == '__main__':
    app.run(host='0.0.0.0')