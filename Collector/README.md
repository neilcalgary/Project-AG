# garden
Collect Mi Flower sensor data and save to Postgresql server
Please copy config_.json to config.json and update to correct Postgresql connection

Please Run this command to get your mi flower sensor bluetooth address
sudo hcitool scan
You are going to get some thing like
C4:7C:xx:xx:xx:xx Flower care

copy the address to collect.py 19 replace default address

You need to edit crontab to decide how frequently you need to collect data, battery will cost for every pull
this is pull data every hour
sudo vim /etc/crontab 
0 * * * * pi  python3 /home/pi/garden/collect.py #add this line to the end of the file

Table structure

CREATE TABLE greenhouse.outdoor_1
(
    "time" bigint NOT NULL,
    temperature real,
    moisture real,
    light real,
    fertility real,
    battery real,
    CONSTRAINT outdoor_1_pkey PRIMARY KEY ("time")
)
