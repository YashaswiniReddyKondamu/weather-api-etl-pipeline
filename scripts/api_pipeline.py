import requests
import pandas as pd
import psycopg2

# API endpoint
url = "https://api.open-meteo.com/v1/forecast?latitude=32.7767&longitude=-96.7970&current_weather=true"

response = requests.get(url)
data = response.json()

weather = data["current_weather"]

df = pd.DataFrame([weather])

df["latitude"] = data["latitude"]
df["longitude"] = data["longitude"]

print("Weather Data:")
print(df)

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    database="sales_pipeline_db",
    user="postgres",
    password="Bunny@3110"
)

cursor = conn.cursor()

# Insert data
for index, row in df.iterrows():
    cursor.execute(
        """
        INSERT INTO weather_data
        (temperature, windspeed, winddirection, weathercode, time, latitude, longitude)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """,
        (
            row["temperature"],
            row["windspeed"],
            row["winddirection"],
            row["weathercode"],
            row["time"],
            row["latitude"],
            row["longitude"]
        )
    )

conn.commit()

cursor.close()
conn.close()

print("Weather data loaded into PostgreSQL")