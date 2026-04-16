'''
If you are running this code first time, and you don't have streamlit installed, then follow this instruction:
1. open a terminal
2. enter this command
    pip install streamlit
'''
import pandas as pd
import streamlit as st
import oracledb

# --- DATABASE SETUP ---
# Update this path to your local Instant Client folder
LIB_DIR = r"C:\Users\boltm\Documents\instantclient_11_2"


# Your Oracle Credentials
DB_USER = "system" # or your FreeSQL username
DB_PASS = "password" # your password for the dbms user
DB_DSN  = "localhost:1521/xe" # or your FreeSQL DSN

# Initialize Oracle Client for Thick Mode
@st.cache_resource
def init_db():
    if LIB_DIR:
        try:
            oracledb.init_oracle_client(lib_dir=LIB_DIR)
        except Exception as e:
            st.error(f"Error initializing Oracle Client: {e}")


init_db()


def get_connection():
    return oracledb.connect(user=DB_USER, password=DB_PASS, dsn=DB_DSN)


# --- STREAMLIT UI ---
st.title("Traffic Accident Risk Analytics Database")

menu = ["Spatial Coordinate Query", "Spatial State Query", "Severity Ranking Query", "City Finder Query", "Time Period Query"]
choice = st.sidebar.selectbox("Select Action", menu)

# --- Average Death Rate ---
if choice == "Spatial Coordinate Query":
    st.write("### Find a Region's Average Death Rate")
    loc_start_lng = st.text_input("Enter longitude1: )")
    loc_start_lat = st.text_input("Enter latitude1: )")
    loc_end_lng = st.text_input("Enter longitude2: )")
    loc_end_lat = st.text_input("Enter latitude2: )")
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"Select a.ACC_ID, a.ACC_DESCRIPTION, a.LOC_ID, l.LOC_START_LAT, l.LOC_START_LNG, l.LOC_ID FROM ACCIDENT a JOIN LOC l ON a.LOC_ID = l.LOC_ID WHERE l.LOC_START_LAT BETWEEN {loc_start_lat} AND {loc_end_lat} AND l.LOC_START_LNG BETWEEN {loc_start_lat} AND {loc_end_lat}")
        data = cur.fetchall()
        df = pd.DataFrame(data)
        cur.close()
        conn.close()

        if data:
            st.table(df)
        else:
            st.info("No records found.")
    except Exception as e:
        st.error(f"Error: {e}")

# --- Retrieve Region Data ---
if choice == "Spatial State Query":
    st.write("### Retrieve State Data")
    state_name = st.text_input("Enter a State Name (Case Sensitive)")
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"Select a.ACC_ID, a.ACC_DESCRIPTION, a.LOC_ID, l.LOC_START_LAT, l.LOC_START_LNG, l.LOC_ID, c.LOC_START_LAT, c.LOC_START_LNG, c.LOC_STATE FROM ACCIDENT a JOIN LOC l ON a.LOC_ID = l.LOC_ID JOIN COORDINATE c ON l.LOC_START_LNG = c.LOC_START_LNG WHERE c.LOC_STATE = \'{state_name}\'")
        data = cur.fetchall()
        df = pd.DataFrame(data)
        cur.close()
        conn.close()

        if data:
            st.table(df)
        else:
            st.info("No records found.")
    except Exception as e:
        st.error(f"Error: {e}")

# --- Retrieve Country Data ---
if choice == "Severity Ranking Query":
    st.write("Severity Ranking Query")
    severity = st.text_input("Enter a Severity")
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"Select a.ACC_ID, a.ACC_DESCRIPTION, a.TIME_ID, t.TIME_ID, t.TIME_START, t.TIME_END, s.TIME_START, s.SEV_RATING FROM ACCIDENT a JOIN TIM t ON a.TIME_ID = t.TIME_ID JOIN SEVERITY s ON t.TIME_START = s.TIME_START WHERE s.SEV_RATING = {severity}")
        data = cur.fetchall()
        df = pd.DataFrame(data)

        cur.close()
        conn.close()

        if data:
            st.table(df)
        else:
            st.info("No records found.")
    except Exception as e:
        st.error(f"Error: {e}")

# --- Find Report Provider ---
if choice == "City Finder Query":
    st.write("### Find City Data")
    city_name = st.text_input("Enter a City Name (Case Sensitive)")
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"Select a.ACC_ID, a.ACC_DESCRIPTION, a.LOC_ID, l.LOC_START_LAT, l.LOC_START_LNG, l.LOC_ID, c.LOC_START_LAT, c.LOC_START_LNG, c.LOC_CITY FROM ACCIDENT a JOIN LOC l ON a.LOC_ID = l.LOC_ID JOIN COORDINATE c ON l.LOC_START_LNG = c.LOC_START_LNG WHERE c.LOC_CITY = \'{city_name}\'")
        data = cur.fetchall()
        df = pd.DataFrame(data)
        cur.close()
        conn.close()

        if data:
            st.table(df)
        else:
            st.info("No records found.")
    except Exception as e:
        st.error(f"Error: {e}")

# --- Retrieve Data From Provider ---
if choice == "Time Period Query":
    st.write("### Retrieve Data From Provider")
    time_start = st.text_input("Enter a Start Date (YYYY-MM-DD HH24:MI:SS)")
    time_end = st.text_input("Enter a End Date (YYYY-MM-DD HH24:MI:SS)")
    try:
        conn = get_connection()
        cur = conn.cursor()
        cur.execute(f"Select a.ACC_ID, a.ACC_DESCRIPTION, a.TIME_ID, t.TIME_ID, t.TIME_START, t.TIME_END FROM ACCIDENT a JOIN TIM t ON a.TIME_ID = t.TIME_ID WHERE (t.TIME_START > TO_DATE(\'{time_start}\', 'YYYY-MM-DD HH24:MI:SS')) AND (t.TIME_END < TO_DATE(\'{time_end}\', 'YYYY-MM-DD HH24:MI:SS'))" )
        data = cur.fetchall()
        df = pd.DataFrame(data)
        cur.close()
        conn.close()

        if data:
            st.table(df)
        else:
            st.info("No records found.")
    except Exception as e:
        st.error(f"Error: {e}")