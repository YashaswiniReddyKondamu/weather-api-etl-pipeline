# Weather API ETL Pipeline

This project demonstrates an ETL pipeline that extracts weather data from a public API, transforms it using Python and Pandas, and loads it into a PostgreSQL database.

## Pipeline Architecture

API → Python → Pandas → PostgreSQL

## Technologies Used

- Python
- Requests
- Pandas
- PostgreSQL
- psycopg2
- Git & GitHub

## Project Structure

weather_api_pipeline
│
├── scripts
│   ├── extract.py
│   ├── transform.py
│   ├── load.py
│   └── main.py
│
├── data
├── sql
└── README.md

## How to Run the Pipeline

1. Install dependencies
pip install requests pandas psycopg2-binary

2. Run the pipeline
python scripts/main.py

## Output

Weather data is stored in the PostgreSQL table `weather_data`.