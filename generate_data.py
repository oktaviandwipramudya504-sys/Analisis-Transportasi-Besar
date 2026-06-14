import pandas as pd
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

NUM_ROWS = 500000
routes = ['R01', 'R02', 'R03', 'R04']
weather = ['Cerah', 'Hujan', 'Mendung', 'Badai']

data = []
start_date = datetime(2025, 1, 1)

print(f"Memulai proses generate {NUM_ROWS} baris...")

for i in range(NUM_ROWS):
    if i % 100000 == 0 and i > 0:
        print(f"Sudah memproses {i} baris...")
        
    timestamp = start_date + timedelta(days=random.randint(0, 365), hours=random.randint(0, 23))
    data.append({
        'timestamp': timestamp.strftime('%Y-%m-%d %H:%M:%S'),
        'route_id': random.choice(routes),
        'passenger_count': random.randint(10, 100),
        'is_weekend': 1 if timestamp.weekday() >= 5 else 0,
        'weather_condition': random.choice(weather),
        'travel_time_min': random.randint(20, 90)
    })

df = pd.DataFrame(data)
df.to_csv('transportation_large_data.csv', index=False)
print("Selesai! File 'transportation_large_data.csv' telah dibuat.")