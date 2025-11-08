"""
Simulates healthcare IoT sensors (temperature, heart rate, SpO2) and exposes Prometheus metrics.
"""

from prometheus_client import Gauge, start_http_server
import random, time

# Define metrics
temp = Gauge('patient_temperature_celsius', 'Patient temperature in Celsius')
heart_rate = Gauge('patient_heart_rate_bpm', 'Patient heart rate in beats per minute')
spo2 = Gauge('patient_spo2_percent', 'Patient oxygen saturation percentage')

if __name__ == '__main__':
    # start_http_server(8000)
    start_http_server(8000, addr='0.0.0.0')
    """
    binds only to localhost inside the process environment, which in Docker or some Linux setups may not be reachable from outside.

✅ Fix: explicitly bind to all interfaces:

start_http_server(8000, addr='0.0.0.0')

0.0.0.0 means “listen on all network interfaces”

127.0.0.1 or nothing means “listen only on local host”
    """

    print('Starting sensor simulator on port 8000...')
    while True:
        temp.set(round(random.uniform(36.0, 39.0), 1))
        heart_rate.set(random.randint(60, 110))
        spo2.set(random.randint(90, 100))
        print(f"Updated vitals: Temp={temp._value.get()}°C, HR={heart_rate._value.get()} bpm, SpO2={spo2._value.get()}%")
        time.sleep(5)
