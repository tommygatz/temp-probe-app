import time
import datetime
from w1thermsensor import W1ThermSensor
from influxdb import InfluxDBClient



w1 = W1ThermSensor()
#w1.set_resolution(9)

#sensors = w1.get_available_sensors()

#print(sensors)

#sensor_names = {"020592450037": "Sensor 1", "021692451bad": "Sensor 2", "02079245806f": "Sensor 3"}

sensor1 = W1ThermSensor(sensor_id='020592450037')
sensor2 = W1ThermSensor(sensor_id='021692451bad')
sensor3 = W1ThermSensor(sensor_id='02079245806f')


def send_to_influxdb(measurement, location, timestamp, temperature):
    payload = [
        {"measurement": measurement,
            "tags": {
                "location": location,
            },
            "time": timestamp,
            "fields": {
                "temperature" : temperature
            }
        }
      ]

    client.write_points(payload)


measurements = [
	"Temp 1",
	"Temp 2",
	"Temp 3"
]

locations = [
	"Temp 1 Sensor",
	"Temp 2 Sensor",
	"Temp 3 Sensor"
]


timestamp = datetime.datetime.utcnow()

s1temp = round(sensor1.get_temperature(W1ThermSensor.DEGREES_F),2)
s2temp = round(sensor2.get_temperature(W1ThermSensor.DEGREES_F),2)
s3temp = round(sensor3.get_temperature(W1ThermSensor.DEGREES_F),2)

# Set up InfluxDB
host = '127.0.0.1'  # Change this as necessary
port = 8086
username = 'grafana'  # Change this as necessary
password = 'grafana'  # Change this as necessary
db = 'home'  # Change this as necessary

# InfluxDB client to write to
client = InfluxDBClient(host, port, username, password, db)



send_to_influxdb(measurements[0], locations[0], timestamp, s1temp)
send_to_influxdb(measurements[1], locations[1], timestamp, s2temp)
send_to_influxdb(measurements[2], locations[2], timestamp, s3temp)


