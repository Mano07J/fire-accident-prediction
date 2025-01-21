import machine
import time
import urequests
import json

# Initialize sensors
temperature_sensor = machine.ADC(machine.Pin(34))
smoke_sensor = machine.ADC(machine.Pin(35))
humidity_sensor = machine.ADC(machine.Pin(32))
gas_sensor = machine.ADC(machine.Pin(33))

# Azure IoT Hub details
iot_hub_url = "https://<YOUR_IOT_HUB_NAME>.azure-devices.net/devices/<DEVICE_ID>/messages/events?api-version=2018-06-30"
sas_token = "<YOUR_SAS_TOKEN>"

# Function to send data
def send_data_to_azure(temperature, smoke, humidity, gas):
    data = {
        "temperature": temperature,
        "smoke": smoke,
        "humidity": humidity,
        "gas": gas
    }
    headers = {
        "Authorization": sas_token,
        "Content-Type": "application/json"
    }
    response = urequests.post(iot_hub_url, headers=headers, json=data)
    print("Data sent to Azure:", response.status_code)

# Main loop
while True:
    temperature = temperature_sensor.read() * 0.1  # Convert to Celsius
    smoke = smoke_sensor.read() * 0.1
    humidity = humidity_sensor.read() * 0.1
    gas = gas_sensor.read() * 0.1
    
    send_data_to_azure(temperature, smoke, humidity, gas)
    time.sleep(60)  # Send data every minute
