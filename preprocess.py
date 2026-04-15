import pandas as pd
import csv
from datetime import datetime, timedelta

# input file
input_file = r"Tiny_US_Accidents_March23.csv"

# read csv
df = pd.read_csv(input_file)

# 1. Severity information csv
severity_df = df[
    [
        "Start_Time",
        "End_Time",
        "Severity",
    ]
].drop_duplicates(subset=["Start_Time","End_Time"]).copy()

# 2. time information csv
time_df = df[
    [
        "Start_Time",
        "End_Time",
    ]
].drop_duplicates(subset=["Start_Time","End_Time"]).copy()
time_df.insert(0,"Time_ID",range(1,len(time_df)+1))

# 3. coordinate information csv
coordinate_df = df[
    [
        "Start_Lat",
        "Start_Lng",
        "Street",
        "City",
        "County",
        "State",
        "Country",
        "Timezone",
        "Airport_Code",
    ]
].drop_duplicates(subset=["Start_Lat","Start_Lng"]).copy()

# 4. location information csv
location_df = df[
    [
        "Start_Lat",
        "Start_Lng",
        "End_Lat",
        "End_Lng",
    ]
].drop_duplicates(subset=["Start_Lat","Start_Lng"]).copy()
location_df.insert(0,"Location_ID",range(1,len(location_df)+1))

# 5. accident information csv
temp_accident_df = df[
    [
        "ID",
        "Source",
        "Description",
        "Distance(mi)",
        "Start_Lat",
        "Start_Lng",
        "Start_Time",
        "End_Time",
    ]
].drop_duplicates(subset=["ID"]).copy()
temp_accident_df = pd.merge(temp_accident_df,location_df, "left", on=["Start_Lat","Start_Lng"])
temp_accident_df = pd.merge(temp_accident_df,time_df, "left", on=["Start_Time","End_Time"])

accident_df = temp_accident_df[
    [
        "ID",
        "Time_ID",
        "Location_ID",
        "Source",
        "Description",
        "Distance(mi)",
    ]
].drop_duplicates("ID").copy()

# 6. weather features information csv
temp_weather_df = df[
    [
        "Start_Lat",
        "Start_Lng",
        "Start_Time",
        "End_Time",
        "Weather_Timestamp",
        "Temperature(F)",
        "Weather_Condition",
        "Wind_Chill(F)",
        "Humidity(%)",
        "Visibility(mi)",
        "Wind_Direction",
        "Wind_Speed(mph)",
        "Pressure(in)",
        "Precipitation(in)",
    ]
]
temp_weather_df = pd.merge(temp_weather_df,location_df, "left", on=["Start_Lat","Start_Lng"])
temp_weather_df = pd.merge(temp_weather_df,time_df, "left", on=["Start_Time","End_Time"])

weather_df = temp_weather_df[
    [
        "Time_ID",
        "Location_ID",
        "Weather_Timestamp",
        "Temperature(F)",
        "Weather_Condition",
        "Wind_Chill(F)",
        "Humidity(%)",
        "Visibility(mi)",
        "Wind_Direction",
        "Wind_Speed(mph)",
        "Pressure(in)",
        "Precipitation(in)",
    ]
].drop_duplicates(subset=["Location_ID","Time_ID"]).copy()

# save files
accident_df.to_csv(r"data\accident_information.csv", index=False)
time_df.to_csv(r"data\time_information.csv", index=False)
severity_df.to_csv(r"data\severity_information.csv", index=False)
location_df.to_csv(r"data\location_information.csv", index=False)
coordinate_df.to_csv(r"data\coordinate_information.csv", index=False)
weather_df.to_csv(r"data\weather_information.csv", index=False)

print("CSV files successfully generated.")
