# garden
Collect Mi Flower sensor data and save to Postgresql server
Please copy config_.json to config.json and update to correct Postgresql connection

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
