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

try:
    # Connect to database
    conn = oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)
    cursor = conn.cursor()
    print("Connected to Database.")

    #Loading CSV Files
    severity_df = pd.read_csv(r"data\severity_information.csv")
    time_df = pd.read_csv(r"data\time_information.csv")
    coordinate_df = pd.read_csv(r"data\coordinate_information.csv")
    location_df = pd.read_csv(r"data\location_information.csv")
    accident_df = pd.read_csv(r"data\accident_information.csv")
    weather_df = pd.read_csv(r"data\weather_information.csv")
    print("CSV files loaded.")

    
    # 1. Severity Table
    for _, row in severity_df.iterrows():
        cursor.execute(
            "INSERT INTO SEVERITY (Time_Start, Time_End, Acc_Severity) VALUES (TO_DATE(:1,'yyyy/mm/dd hh:mi:ss am'),TO_DATE(:2,'yyyy/mm/dd hh:mi:ss am'), To_NUMBER(:3))",
            [row["Start_Time"], row["End_Time"], int(row["Severity"])]
        )

    print("Severity Table Loaded")

    # 2. Time Table
    for _, row in time_df.iterrows():
        cursor.execute(
            "INSERT INTO TIM (Time_ID, Time_Start, Time_End) VALUES (:1,TO_DATE(:2,'yyyy/mm/dd hh:mi:ss am'),TO_DATE(:3,'yyyy/mm/dd hh:mi:ss am'))",
            [row["Time_ID"],row["Start_Time"], row["End_Time"]]
        )

    print("Time Table Loaded")

    # 3. Coordinate Table
    for _, row in coordinate_df.iterrows():
        cursor.execute(
            "INSERT INTO COORDINATE (Loc_Start_Lat, Loc_Start_Lng, Loc_Street, Loc_City, Loc_County, Loc_State, Loc_Country, Loc_Timezone, Loc_Airport_Code) VALUES (:1, :2, :3, :4, :5, :6, :7, :8, :9)",
            [float(row["Start_Lat"]), float(row["Start_Lng"]), row["Street"], row["City"], row["County"], row["State"], row["Zipcode"], row["Country"], row["Airport_Code"]]
        )

    print("Coordinate Table Loaded")

    # 4. Location Table
    for _, row in location_df.iterrows():
        cursor.execute(
            "INSERT INTO LOC (Loc_ID, Loc_Start_Lat, Loc_Start_Lng, Loc_End_Lat, Loc_End_Lng) VALUES (:1, :2, :3, :4, :5)",
            [row["Location_ID"],float(row["Start_Lat"]), float(row["Start_Lng"]), float(row["End_Lat"]), float(row["End_Lng"])]
        )

    print("Location Table Loaded")
    # 5. Accident Table
    for _, row in accident_df.iterrows():
        cursor.execute(
            "INSERT INTO ACCIDENT (Acc_ID, Time_ID, Loc_ID, Acc_Source, Acc_Description, Acc_Distance) VALUES (:1, :2, :3, :4, :5, :6)",
            [row["ID"], row["Location_ID"], row["Time_ID"], row["Source"],float(row["Distance(mi)"]),row["Description"]]
        )

    print("Accident Table Loaded")

    # 6. Weather Table
    for _, row in weather_df.iterrows():
        cursor.execute(
            "INSERT INTO WEATHER (Time_ID, Loc_ID, Wea_Timestamp, Wea_Temperature, Wea_Condition, Wea_Wind_Chill, Wea_Humidity, Wea_Visibility, Wea_Wind_Direction, Wea_Wind_Speed, Wea_Precipitation, Wea_Sunrise_Sunset, Wea_Civil_Twilight, Wea_Nautical_Twilight, Wea_Astronomical_Twilight) VALUES (:1, :2, TO_TIMESTAMP(:3,'mm/dd/yyyy hh:mi:ss am'), :4, :5, :6, :7, :8, :9, :10, :11, :12, :13, :14, :15, :16, :17)",
            [row["Location_ID"], row["Time_ID"], row["Weather_Timestamp"], float(row["Temperature(F)"]), row["Weather_Condition"], float(row["Wind_Chill(F)"]), int(row["Humidity(%)"]), int(row["Visibility(mi)"]), row["Wind_Direction"], float(row["Wind_Speed(mph))"]),float(row["Precipitation(in)"]), row["Sunrise_Sunset"], row["Civil_Twilight"], row["Nautical_Twilight"], row["Astronomical_Twilight"]]
        )

    print("Weather Table Loaded")

except Exception as e:
        print(f"Error during bulk load: {e}")
        if 'conn' in locals():
            conn.rollback() # Undo changes if an error occurs

finally:
    if 'cursor' in locals(): cursor.close()
    if 'conn' in locals(): conn.close()