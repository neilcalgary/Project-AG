#!/usr/bin/python3
import psycopg2
import time
import json
from pprint import pprint
from miflora.miflora_poller import MiFloraPoller, \
    MI_CONDUCTIVITY, MI_MOISTURE, MI_LIGHT, MI_TEMPERATURE, MI_BATTERY

with open('/home/pi/garden/config.json') as f:
    config = json.load(f)

try:
    connection = psycopg2.connect(user = config["user"],
                                  password = config["password"],
                                  host = config["host"],
                                  port = config["port"],
                                  database = config["database"])
    cursor = connection.cursor()
    address1 = "C4:7C:xx:xx:xx:xx"
    poller1 = MiFloraPoller(address1)

    temp = poller1.parameter_value("temperature")
    moisture = poller1.parameter_value(MI_MOISTURE)
    light = poller1.parameter_value(MI_LIGHT)
    fertility = poller1.parameter_value(MI_CONDUCTIVITY)
    battery = poller1.parameter_value(MI_BATTERY)
    currentTime = int(time.time()) 
    sql = "insert into greenhouse.outdoor_1 (\"time\", temperature, moisture, light, fertility, battery) values ({},{},{},{},{},{})".format(currentTime,temp,moisture,light,fertility,battery)
    cursor.execute(sql)
    connection.commit()
    print("saved data to db.")
    #print("Mi Flora: " + address1)
    #print("Firmware: {}".format(poller1.firmware_version()))
    #print("Name: {}".format(poller1.name()))
    #print("Temperature: {}°C".format(temp))
    #print("Moisture: {}%".format(moisture))
    #print("Light: {} lux".format(light))
    #print("Fertility: {} uS/cm?".format(fertility))
    #print("Battery: {}%".format(battery))

except (Exception, psycopg2.Error) as error :
    print ("Error while connecting to PostgreSQL", error)
finally:
    #closing database connection.
    print("close connection to db.")
    if(connection):
        cursor.close()
        connection.close()
