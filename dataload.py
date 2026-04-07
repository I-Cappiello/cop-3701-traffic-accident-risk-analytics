import oracledb
import csv
import pandas as pd

# Configuration
LIB_DIR = r"C:\oraclexe\app\oracle\instantclient_11_2\instantclient_23_0" # Your Instant Client Path
DB_USER = "SYSTEM"
DB_PASS = "QuiteME3M"
DB_DSN  = "127.0.0.1:1521/XE"

# Initialize Oracle Client
oracledb.init_oracle_client(lib_dir=LIB_DIR)
# Defining CSV file paths and preparing SQL statements
severity_path = r"data\severity_information.csv"
severity_str = "INSERT INTO SEVERITY (Time_Start, Time_End, Sev_Rating) VALUES (to_date(:1,'YYYY-MM-DD HH24:MI:SS '), to_date(:2,'YYYY-MM-DD HH24:MI:SS'), :3)"

time_path = r"data\time_information.csv"
time_str = "INSERT INTO TIM (Time_ID, Time_Start, Time_End) VALUES (:1,to_date(:2,'YYYY-MM-DD HH24:MI:SS'), to_date(:3,'YYYY-MM-DD HH24:MI:SS'))"

coordinate_path = r"data\coordinate_information.csv"
coordinate_str = "INSERT INTO COORDINATE (Loc_Start_Lat, Loc_Start_Lng, Loc_Street, Loc_City, Loc_County, Loc_State, Loc_Country, Loc_Timezone, Loc_Airport_Code) VALUES (:1,:2,:3,:4,:5,:6,:7,:8,:9)"

location_path = r"data\location_information.csv"
location_str = "INSERT INTO LOC (Loc_ID, Loc_Start_Lat, Loc_Start_Lng, Loc_End_Lat, Loc_End_Lng) VALUES (:1,:2,:3,:4,:5)"

accident_path = r"data\accident_information.csv"
accident_str = "INSERT INTO ACCIDENT (Acc_ID, Time_ID, Loc_ID, Acc_Source, Acc_Description, Acc_Distance) VALUES (:1,:2,:3,:4,:5,:6)"

weather_path = r"data\weather_information.csv"
weather_str = "INSERT INTO WEATHER (Time_ID, Loc_ID, Wea_Timestamp, Wea_Temperature, Wea_Condition, Wea_Wind_Chill, Wea_Humidity, Wea_Visibility, Wea_Wind_Direction, Wea_Wind_Speed, Wea_Pressure, Wea_Precipitation) VALUES (:1,:2,to_date(:3,'YYYY-MM-DD HH24:MI:SS'),:4,:5,:6,:7,:8,:9,:10,:11,:12)"
print("CSV files loaded.")

# Load function 
def bulk_load(file_path, sql_str):
    try:
        # 1. Connect to database
        conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
        cursor = conn.cursor()
        print("Connected to Database.")

        # 2. Reading file
        with open(file_path, mode='r', encoding="utf-8") as f:
            reader = csv.reader(f)
            next(reader)
            data_to_insert = [row for row in reader]
        
        print("Table Read")

        # 3. Prepare Bulk Insert SQL
        sql = sql_str

        # 4. Execute Batch
        print(f"Start bulk load of {len(data_to_insert)} raw...")
        cursor.executemany(sql, data_to_insert)

        # 5. Commit Changes
        conn.commit()
        print(f"Successfully Loaded {cursor.rowcount} rows into database")
        
    except Exception as e:
            print(f"Error during bulk load: {e}")
            if 'conn' in locals():
                conn.rollback() # Undo changes if an error occurs

    finally:
        if 'cursor' in locals(): cursor.close()
        if 'conn' in locals(): conn.close()

# Loading the csv files into the database
bulk_load(severity_path, severity_str)
bulk_load(time_path, time_str)
bulk_load(coordinate_path, coordinate_str)
bulk_load(location_path, location_str)
bulk_load(accident_path, accident_str)
bulk_load(weather_path, weather_str)
