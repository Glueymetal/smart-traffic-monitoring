import random as rm
import string
from datetime import datetime
import time

def generate_id(length = 5):
    characters = string.ascii_letters + string.digits
    return ''.join(rm.choice(characters) for i in range(length))

def generate_reading():
    intersection_id = rm.randint(1,5)
    vehicle_count = rm.randint(5,70)
    avg_speed = rm.uniform(10,60)
    temp_reading = rm.uniform(-10,70)
    if rm.random() < 0.05:
        air_quality = rm.uniform(100,110)
    else:
        air_quality = rm.uniform(72,90)
    rfid_id = generate_id()
    dt = datetime.now()

    record = {"intersection_id" : intersection_id,
            "vehicle_count" : vehicle_count,
            "average_speed": avg_speed,
            "temperature_reading": temp_reading,
            "air quality": air_quality,
            "rfid": rfid_id,
            "timestamp": datetime.isoformat(dt)}
    
    return record

def process_reading(record):
    congestion = False
    poorAirQuality = False
    if record["vehicle_count"] > 50 and record["average_speed"] <= 20:
        congestion = True
    if record["air quality"] > 90:
        poorAirQuality = True
    dt =  datetime.now()
    result = {"intersection_id":record["intersection_id"],
              "timestamp":datetime.isoformat(dt),
              "Congestion":congestion,
              "Poor_Air_Quality":poorAirQuality,
              "alert_required":congestion | poorAirQuality}
    return result


while True:
    record = generate_reading() 
    print(record)
    result = process_reading(record)
    print(result)
    if result["alert_required"]:
        print("ALERT!! - Notifying the traffic authority now.")
    time.sleep(5)
