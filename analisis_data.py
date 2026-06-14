import pandas as pd

# 1. Membaca data yang sudah kita generate
print("Membaca file data (500rb baris)...")
df = pd.read_csv('transportation_large_data.csv')

# 2. Analisis Dasar: Rata-rata penumpang berdasarkan kondisi cuaca
print("\n--- Rata-rata Penumpang Berdasarkan Cuaca ---")
weather_stats = df.groupby('weather_condition')['passenger_count'].mean()
print(weather_stats)

# 3. Analisis Dasar: Tren Akhir Pekan
print("\n--- Perbandingan Hari Kerja vs Akhir Pekan ---")
weekend_stats = df.groupby('is_weekend')['passenger_count'].mean()
print(weekend_stats)

# 4. Analisis Performa Rute
print("\n--- Rute dengan Penumpang Terbanyak ---")
route_stats = df.groupby('route_id')['passenger_count'].sum().sort_values(ascending=False)
print(route_stats)

print("\nAnalisis selesai!")