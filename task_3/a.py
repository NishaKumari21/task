python
Copy code
from datetime import datetime
import time

while True:
    weather_data = get_weather_data(CITY)
    if is_heat_wave(weather_data):
        conn = sqlite3.connect('users.db')
        c = conn.cursor()
        c.execute('SELECT phone FROM users')
        users = c.fetchall()
        conn.close()

        for user in users:
            send_alert(user[0], "Heatwave Alert! Temperatures are expected to exceed 35°C.")
    
    # Run every hour
    time.sleep(3600)